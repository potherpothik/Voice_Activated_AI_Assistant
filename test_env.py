# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load from current directory

print(f"DEEPGRAM_API_KEY exists: {'DEEPGRAM_API_KEY' in os.environ}")
print(f"GEMMA_MODEL value: {os.getenv('GEMMA_MODEL')}")
print(f"OLLAMA_HOST value: {os.getenv('OLLAMA_HOST')}")