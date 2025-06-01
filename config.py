import os
from dotenv import load_dotenv
from pathlib import Path

# Get the absolute path to this config.py file
current_dir = Path(__file__).resolve().parent

# Load environment variables from .env file in the project root
env_path = current_dir / ".env"  # .env is in same directory as config.py
load_dotenv(dotenv_path=env_path)

# Debug output
print(f"🔧 CONFIG LOADED FROM: {env_path}")
print(f"🔧 GEMMA_MODEL={os.getenv('GEMMA_MODEL')}")
print(f"🔧 OLLAMA_HOST={os.getenv('OLLAMA_HOST')}")

# Deepgram API configuration
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

# Ollama configuration
OLLAMA_HOST="http://localhost:11434"
GEMMA_MODEL="gemma:2b"
EMBEDDING_MODEL="nomic-embed-text"

print(f"⛑️  FORCED CONFIG: GEMMA_MODEL={GEMMA_MODEL}")

# Audio configuration
AUDIO_FORMAT = 'wav'
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 5

# Service descriptions
SERVICES = {
    "ac_repair": {
        "name": "Air Conditioning Repair",
        "description": "Repair and maintenance services for AC units including cooling issues, strange noises, water leakage, and thermostat problems.",
        "common_issues": ["not cooling", "strange noises", "water leakage", "thermostat issues", "blowing warm air"],
        "price_range": "$80-$300"
    },
    "fridge_repair": {
        "name": "Refrigerator Repair",
        "description": "Repair services for all types of refrigerators addressing cooling problems, water leakage, ice maker issues, and unusual noises.",
        "common_issues": ["not cooling", "water leaking", "ice maker not working", "unusual noises", "freezing food"],
        "price_range": "$100-$350"
    },
    "oven_repair": {
        "name": "Oven Repair",
        "description": "Repair services for electric and gas ovens including heating problems, temperature inconsistency, and control panel issues.",
        "common_issues": ["not heating", "uneven cooking", "temperature issues", "control panel failures", "strange odors"],
        "price_range": "$90-$320"
    },
    "washing_machine": {
        "name": "Washing Machine Repair",
        "description": "Repair services for washing machines addressing problems with spinning, draining, leaking, and unusual noises.",
        "common_issues": ["not spinning", "not draining", "leaking water", "making loud noises", "stuck on spin cycle"],
        "price_range": "$85-$310"
    }
}
