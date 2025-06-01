import sys
import os
from typing import Dict, List, Any
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
# sys.path.append('..')
from config import OLLAMA_HOST, GEMMA_MODEL, SERVICES


class RepairResponse(BaseModel):
    """Response structure for repair inquiries."""
    service_type: str = Field(description="Type of repair service needed")
    issue_description: str = Field(description="Description of the issue")
    next_steps: str = Field(description="Suggested next steps")
    request_additional_info: bool = Field(description="Whether to request more information")
    additional_info_needed: str = Field(description="What additional information is needed")


class GemmaLLMChain:
    def __init__(self):
        print(f"Debug - GEMMA_MODEL from config: {GEMMA_MODEL}")
        print(f"Debug - OLLAMA_HOST from config: {OLLAMA_HOST}")
        self.llm = OllamaLLM(base_url=OLLAMA_HOST, model=GEMMA_MODEL)
        print(f"Debug - LLM model name: {self.llm.model}")
        self._load_prompt_template()
        self.output_parser = PydanticOutputParser(pydantic_object=RepairResponse)
        
    def _load_prompt_template(self):
        """Load the prompt template from file."""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(script_dir, 'prompt_templates', 'system_prompt.txt')
        
        with open(prompt_path, 'r') as file:
            self.system_prompt = file.read()

    def create_chain(self):
        """Create a LangChain chain using the Gemma model."""
        prompt = PromptTemplate(
            template=self.system_prompt + "\n\nUser query: {query}\n\n",
            input_variables=["query"],
            partial_variables={"format_instructions": self.output_parser.get_format_instructions(),
                              "services": str(SERVICES)}
        )
        
        return prompt | self.llm

    def process_query(self, query: str) -> Dict[str, Any]:
        """Process a user query and return structured response."""
        chain = self.create_chain()
        result = chain.invoke({"query": query})
        
        try:
            parsed_response = self.output_parser.parse(result)
            return parsed_response.dict()
        except Exception as e:
            print(f"Error parsing LLM response: {e}")
            # Fallback response
            return {
                "service_type": "unknown",
                "issue_description": "I couldn't understand the issue clearly.",
                "next_steps": "Could you please explain your appliance problem again?",
                "request_additional_info": True,
                "additional_info_needed": "Please describe what appliance is having issues and what symptoms you're experiencing."
            }
