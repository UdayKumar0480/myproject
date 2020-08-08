import requests
from bs4 import BeautifulSoup
from plyer import notification
import time
import pywhatkit as kit
res = requests.get("https://www.worldometers.info/coronavirus/").text
soup = BeautifulSoup(res,"html.parser")
soup.encode("utf-8")
cases = soup.find("div",{"class":"maincounter-number"}).get_text().strip()
kit.sendwhatmsg("+916302258525","Hi This is system generated message and total carona cases are: ",cases,18,10)
def notifyMe(title,message):
	notification.notify(
	title = title,
	message = message,
	timeout = 5 )
	
while True:
	notifyMe("Total Number of cases",cases)
	print("success")
	time.sleep(10)
#kit.sendwhatmsg("+916302258525","Hi This is system generated message and total carona cases are: ",cases,17,55)
