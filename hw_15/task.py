import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

books = soup.findAll("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

data = []

for book in books:
    title = f"Title: {book.find("h3").find("a").get("title")}"
    img = f"Image: {book.find("div", class_="image_container").find("img").get("src")}"
    link = f'Link: {url}{book.find("div", class_="image_container").find("a").get("href")}'
    rating = f"Rating: {book.find("p").get("class")[1]} / Five"
    price = f'Price: {book.find("div", class_="product_price").find("p").text[1:]}'
    stock = f'Stock: {book.find("div", class_="product_price").find("p", class_="instock availability").text.strip()}'

    data.append([title, img, link, rating, price, stock])

position = 0

for i in data:
    position += 1
    print(f"Position {position}: {i}")
