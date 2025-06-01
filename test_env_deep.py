# test_env_deep.py
import os
from dotenv import load_dotenv
import sys

def print_divider(title):
    print(f"\n{'='*40}")
    print(f"=== {title}")
    print(f"{'='*40}")

print_divider("ENVIRONMENT VARIABLES BEFORE LOADING .env")
for k, v in os.environ.items():
    if "GEMMA" in k or "OLLAMA" in k or "DEEPGRAM" in k:
        print(f"{k}: {v}")
    elif k == "PATH":
        # Print just the beginning of PATH to avoid huge output
        print(f"PATH: {v[:200]}... [truncated]")
    elif "PYTHON" in k or "VIRTUAL" in k:
        print(f"{k}: {v}")

print_divider("LOADING .env FILE")
try:
    # Try loading from current directory
    load_dotenv() 
    print("Loaded .env from current directory")
except Exception as e:
    print(f"Error loading .env: {e}")

print_divider("ENVIRONMENT VARIABLES AFTER LOADING .env")
print(f"GEMMA_MODEL: {os.getenv('GEMMA_MODEL')}")
print(f"OLLAMA_HOST: {os.getenv('OLLAMA_HOST')}")
print(f"DEEPGRAM_API_KEY: {os.getenv('DEEPGRAM_API_KEY')}")

print_divider("DIRECT .env FILE CONTENTS")
try:
    with open('.env', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print(".env file not found in current directory")
except Exception as e:
    print(f"Error reading .env: {e}")

print_divider("PYTHON PATH")
for path in sys.path:
    print(path)

print_divider("CURRENT WORKING DIRECTORY")
print(os.getcwd())

print_divider("FILE LISTING")
try:
    for item in os.listdir():
        print(item)
except Exception as e:
    print(f"Error listing directory: {e}")