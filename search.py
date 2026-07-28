import json

with open("output/parsed_articles.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

query = input("Enter keyword: ").lower()

results = []

for article in articles:

    if (
        query in article["title"].lower()
        or query in article["summary"].lower()
        or query in article["category"].lower()
        or query in article["sentiment"].lower()
        or any(query in keyword.lower() for keyword in article["keywords"])
    ):
        results.append(article)

print()

if results:

    print(f"Found {len(results)} article(s)\n")

    for article in results:

        print("=" * 60)
        print("Title:", article["title"])
        print("Category:", article["category"])
        print("Sentiment:", article["sentiment"])
        print("Summary:", article["summary"])
        print("Keywords:", ", ".join(article["keywords"]))
        print("URL:", article["url"])

else:
    print("No matching articles found.")