import tkinter as tk
import pyautogui as pg
root = tk.Tk()
root.title("SCREENSHOT GUI")
root.geometry("500x500")
def screenshot():
	screenshot=pg.screenshot()
	screenshot.save(r"C:\Users\Uday Kumar Gandluri\Desktop\My_Python_Personal\Songs\py_screenshots\screenshot.jpg")
capture=tk.Button(root,text="CAPTURE",command=screenshot)
capture.grid(row=3,column=3)
root.mainloop()