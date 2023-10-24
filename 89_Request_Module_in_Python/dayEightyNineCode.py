import requests
from bs4 import BeautifulSoup
# response=requests.get("https://www.google.com")
# print(response)
url="https://www.codewithharry.com/blogpost/django-cheatsheet/"
res=requests.get(url)

soup=BeautifulSoup(res.tex,'html.parser')
print(soup.prettify())