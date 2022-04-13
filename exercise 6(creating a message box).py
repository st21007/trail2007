'''In this program we will create a message box'''

#from nsilib.schema import icon
from tkinter import * #import everthing from TK
from tkinter import ttk
# if we do not import we cannot use message box for our application
from tkinter import messagebox


root = Tk()


def callback2():
    #1st parameter will be title and then the text
    mbox = messagebox.askquestion("Delete","Are you Sure?",icon='warning')
    #can change icon by adding,icon='warning')
    if mbox == 'yes':
        print("Deleted")
    else:
        print("Not Deleted")


        
def callback2():
    messagebox.showinfo('Success',"Well Done!")
    print("You Clicked OK!")

button1 = ttk.Button(root,text='Delete', command=callback2).grid(
    row=0,column=8) #command will be defintion name but need function
button2 = ttk.Button(
    root,text='Info',command=callback2).grid(row=0,column=1)
#cannot run without function


root.geometry('358x250')
root.mainloop()
