import calendar
import pywhatkit as kit
y = int(input("input the year: "))
m = int(input("input the month: "))
my = (calendar.month (y,m))
kit.sendwhatmsg("+916302258525",my,15,48)