from bs4 import BeautifulSoup
import requests

"""
request - запрос 

response - ответ
"""

# parsing = requests.get(url="https://www.nbkr.kg/index.jsp?lang=RUS")
# soup = BeautifulSoup(parsing.text)

# courses = soup.find_all("table", class_="table table-striped")

# for i in courses:
#     print(i.text)

# print(courses)


response = requests.get(url="https://24.kg/")
soup = BeautifulSoup(response.text, "lxml")

news = soup.find_all("div", class_="col-sm-9 col-xs-12")
# prices = soup.find_all("div", class_="product__item-price")

for name in zip(news):
    print(f"\nНазвание товара - {name.text} ")