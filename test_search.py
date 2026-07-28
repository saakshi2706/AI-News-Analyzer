from tools import search_articles

keyword = input("Enter a keyword: ")

results = search_articles(keyword)

if results:
    print(f"\nFound {len(results)} matching article(s):\n")

    for article in results:
        print("=" * 60)
        print("Title:", article["title"])
        print("URL:", article["url"])
        print("Published:", article["published_date"])
        print("\nAnalysis:")
        print(article["analysis"])
        print("=" * 60)
else:
    print("\nNo matching articles found.")