import json
import os

# -----------------------------
# Load analyzed articles
# -----------------------------

with open("output/analysis.json", "r", encoding="utf-8") as file:
    articles = json.load(file)

parsed_articles = []

# -----------------------------
# Parse every article
# -----------------------------

for article in articles:

    title = article.get("title", "").strip()
    url = article.get("url", "").strip()
    published_date = article.get("published_date", "").strip()

    summary = article.get("summary", "").strip()
    category = article.get("category", "").strip()
    sentiment = article.get("sentiment", "").strip()

    keywords = article.get("keywords", [])

    # Remove duplicate keywords
    keywords = list(dict.fromkeys(keywords))

    parsed_articles.append({
        "title": title,
        "url": url,
        "published_date": published_date,
        "summary": summary,
        "category": category,
        "sentiment": sentiment,
        "keywords": keywords
    })

# -----------------------------
# Save parsed data
# -----------------------------

os.makedirs("output", exist_ok=True)

with open("output/parsed_articles.json", "w", encoding="utf-8") as file:
    json.dump(parsed_articles, file, indent=4, ensure_ascii=False)

print("Parsing Complete!")
print(f"Parsed {len(parsed_articles)} articles.")
print("Saved to output/parsed_articles.json")