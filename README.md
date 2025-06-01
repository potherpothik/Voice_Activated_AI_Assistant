# Voice-Activated AI Assistant for Home Appliance Repair

A voice-activated AI assistant that helps users troubleshoot and get repair guidance for home appliances. The assistant uses natural language processing and speech recognition to provide interactive support for various home appliances.

## Features

- 🎤 Voice Input: Speak naturally to interact with the assistant
- 🔊 Voice Output: Get spoken responses from the assistant
- 🤖 AI-Powered: Uses advanced language models for understanding and responses
- 🏠 Appliance Support: Specialized knowledge for various home appliances
- 🔄 Interactive: Two-way conversation with follow-up questions
- 📱 Easy to Use: Simple voice interface

## Supported Appliances

- Air Conditioners
- Refrigerators
- Ovens
- Washing Machines
- And more...

## Prerequisites

- Python 3.8 or higher
- Internet connection (for Google Text-to-Speech)
- Microphone and speakers

## Installation

1. Clone the repository:
```bash
git clone https://github.com/potherpothik/Voice_Activated_AI_Assistant.git
cd Voice_Activated_AI_Assistant
```

2. Create and activate a virtual environment:
```bash
python -m venv env
# On Windows
env\Scripts\activate
# On Unix or MacOS
source env/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Project Structure

```
Voice_Activated_AI_Assistant/
├── voice/               # Voice processing modules
│   ├── stt.py          # Speech-to-Text implementation
│   └── tts.py          # Text-to-Speech implementation
├── llm/                # Language model integration
│   └── gemma_chain.py  # LLM processing chain
├── embeddings/         # Service embeddings
├── services/          # Appliance-specific services
├── utils/             # Utility functions
├── main.py            # Main application entry point
└── requirements.txt   # Project dependencies
```

## Usage

1. Start the assistant:
```bash
python main.py
```

2. Wait for the "Listening..." prompt
3. Speak your question or describe your appliance issue
4. Listen to the assistant's response
5. Continue the conversation as needed

## Example Interactions

User: "My refrigerator is making a strange noise"
Assistant: "I understand you're having an issue with your refrigerator. Could you describe the noise you're hearing? Is it a buzzing, clicking, or humming sound?"

User: "The washing machine won't drain"
Assistant: "Let me help you with your washing machine drainage issue. First, let's check if there's any blockage in the drain hose..."

## Dependencies

- gTTS (Google Text-to-Speech)
- PyAudio
- pygame
- langchain
- ollama
- And other dependencies listed in requirements.txt

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Text-to-Speech for voice synthesis
- Gemma LLM for natural language processing
- All contributors and users of the project 