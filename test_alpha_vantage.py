import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ["ALPHA_VANTAGE_KEY"]
symbol = "AAPL"

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&{symbol}=IBM&apikey={api_key}'
api_key = os.environ["ALPHA_VANTAGE_KEY"]
r = requests.get(url)
data = r.json()

print(data)

response = requests.get(url)
data = response.json()

print("✅ Alpha Vantage API Working!")
print(f"Stock: {symbol}")
print(f"Response: {data}")