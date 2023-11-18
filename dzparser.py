# biblioteki
import requests
import lxml
from bs4 import BeautifulSoup
#chistka
f = open('output.txt', 'r+')
f.truncate(0)
f.close()
#bazovie danie
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
headers = {"User-agent" : user}
sess = requests.Session()
counter = 0
#kod
for j in range (1,6):
  url = f"https://cash-backer.club/shops?page={j}"
  resp = sess.get(url, headers = headers)
  soup = BeautifulSoup(resp.text, "html.parser")
  products = soup.findAll("div", class_ = 'col-lg-2 col-md-3 shop-list-card pseudo-link no-link')
  for product in products:
    counter += 1
    title = product.find("div", class_ = "shop-title").text
    cashback = product.find("div", class_ = "shop-rate").text
    with open('output.txt', "a", encoding = "utf-8") as file:
      file.write(f"Shop No {counter}Name: {title} Cashback: {cashback}\n")