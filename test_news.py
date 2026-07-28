from news_fetcher import fetch_news

articles = fetch_news("AI")

print()

for article in articles:
    print(article["title"])