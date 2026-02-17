from dotenv import load_dotenv
import os

load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=os.environ["GROQ_API_KEY"]
)

response = llm.invoke("Explain what a stock P/E ratio means in one sentence.")
print("✅ LLM Connection Working!")
print(f"Response: {response.content}")
