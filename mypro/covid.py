'''
from covid import Covid
import matplotlib.pyplot as pyplot
#country = India
country = input("Enter your country name: ")

covid = Covid()
data = covid.get_status_by_country_name(country)
collect = {
	key: data[key]
	for key in data.keys() & {"confirmed","active","recovered","deaths"}
}
n = list(collect.keys())
v = list(collect.values())
print(collect)

pyplot.title(Country)
pyplot.bar(range(len(collect)), v, tick_label=n)
pyplot.show()



import requests
import pywhatkit as kit
from bs4 import BeautifulSoup
url = "https://www.worldometers.info/coronavirus/?"
r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
data = s.find_all("div",class_="maincounter-number")
print("Total Cases: ",data[0].text.strip())
print("Total Deaths: ",data[1].text.strip())
print("Total Recovered: ",data[2].text.strip())


C = ("Total Cases: ",data[0].text.strip())
D = ("Total Deaths: ",data[1].text.strip())
R = ("Total Recovered: ",data[2].text.strip())
'''


import COVID19Py
covid19 = COVID19Py.COVID19()
data = covid19.getAll(timelines=True)
virusdetails=dict(data["latest"])
names = list(virusdetails.keys())
values = list(virusdetails.values())
print(virusdetails)