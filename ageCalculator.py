from tkinter import *
from datetime import date
import tkinter.messagebox
window = Tk()
window.geometry("600x600")
window.title("Age calculator")

todaysYear = date.today().year

def calculate():
    BirthNum = int(BirthYear.get())
    Age = todaysYear - BirthNum
    tkinter.messagebox.showinfo("Age", "Your age is " + str(Age))

Submit = Button(window, text = "submit", bg = "purple", fg = "white", command = calculate)

BirthYear = Entry(window, width = 30, fg = "red")

BirthYear.place(x = 115, y = 192)
Submit.place(x = 50, y = 450)

window.mainloop()