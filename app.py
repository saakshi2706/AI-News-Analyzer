from flask import Flask, render_template, request
from news_fetcher import fetch_news

app = Flask(__name__)

# ------------------------
# Home Page
# ------------------------

@app.route("/")
def home():
    return render_template(
        "index.html",
        articles=[],
        keyword=""
    )


# ------------------------
# Search
# ------------------------

@app.route("/search")
def search():

    keyword = request.args.get("keyword", "").strip()

    if keyword == "":
        return render_template(
            "index.html",
            articles=[],
            keyword=""
        )

    try:
        articles = fetch_news(keyword)
    except Exception as e:
        print("Error:", e)
        articles = []

    return render_template(
        "index.html",
        articles=articles,
        keyword=keyword
    )


# ------------------------
# Run Flask
# ------------------------

if __name__ == "__main__":
    app.run(debug=True)