# 📰 AI News Analyzer

An AI-powered web application that allows users to search for the latest news articles on any topic and view them through a clean, modern interface. The application fetches real-time news using NewsAPI and presents the results in an easy-to-read dashboard built with Flask and Bootstrap.

---

## 📌 Features

- 🔍 Search news on any keyword (AI, Tesla, Cricket, Apple, etc.)
- 🌍 Fetches real-time news using NewsAPI
- 📰 Displays latest articles with title, source, publication date, and summary
- 📖 Direct link to the complete news article
- 🎨 Modern and responsive Bootstrap interface
- ⚡ Fast search with Flask backend
- 🔐 Secure API key management using environment variables

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- Font Awesome

### Backend
- Python
- Flask

### APIs
- NewsAPI

### Libraries
- requests
- python-dotenv

---

## 📂 Project Structure

```
AI-News-Analyzer/
│
├── app.py
├── news_fetcher.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── data/
│
└── output/
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/saakshi2706/AI-News-Analyzer.git
```

### 2. Navigate to the project

```bash
cd AI-News-Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` file

```env
NEWS_API_KEY=YOUR_NEWSAPI_KEY
```

---

## ▶️ Run the Project

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📸 Application Workflow

1. User enters a keyword.
2. Flask receives the request.
3. NewsAPI fetches the latest articles.
4. Articles are processed by the backend.
5. Results are displayed in a responsive interface.
6. Users can open the original news article with a single click.

---

## 🎯 Project Objectives

- Simplify access to real-time news.
- Provide an intuitive and responsive user interface.
- Allow users to search news across multiple domains.
- Demonstrate integration of REST APIs with Flask.
- Showcase full-stack web development skills.

---

## 🔮 Future Enhancements

- AI-generated article summaries using LLMs
- Sentiment Analysis
- News Categorization
- Bookmark favourite articles
- User authentication
- Search history
- Dark Mode
- Trending Topics
- Multi-language support

---

## 👩‍💻 Author

**Saakshi Tewari**

GitHub: https://github.com/saakshi2706

---

## 📄 License

This project is developed for educational and learning purposes.
