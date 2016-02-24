import requests
from bs4 import BeautifulSoup

r = "http://www.amazon.com/gp/product/B009ZDQWBY/"

request = requests.get(r)
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "priceblock_ourprice",
                             "class": "a-size-medium a-color-price"})
print(element.text.strip())