from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.environ["NEWS_API_KEY"]
keyword = ""

# Search for stock market news
url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}&pageSize=3&language=en"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("✅ NewsAPI Working!")
    print(f"Total results: {data.get('totalResults', 0)}")
    
    if 'articles' in data:
        print("\nTop 3 articles:")
        for i, article in enumerate(data['articles'][:3], 1):
            print(f"\n{i}. {article['title']}")
            print(f"   Source: {article['source']['name']}")
            print(f"   Published: {article['publishedAt'][:10]}")
else:
    print(f"❌ Error: {data.get('message', 'Unknown error')}")