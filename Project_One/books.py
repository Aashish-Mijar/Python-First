import requests
from bs4 import BeautifulSoup 
import pandas as pd

# Starting page
page = 1
all_books = []

# Keep scraping pages until no more are found
while True:
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)

 # If the page doesn't exist, stop
    if response.status_code != 200:
        break
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

 # If no books found, stop
    if not books:
        break

 # Loop through each book and get title + price
    for book in books:
        title = book.h3.a["title"]
        raw_price = book.find("p", class_="price_color").text
        clean_price = raw_price.replace("£", "").replace("Â", "").strip()

        try:
            price = float(clean_price)
        except ValueError:
            continue # Skip if price can't be converted
        all_books.append({"Title": title, "Price": price})
    print(f" Page {page} scraped.")
    page += 1 # Go to next page

# Convert list to a table
df = pd.DataFrame(all_books)

# Save table to CSV file
df.to_csv("books.csv", index=False)
print("\n Done! Books saved to 'books.csv'")