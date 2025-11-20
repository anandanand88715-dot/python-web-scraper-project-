import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

titles = []
prices = []

for book in books:
    titles.append(book.h3.a["title"])
    prices.append(book.find("p", class_="price_color").text)

data = pd.DataFrame({
    "Title": titles,
    "Price": prices
})

data.to_csv("scraped_report.csv", index=False)

print("Scraping completed. File saved as scraped_report.csv")
