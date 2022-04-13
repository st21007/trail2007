#in this program we will create a list box - useful for listing items

from tkinter import *
from tkinter import ttk

root = Tk()
listBox = Listbox(root,width=40,height=15) #variable called listbox
listBox.insert(0,"Python") #0,1,2,... are index numbers
listBox.insert(1,"C++")
listBox.insert(2, "C#")
listBox.insert(3, "PHP")
listBox.pack(pady=25)

root.geometry("650x650+650+200")
root.mainloop


