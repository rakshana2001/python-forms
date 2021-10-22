from tkinter import *
from tkinter import ttk
window = Tk()
window.title("FORM PAGE")
window.geometry('700x700')
window.configure(background = "Light Blue")
ttk.Button(window, text="Hai, Rakshana").grid()
ttk.Button(window, text="Welcome to our Form Page").grid()
window.mainloop()