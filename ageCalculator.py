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
heading = Label(window, text = "Age calculator", bg = "black", fg = "white", font = ("Ariel", 30))
name = Label(window, text = "enter age here: ", font = ("Ariel", 15))

Submit = Button(window, text = "submit", bg = "purple", fg = "white", command = calculate)

BirthYear = Entry(window, width = 30, fg = "red")

heading.place(x = 185, y = 50)
name.place(x = 210, y = 150)
BirthYear.place(x = 210, y = 192)
Submit.place(x = 250, y = 450)

window.mainloop()