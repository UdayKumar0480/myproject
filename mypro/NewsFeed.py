import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
news_url="https://news.google.com/rss"
#news_url="https://epaper.eenadu.net/Home/Index/rss"
#https://epaper.eenadu.net/Home/Index/rss
Client=urlopen(news_url)
xml_page=Client.read()
soup_page=soup(xml_page,"xml")
news_list = soup_page.findAll("item")
for news in news_list:
	print(news.title.text)
	print(news.link.text)
	print(news.pubDate.text)
	print("_"*60)