import requests
from bs4 import BeautifulSoup
import json

data = []
position = 0

for page in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")

    books = soup.findAll("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    for book in books:
        title = f"Title: {book.find("h3").find("a").get("title")}"
        img = f"Image: {book.find("div", class_="image_container").find("img").get("src")}"
        link = f'Link: https://books.toscrape.com/catalogue/{book.find("div", 
                                                                       class_="image_container").find("a").get("href")}'
        rating = f"Rating: {book.find("p").get("class")[1]} / Five"
        price = f'Price: {book.find("div", class_="product_price").find("p").text[1:]}'
        stock = f'Stock: {book.find("div", class_="product_price").find("p", 
                                                                        class_="instock availability").text.strip()}'

        data.append([title, img, link, rating, price, stock])
#
# for i in data:
#     position += 1
#     print(f"Position {position}: {i}")
#
#
# print(len(data))
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)
with open('data.json', 'r') as json_file:
    loaded_list = json.load(json_file)
    print(loaded_list)
