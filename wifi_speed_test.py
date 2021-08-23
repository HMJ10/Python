from tkinter import *
from tkinter import messagebox
import pyspeedtest

def one():
    speed = pyspeedtest.SpeedTest("www.google.com")
    a1 = (str(speed.download()))
    new = float(a1) / 102400
    messagebox.showinfo("Your Download speed is ", new)


root = Tk()
root.title("INTERNET SPEED CHECKER")
root.configure(bg="blue")
root.geometry('500x250')

label1 = Label(root, text="Internet speed checker", font=("Arial", 30, "bold"), bg="yellow")
button1 = Button(root, text="Click !!", font=("Arial", 20, "bold"), bg="yellow", height=1, width=10, command=one).pack()


root.mainloop()
