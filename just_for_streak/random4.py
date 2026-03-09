import os
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from collections import Counter
import csv
from urllib.parse import urlparse
from datetime import datetime

# === Setup directories ===
RAW_DIR = "data/raw"
ARTICLES_DIR = "data/articles"
SUMMARY_FILE = "data/articles_summary.csv"
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(ARTICLES_DIR, exist_ok=True)

# === Step 1: Fetch main page ===
url = input("Enter the url of the webpage to scrape: ").strip()
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
response.raise_for_status()

# Save raw HTML
domain = urlparse(url).netloc.replace(".", "_")
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
raw_file = os.path.join(RAW_DIR, f"{domain}_{timestamp}.html")
with open(raw_file, "w", encoding="utf-8") as f:
    f.write(response.text)
print(f"Saved HTML to: {raw_file}")

soup = BeautifulSoup(response.text, "html.parser")

# Page Title
page_title = soup.title.string.strip() if soup.title else "No Title"
print("Page Title: ", page_title)

# === Step 2: Extract article links ===
links = []
for a in soup.find_all("a", href=True):
    href = a["href"]
    if href.startswith("/"):
        full_url = "https://www.bbc.com" + href
    elif href.startswith("http"):
        full_url = href
    else:
        continue

    # filter BBC article links
    if "/news/articles/" in full_url:
        if full_url not in links:
            links.append(full_url)

print(f"\nFound {len(links)} article-like links:")
for l in links:
    print(l)


# === Step 3: Function to fetch & analyze articles ===
def fetch_and_analyze_article(url, article_id):
    """Fetch article, extract metadata, analyze sentiment, and save."""
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        # ---- Metadata ----
        title = soup.find("h1")
        title = title.get_text(strip=True) if title else "N/A"

        author = soup.find("span", {"class": "ssrcss-68pt20-Text-TextContributorName"})
        author = author.get_text(strip=True) if author else "N/A"

        date = soup.find("time")
        date = date.get("datetime") if date else "N/A"

        # ---- Article Text ----
        paragraphs = soup.find_all("p")
        text = " ".join(p.get_text() for p in paragraphs)

        # Save raw text
        article_path = os.path.join(ARTICLES_DIR, f"article_{article_id}.txt")
        with open(article_path, "w", encoding="utf-8") as f:
            f.write(text)

        # ---- Sentiment ----
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        sentiment = "Positive" if polarity > 0.05 else "Negative" if polarity < -0.05 else "Neutral"

        # ---- Top Words ----
        words = [w.lower() for w in blob.words if w.isalpha()]
        freq = Counter(words)
        top_words = ", ".join([f"{w}:{c}" for w, c in freq.most_common(10)])

        # Print live progress
        print(f"\nArticle {article_id}: {title}")
        print(f" Author: {author}")
        print(f" Date: {date}")
        print(f" Saved to: {article_path}")

        # Return row for CSV
        return [article_id, title, author, date, url, polarity, subjectivity, sentiment, top_words]

    except Exception as e:
        print(f"⚠️ Error fetching {url}: {e}")
        return [article_id, "ERROR", "N/A", "N/A", url, 0, 0, "N/A", ""]


# === Step 4: Save summaries to CSV ===
with open(SUMMARY_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Title", "Author", "Date", "URL", "Polarity", "Subjectivity", "Sentiment", "Top Words"])
    for i, link in enumerate(links[:5], 1):  # limit to 5 articles for demo
        print(f"\nFetching article {i}: {link}")
        row = fetch_and_analyze_article(link, i)
        writer.writerow(row)

print(f"\n✅ Saved summary of {min(5, len(links))} articles to {SUMMARY_FILE}")


import pandas as pd

def search_interface():
    print("\n=== Article Search Interface ===")
    df = pd.read_csv(SUMMARY_FILE)

    while True:
        print("\nOptions:")
        print("1. Search by keyword in title")
        print("2. Filter by sentiment (Positive/Negative/Neutral)")
        print("3. Show top N articles")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            keyword = input("Enter keyword to search in titles: ").strip().lower()
            results = df[df["Title"].str.lower().str.contains(keyword, na=False)]
            print(results[["ID", "Title", "Sentiment"]])

        elif choice == "2":
            sent = input("Enter sentiment (Positive/Negative/Neutral): ").strip().capitalize()
            results = df[df["Sentiment"] == sent]
            print(results[["ID", "Title", "Sentiment"]])

        elif choice == "3":
            try:
                n = int(input("How many articles to display? "))
            except ValueError:
                n = 5
            print(df.head(n)[["ID", "Title", "Sentiment"]])

        elif choice == "4":
            print("Exiting search interface...")
            break

        else:
            print("❌ Invalid choice, try again.")


# === Run search menu after scraping ===
search_interface()
