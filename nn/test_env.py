# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    print("✅ GOOGLE_API_KEY loaded successfully.")
else:
    print("❌ GOOGLE_API_KEY not found. Check your .env file.")
