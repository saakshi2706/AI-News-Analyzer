import json

def search_articles(query):
    with open("output/analysis.json", "r", encoding="utf-8") as file:
        articles = json.load(file)

    results = []

    query = query.lower()

    for article in articles:
        if (
            query in article["title"].lower()
            or query in article["analysis"].lower()
        ):
            results.append(article)

    return results