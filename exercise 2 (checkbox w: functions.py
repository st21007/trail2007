"""Tn this program we will create a function for our button -
so that when you hit the button you can
get the values that are entered and also to check the checkbox is checked.
so you have to configure your button first."""


from tkinter import * #import everything from Tk
from tkinter import ttk

root = Tk()


def callback(): #callback function
    print("Your Name :"+entry.get())
    print("Your Password :"+entry.get())
    if chvar.get() == 1: # means the checkbox is checked
        print("Remember me selected")
    else:
        print("not selected")


# create entry boxes
entry = ttk.Entry(root,width=30) #size of the field for entry
entry2 = ttk.Entry(root,width=30)
entry.insert(0,"Please enter your name: ") # 0 is the index - first charcter
entry.insert(0,"Please enter your password: ")

#add a button to the window
# the difference in this exercise is that we are configuring our button with
button = ttk.Button(root, text='Enter')
button.config(command=callback) # with the callback function

#add label title
lbltitle = ttk.Label(text='Our Title Goes Here', font=(('Arial'),22))

lblname = ttk.Label(text='Your Name : ')
lblpass = ttk.Label(text='Ypur Password :')
lbltitle.grid(row=0,column=0,columnspan=2)
lblname.grid(row=1,column=0,sticky=W)
lblpass.grid(row=2,column=0)
entry.grid(row=1,column=1)
entry2.grid(row=2,column=1)
button.grid(row=3,column=1,sticky=W+E,pady=5)

#checkbox
chvar = IntVar() #check box variable
chvar.set(0) #set to 0 (zero) - means not checked

#checkbox variable
cbox = Checkbutton(root,text='Remember Me', variable=chvar,
                font='Arial 16').grid(row=4,column=0,sticky=E,columnspan=2)
#in order to get it align right

root.geometry("500x450") #the size of the window
root.mainloop()



 
