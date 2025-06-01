import asyncio
import os
import sys
from voice.stt import SpeechToText
from voice.tts import TextToSpeech
from llm.gemma_chain import GemmaLLMChain
from embeddings.generate_embeddings import ServiceEmbeddings
from services import get_service

# Ensure the project root is in Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class VoiceAssistant:
    def __init__(self):
        self.stt = SpeechToText()
        self.tts = TextToSpeech()
        self.llm_chain = GemmaLLMChain()
        self.service_embeddings = ServiceEmbeddings()
        
        # Load or generate service embeddings
        if not self.service_embeddings.load_embeddings():
            print("Generating service embeddings...")
            self.service_embeddings.generate_service_embeddings()
    
    async def run(self):
        """Run the voice assistant."""
        print("Voice Assistant for Home Appliance Repair is ready!")
        print("Speak after the prompt...")
        
        try:
            while True:
                # Step 1: Record and transcribe speech
                print("\n🎤 Listening...")
                audio_path = self.stt.record_audio()
                transcript = await self.stt.transcribe_audio(audio_path)
                
                if not transcript.strip():
                    print("I didn't catch that. Please try again.")
                    await self.speak("I didn't catch that. Please try again.")
                    continue
                
                print(f"🔊 You said: {transcript}")
                
                # Step 2: Process the query with the LLM
                print("🧠 Processing...")
                llm_response = self.llm_chain.process_query(transcript)
                
                # Step 3: Get more specific service response if applicable
                service_type = llm_response.get("service_type")
                if service_type != "unknown":
                    # Find the specific service
                    service = get_service(service_type)
                    if service:
                        service_response = service.get_response(llm_response.get("issue_description", ""))
                        response_text = service_response.get("response_text", "")
                        follow_up = service_response.get("follow_up_question", "")
                        final_response = f"{response_text} {follow_up}"
                    else:
                        final_response = f"{llm_response.get('next_steps', '')}"
                else:
                    final_response = f"I'm not sure I understand what appliance you're having trouble with. Could you please specify if it's an air conditioner, refrigerator, oven, or washing machine issue?"
                
                print(f"🤖 Assistant: {final_response}")
                
                # Step 4: Convert response to speech and play it
                await self.speak(final_response)
                
        except KeyboardInterrupt:
            print("\nShutting down...")
        finally:
            # Clean up any temporary files
            self.stt.cleanup()
            self.tts.cleanup()
    
    async def speak(self, text: str):
        """Convert text to speech and play it."""
        audio_path = await self.tts.synthesize_speech(text)
        self.tts.play_audio(audio_path)


if __name__ == "__main__":
    assistant = VoiceAssistant()
    asyncio.run(assistant.run())
