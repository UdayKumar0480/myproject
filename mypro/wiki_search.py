import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo
win = Tk()
win.title("wikipedia")
win.geometry("500x200")
def serach_wiki():
	serach = entry.get()
	answer = wikipedia.summary(serach)
	showinfo("wikipedia Answer",answer)
label = Label(win,text="wikipedia Search: ")
label.grid(row=0,column=0)
entry = Entry(win)
entry.grid(row=1,column=0)
button = Button(win,text="Search",command=serach_wiki)
button.grid(row=1,column=1,padx=10)
win.mainloop()