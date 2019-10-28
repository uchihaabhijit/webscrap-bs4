from bs4 import BeautifulSoup
import requests

URL = "https://www.snapdeal.com/product/hp-15-da1058tu-notebook-core/626504829157"

headers = { "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36" }

html = requests.get(URL, headers=headers).text

soup = BeautifulSoup(html, 'html5lib')
span = soup.find("span", class_="payBlkBig")
final_price = int(span.text)

if final_price < 25299:
    print("The price has decreased. Go buy!")
else:
    print("The price is still the same or has increased")