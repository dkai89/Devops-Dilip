from dotenv import load_dotenv
import os

load_dotenv()
print("Loaded API Key:", os.getenv("GOOGLE_API_KEY"))
