import requests
from bs4 import BeautifulSoup
import json

RSS_URL = "https://blog.python.org/feeds/posts/default?alt=rss&max-results=500"

print("Downloading RSS feed...")

response = requests.get(RSS_URL)

if response.status_code != 200:
    print("Could not download RSS feed.")
    exit()

rss = BeautifulSoup(response.content, "xml")

items = rss.find_all("item")

print(f"Found {len(items)} articles.\n")

articles = []

for item in items:

    article_url = item.find("link").text
    print("Scraping:", article_url)

    try:
        page = requests.get(article_url, timeout=10)

        if page.status_code != 200:
            continue

        soup = BeautifulSoup(page.text, "html.parser")

        title_tag = soup.find("h1")
        title = title_tag.get_text(strip=True) if title_tag else item.find("title").text

        time_tag = soup.find("time")
        published_date = time_tag.get("datetime", "") if time_tag else ""

        article = soup.find("article")

        content = ""

        if article:
            for p in article.find_all("p"):
                text = p.get_text(strip=True)

                if text:
                    content += text + "\n"

        if not content.strip():
            continue

        articles.append({
            "title": title,
            "url": article_url,
            "published_date": published_date,
            "content": content
        })

    except Exception as e:
        print("Skipped:", article_url)
        print(e)

with open("data/articles.json", "w", encoding="utf-8") as f:
    json.dump(articles, f, indent=4, ensure_ascii=False)

print()
print(f"Saved {len(articles)} articles successfully!")