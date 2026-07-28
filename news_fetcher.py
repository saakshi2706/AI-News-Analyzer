import os
import requests
from dotenv import load_dotenv

# -----------------------------
# Load Environment Variables
# -----------------------------

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

BASE_URL = "https://newsapi.org/v2/everything"

# -----------------------------
# Fetch News Function
# -----------------------------

def fetch_news(keyword):

    if not API_KEY:
        print("ERROR: NEWS_API_KEY not found!")
        return []

    params = {
        "q": keyword,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 10,
        "apiKey": API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        print("Request URL:", response.url)
        print("Status Code:", response.status_code)

        if response.status_code != 200:
            print("NewsAPI Error:")
            print(response.text)
            return []

        data = response.json()

        articles = []

        for article in data.get("articles", []):

            articles.append({
                "title": article.get("title", "No Title"),
                "url": article.get("url", ""),
                "published_date": article.get("publishedAt", ""),
                "summary": article.get("description") or "No summary available.",
                "content": article.get("content") or "",
                "source": article.get("source", {}).get("name", "Unknown"),
                "author": article.get("author") or "Unknown",
                "image": article.get("urlToImage"),
                "category": keyword.title()   # Since NewsAPI doesn't provide a category
            })

        print(f"\nFetched {len(articles)} articles successfully.")

        return articles

    except requests.exceptions.RequestException as e:
        print("Network Error:", e)
        return []

    except Exception as e:
        print("Unexpected Error:", e)
        return []