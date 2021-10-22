from tkinter import *
from tkinter import ttk
window = Tk()
window.title("WELCOME TO REGISTERATION FORM")
window.geometry('800x800')
window.configure(background = "light blue");

a = Label(window ,text = "First Name").grid(row = 0,column = 0)
b = Label(window ,text = "Last Name").grid(row = 1,column = 0)
c = Label(window ,text = "Date of Birth").grid(row = 2,column = 0)
d = Label(window ,text = "Email Id").grid(row = 3,column = 0)
e = Label(window ,text = "Password").grid(row = 4,column = 0)
f = Label(window ,text = "Address").grid(row = 5,column = 0)
g = Label(window ,text = "Contact Number").grid(row = 6,column = 0)

a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1)
e1 = Entry(window).grid(row = 4,column = 1)
f1 = Entry(window).grid(row = 5,column = 1)
g1 = Entry(window).grid(row = 6,column = 1)

def clicked():
   res = "Welcome to " + txt.get()
   lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=7,column=0)
btn = ttk.Button(window ,text="return").grid(row=7,column=1)
window.mainloop()