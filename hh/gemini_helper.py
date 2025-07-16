import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("AIzaSyAQD3ENsSfyq3BDom3TKLH3UZ0wmgUjd3g")
genai.configure(api_key=api_key)

# Use full model name (important!)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

def get_answer_from_chunks(question, chunks):
    responses = []
    for chunk in chunks:
        prompt = f"Given this text:\n\n{chunk}\n\nAnswer this question:\n{question}"
        try:
            response = model.generate_content(prompt)
            text = response.text
            if "does not mention" not in text and "cannot answer" not in text:
                responses.append(text.strip())
        except Exception as e:
            responses.append(f"Error: {e}")
    return responses or ["No relevant information found."]

