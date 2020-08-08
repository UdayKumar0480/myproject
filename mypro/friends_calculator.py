import random
import tkinter as tk
#from tkinter import Text,tk
import pandas as pd
import datetime
root = tk.Tk()
root.geometry("400x300")
root.title("Friendship Calculater")
result = 40+int(pd.datetime.now().second)
entername1 = tk.Entry(root,width=20, textvariable=name1)
entername1.grid(column=1,row=1)
YourFriendName = tk.Entry(root,width=20, textvariable=FriendName)
YourName.grid(column=1,row=2)
Press_button = tk.Button(text="     Check your Friendship     ",bg="pink",command=check)
Press_button.grid(column=2,row=4)
label_Your = tk.Label(root, text="Name: ",bg="red",font=(" ",15,"bold"))
label_Your.grid(row1,column=0,pady=5, padx=5)
label_Friend = tk.Label(root, text="Friend Name: ",bg="red",font=(" ",15,"bold"))
label_Friend.grid(row2,column=0,pady=5, padx=5)
def CheckFriendship():
	global result
	text_area = tk.Text(master=root,height=2,width=60,bg="#FFFF99")
	text_area.grid(column=0,row=5)
	result = ("friendship score is: ",result)
	text_area.insert(tk.END,result)
root.mainloop()