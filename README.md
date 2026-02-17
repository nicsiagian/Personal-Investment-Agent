# Personal-Investment-Agent

This project aims to build a personal investment agent that makes recommendations based on market history and economic factors. This agent helps retail and professional investors analyze individual stocks and optimize portfolio allocations by retrieving live market data, parsing news sentiment, and synthesizing insights via a RAG-powered LLM. It answers natural-language questions like "Should I rebalance my tech exposure?" or "What is the risk profile of NVDA right now?"

## Setup Instructions

### 1. Open in Codespaces
Click the green "Code" button → "Codespaces" → "Create codespace on main"

### 2. Add API Keys
Go to your GitHub Settings → Codespaces → Secrets and add:
- `GROQ_API_KEY` (get from https://console.groq.com/keys)
- `NEWSAPI_KEY` (get from https://newsapi.org/register)
- `ALPHAVANTAGE_KEY` (get from https://www.alphavantage.co/support/#api-key)

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Tests
```bash
# Test LLM connection
python test_llm.py

# Test vector store
python test_vectorstore.py

# Test agent (stretch goal)
python test_agent.py
```

## Provider Choice

**LLM:** Groq (Llama 3.3 70B)  
**Why:** 
- Higher free tier limits than Gemini (no quota issues)
- Faster inference speed (optimized hardware)
- Excellent performance on financial reasoning tasks

**Embeddings:** HuggingFace (all-MiniLM-L6-v2)  
**Why:** 
- Runs locally (no API key required)
- No rate limits or quota issues
- Good quality for semantic search on financial text
- CPU-friendly for Codespaces environment

## Project Structure
```
Personal-Investment-Agent/
├── README.md
├── requirements.txt
├── .gitignore
├── test_llm.py           # Proves LLM connection works
├── test_vectorstore.py   # Proves ChromaDB works
├── test_agent.py         # (Stretch) Proves agent works
└── src/
    ├── config.py
    └── tools/
        └── rag_tool.py
```

## Issues Encountered
- **Rate limits:** Switched from Gemini to Groq due to quota exhaustion on free tier
- **Embedding model compatibility:** Used HuggingFace embeddings instead of Gemini to avoid API quota issues
- **Metadata filtering:** ChromaDB filters required exact dict match
- **Chunking:** 500 tokens worked better than 1000 for financial news

## Next Steps
- [ ] Load real Yahoo Finance data
- [ ] Add live price fetch tool
- [ ] Build portfolio calculator
- [ ] Add news sentiment scoring