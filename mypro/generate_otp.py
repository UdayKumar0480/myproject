from tkinter import *
from tkinter import messagebox
import random
win=Tk()
win.title("OTP Generator")
win.geometry("300x200")


def getotp():
	messagebox.showinfo(title='OTP',message=f'your OTP is :{random.randint(1000,9999)}')
Label(text='------------ click to Generate OTP ---------',font=12).pack(fill='x',pady=6)
but=Button(text="Generate",command=getotp,padx=10).pack(pady=2)
win.mainloop()
