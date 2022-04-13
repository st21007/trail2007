#in this program we will create a list box - useful for listing items

from tkinter import *
from tkinter import ttk

root = Tk()

#below we will add single/double or mutiltuple/extended browse mode
#which lets ytou choose one or multiple items from the list

#single selection from list
listBox = Listbox(root,width=40,height=15,selectmode=MULTIPLE)
#once you run the program with single,change the mode to MUTIPLE
# # and run it again and select the items of the list
listBox.insert(0,"Python") #0,1,2,... are index numbers
listBox.insert(1,"C++")
listBox.insert(2, "C#")
listBox.insert(3, "PHP")
listBox.pack(pady=25)

root.geometry("650x650+650+200")
root.mainloop


