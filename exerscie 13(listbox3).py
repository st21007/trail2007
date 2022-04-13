#in this program we will create a list box - useful for listing items

from tkinter import *
from tkinter import ttk

root = Tk()
def  print_me():
    selected_item = listBox.curselection()
    for item in selected_item:
        print(listBox.get(item))

def delete_me():
    selected_item = listBox.curselection()
    for item in selected_item:
        listBox.delete(item)


    
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

# create buttons
button = Button(root,text='Print',command=print_me).place(x=300,y=300)
button2 = Button(root,text='Delete',command=delete_me).place(x=350, y=300)
#for these you need callback function and i want you to figure it out
#how to write this out and ensure you are able to print and also delete items from the list


root.geometry("650x650+650+200")
root.mainloop


