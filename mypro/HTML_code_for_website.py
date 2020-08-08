import requests
from bs4 import BeautifulSoup
URL = "https://www.youtube.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content,"html.parser")
print(sopu.prettify())