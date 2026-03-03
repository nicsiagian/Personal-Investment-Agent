from dotenv import load_dotenv
import os
import requests
from langchain_groq import ChatGroq

load_dotenv()

def get_stock_price(ticker):
    """Get current stock price"""
    api_key = os.environ["ALPHA_VANTAGE_KEY"]
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if "Global Quote" in data:
        quote = data["Global Quote"]
        return {
            "price": quote.get('05. price', 'N/A'),
            "change": quote.get('09. change', 'N/A'),
            "change_percent": quote.get('10. change percent', 'N/A'),
            "volume": quote.get('06. volume', 'N/A'),
            "date": quote.get('07. latest trading day', 'N/A')
        }
    return None

def get_stock_news(ticker):
    """Get recent news"""
    api_key = os.environ["NEWS_API_KEY"]
    url = f"https://newsapi.org/v2/everything?q={ticker}&pageSize=5&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    
    articles = []
    for article in data.get('articles', [])[:5]:
        # Fix: Handle None description
        description = article.get('description') or ''
        articles.append({
            "title": article['title'],
            "source": article['source']['name'],
            "date": article['publishedAt'][:10],
            "description": description[:150] if description else ''
        })
    return articles

def analyze_stock(ticker):
    """Complete stock analysis with Groq AI"""
    
    print(f"\n{'=' * 70}")
    print(f"ANALYZING: {ticker}")
    print('=' * 70)
    
    # Get data
    price = get_stock_price(ticker)
    news = get_stock_news(ticker)
    
    # Build context
    context = f"STOCK ANALYSIS FOR {ticker}\n\n"
    
    if price:
        context += "CURRENT PRICE DATA:\n"
        context += f"- Price: ${price['price']}\n"
        context += f"- Change: {price['change']} ({price['change_percent']})\n"
        context += f"- Volume: {price['volume']}\n"
        context += f"- Date: {price['date']}\n\n"
    else:
        context += "Price data unavailable\n\n"
    
    context += "RECENT NEWS:\n"
    for i, article in enumerate(news, 1):
        context += f"{i}. {article['title']}\n"
        context += f"   {article['source']} | {article['date']}\n"
        if article['description']:
            context += f"   {article['description']}...\n"
        context += "\n"
    
    # AI Analysis
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        groq_api_key=os.environ["GROQ_API_KEY"]
    )
    
    prompt = f"""{context}

Based on this data, provide a brief investment analysis:

1. **Price Sentiment**: Is the stock trending up or down? What does the price change indicate?
2. **News Sentiment**: What's the overall tone of recent news (bullish/bearish/neutral)?
3. **Investment Outlook**: Brief recommendation (2-3 sentences)

Keep it concise and actionable.
"""
    
    response = llm.invoke(prompt)
    
    print(context)
    print('=' * 70)
    print("AI ANALYSIS:")
    print('=' * 70)
    print(response.content)
    print('=' * 70)
    
    return response.content

def compare_stocks(ticker1, ticker2):
    """Compare two stocks side by side"""
    
    print(f"\n{'=' * 70}")
    print(f"COMPARING: {ticker1} vs {ticker2}")
    print('=' * 70)
    
    # Get data for both
    price1 = get_stock_price(ticker1)
    price2 = get_stock_price(ticker2)
    news1 = get_stock_news(ticker1)
    news2 = get_stock_news(ticker2)
    
    # Build comparison
    context = f"STOCK COMPARISON: {ticker1} vs {ticker2}\n\n"
    
    context += f"{ticker1}:\n"
    if price1:
        context += f"  Price: ${price1['price']} ({price1['change_percent']})\n"
    context += f"  Recent Headlines:\n"
    for article in news1[:3]:
        context += f"  - {article['title']}\n"
    
    context += f"\n{ticker2}:\n"
    if price2:
        context += f"  Price: ${price2['price']} ({price2['change_percent']})\n"
    context += f"  Recent Headlines:\n"
    for article in news2[:3]:
        context += f"  - {article['title']}\n"
    
    # AI Comparison
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        groq_api_key=os.environ["GROQ_API_KEY"]
    )
    
    prompt = f"""{context}

Compare these two stocks:
1. Which has better recent performance?
2. Which has more positive news sentiment?
3. Which would you recommend for a short-term investment and why?

Keep it brief and actionable.
"""
    
    response = llm.invoke(prompt)
    
    print(context)
    print('=' * 70)
    print("COMPARISON ANALYSIS:")
    print('=' * 70)
    print(response.content)
    print('=' * 70)

def analyze_portfolio(tickers):
    """Analyze multiple stocks in your portfolio"""
    
    print(f"\n{'=' * 70}")
    print(f"PORTFOLIO ANALYSIS: {', '.join(tickers)}")
    print('=' * 70)
    
    portfolio_data = []
    
    for ticker in tickers:
        price = get_stock_price(ticker)
        if price:
            portfolio_data.append({
                "ticker": ticker,
                "price": price['price'],
                "change_percent": price['change_percent']
            })
    
    # Build summary
    context = "PORTFOLIO SUMMARY:\n\n"
    for stock in portfolio_data:
        context += f"{stock['ticker']}: ${stock['price']} ({stock['change_percent']})\n"
    
    # AI Analysis
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        groq_api_key=os.environ["GROQ_API_KEY"]
    )
    
    prompt = f"""{context}

Analyze this portfolio:
1. Which stocks are performing best/worst?
2. Is the portfolio well-diversified?
3. Any recommendations for rebalancing?
"""
    
    response = llm.invoke(prompt)
    
    print(context)
    print('=' * 70)
    print("PORTFOLIO ANALYSIS:")
    print('=' * 70)
    print(response.content)
    print('=' * 70)

# Use it:
if __name__ == "__main__":
    analyze_portfolio(["AAPL", "NVDA", "TSLA", "MSFT", "GOOGL"])
