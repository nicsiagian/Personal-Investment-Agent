from dotenv import load_dotenv
import os

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  # Changed this line
    temperature=0,
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

response = llm.invoke("Explain what a stock P/E ratio means in one sentence.")
print("✅ LLM Connection Working!")
print(f"Response: {response.content}")