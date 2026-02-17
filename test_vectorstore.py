from dotenv import load_dotenv
import os

load_dotenv()

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

# No API key needed - runs locally
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

test_docs = [
    Document(
        page_content="Apple stock (AAPL) hit $180 per share on strong iPhone sales.",
        metadata={"ticker": "AAPL", "source": "test"}
    ),
    Document(
        page_content="NVIDIA (NVDA) announced new AI chips, stock rose 12%.",
        metadata={"ticker": "NVDA", "source": "test"}
    ),
    Document(
        page_content="The S&P 500 index tracks 500 large US companies.",
        metadata={"source": "test"}
    ),
]

print("Creating embeddings...")
vectorstore = Chroma.from_documents(
    test_docs, 
    embeddings, 
    persist_directory="./chroma_db"
)

print("Querying vector store...")
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
results = retriever.invoke("What happened with Apple?")

print("✅ Vector Store Working!")
print(f"Query: 'What happened with Apple?'")
print(f"\nTop results:")
for i, doc in enumerate(results, 1):
    print(f"{i}. {doc.page_content}")
    print(f"   Metadata: {doc.metadata}")