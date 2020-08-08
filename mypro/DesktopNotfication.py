
from tkinter import *
from win10toast import ToastNotifier

def send_notification(mgs):
	toaster = ToastNotifier()
	toaster.show_toast("New Notification",mgs)

root = Tk()
root.geometry("300x300")
mgs = Entry(root,width=30)
mgs.place(x = 20, y = 30)
button = Button(root,text = "Send Notification",bg="brown",fg="white",command = lambda: send_notification(mgs.get()))
button.place(x = 110, y = 200)
root.mainloop()


'''

# Python program to illustrate  
# desktop news notifier 
import feedparser 
import notify2 
import os 
import time 
def parseFeed(): 
    f = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml") 
    ICON_PATH = os.getcwd() + "/icon.ico"
    notify2.init('News Notify') 
    for newsitem in f['items']:  
        n = notify2.Notification(newsitem['title'],  
                                 newsitem['summary'],  
                                 icon=ICON_PATH  
                                 ) 
    n.set_urgency(notify2.URGENCY_NORMAL) 
    n.show() 
    n.set_timeout(15000) 
    time.sleep(1200)     
if __name__ == '__main__': 
    parseFeed() 
'''