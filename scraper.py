import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# --------------------------------------------
# STEP 1: Website URL to Scrape
# (Demo site – safe for scraping)
# --------------------------------------------
URL = "https://books.toscrape.com/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# --------------------------------------------
# STEP 2: Extract Book Titles & Prices
# --------------------------------------------
titles = []
prices = []

books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    
    titles.append(title)
    prices.append(price)

# --------------------------------------------
# STEP 3: Create DataFrame
# --------------------------------------------
df = pd.DataFrame({
    "Book Title": titles,
    "Price": prices,
    "Scraped On": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
})

# --------------------------------------------
# STEP 4: Save to CSV
# --------------------------------------------
file_name = "scraped_report.csv"
df.to_csv(file_name, index=False)

print("Scraping Completed Successfully!")
print("Saved File:", file_name)
print(df)
