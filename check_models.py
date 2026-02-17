from dotenv import load_dotenv
import os

load_dotenv()

import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

print("Available models for generateContent:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"  ✅ {model.name}")