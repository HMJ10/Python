import tkinter
from tkinter import *
import wikipedia

window = Tk()
window.title("Personal WIKIPEDIA")
window.config(bg="light blue")
f1_heading = Frame(window)
f2_frame = Frame(window)
f3_result = Frame(window)

Label(f1_heading, text="Personal WIKIPEDIA", font=("times", 30, "bold"), bg="lightgreen", pady=15, padx=5).pack(side=TOP)

Label(f2_frame, text="Search Here", font=("Arial", 20, "bold"), bg="yellow").pack(side=LEFT)

Label(f3_result, text="Searched Results:", font=("Arial", 25, "bold"), bg="light pink").pack(side=LEFT)

entry_box = Entry(f2_frame, width=40, font=("Arial", 20, "bold"))
entry_box.pack(side=LEFT, fill=BOTH, expand=5)
entry_box.focus_set()

query = ""
text = Text(window, font=("Arial", 17), bg="lightblue", padx=55, pady=10)


def text_search():
    global query
    query = entry_box.get()
    try:
        txt_summary = wikipedia.summary(query)
        text.insert('1.0', txt_summary)
    except:
        text.insert('1.0', "NO RESULTS FOUND")


button1 = Button(f2_frame, text="SEARCH", font=("Arial", 15, "bold"), bg="red", command=text_search)
button1.pack(side=RIGHT)

f1_heading.pack()
f2_frame.pack(side=TOP)
f3_result.pack(side=TOP, pady=20, padx=50)
text.pack()

window.mainloop()
