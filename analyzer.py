import json
import os
import re
from collections import Counter

# -------------------------
# Load Articles
# -------------------------

with open("data/articles.json", "r", encoding="utf-8") as file:
    articles = json.load(file)

analysis_results = []

# -------------------------
# Keyword Dictionaries
# -------------------------

categories = {
    "Software Development": ["python", "release", "beta", "alpha", "version", "software"],
    "Cybersecurity": ["security", "vulnerability", "authentication", "exploit", "api"],
    "Community": ["community", "council", "election", "foundation", "packaging"],
}

positive_words = [
    "released", "improved", "success", "available",
    "announced", "fixed", "secure", "beta"
]

negative_words = [
    "bug", "error", "failed", "attack",
    "vulnerability", "exploit"
]

# -------------------------
# Analyze Articles
# -------------------------

for article in articles:

    title = article["title"]
    content = article["content"]

    text = (title + " " + content).lower()

    # -------------------------
    # Summary
    # -------------------------

    sentences = re.split(r'(?<=[.!?]) +', content)
    summary = " ".join(sentences[:2])

    # -------------------------
    # Category
    # -------------------------

    category = "General"

    for cat, words in categories.items():
        if any(word in text for word in words):
            category = cat
            break

    # -------------------------
    # Sentiment
    # -------------------------

    positive = sum(word in text for word in positive_words)
    negative = sum(word in text for word in negative_words)

    if positive > negative:
        sentiment = "Positive"
    elif negative > positive:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # -------------------------
    # Keywords
    # -------------------------

    words = re.findall(r'\b[a-zA-Z]{4,}\b', text)

    stopwords = {
        "this","that","with","have","from","will","been",
        "they","their","were","about","into","python",
        "https","blog","official","team","more"
    }

    words = [w for w in words if w not in stopwords]

    keywords = [w.title() for w, _ in Counter(words).most_common(4)]

    analysis_results.append({
        "title": title,
        "url": article["url"],
        "published_date": article["published_date"],
        "summary": summary,
        "category": category,
        "sentiment": sentiment,
        "keywords": keywords
    })

# -------------------------
# Save
# -------------------------

os.makedirs("output", exist_ok=True)

with open("output/analysis.json", "w", encoding="utf-8") as file:
    json.dump(analysis_results, file, indent=4, ensure_ascii=False)

print("Analysis Complete!")
print(f"Saved {len(analysis_results)} articles.")