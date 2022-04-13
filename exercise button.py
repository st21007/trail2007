
# In this program we will create a function for our button - so that when you hit the button
# you can get the values that are entered and also to check that checkbox is checked.
# So you have t configure your button first

from tkinter import * # imports everything from TK
from tkinter import ttk

root=Tk()

def callback():            # callback function
    print("Your Name :"+entry.get())
    print("Your Password :"+entry2.get())
    if chvar.get()==1:      # means checkbox is checked
        print("Remember me selected")
    else:
        print("not selected")

# Create entry boxes

entry = ttk.Entry(root, width=30) #size of the field for entry
entry2 = ttk.Entry(root, width=30)
entry.insert(0, "Please enter your name: ") # 0 is the index - first character
entry2.insert(0, "Please enter your password: ")

# add a button to the window
button = ttk.Button(root, text="Enter")

# add label title
lbltitle = ttk.Label(text="Our Title Goes Here", font= (("Arial"), 22))

lblname = ttk.Label(text= "Your Name : ")
lblpass = ttk.Label(text= "Your Password : ")
lbltitle.grid(row=0, column=0, columnspan=2)
lblname.grid(row=1, column=0, sticky=W)
lblpass.grid(row=2, column=0)
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, sticky=W+E, pady=5)

# checkbox
chvar = IntVar() # checkbox variable
chvar.set(0) # set to 0 (zero) - means not checked

# checkbox variable
cbox = Checkbutton(root, text="Remember Me", variable=chvar, font="Arial 16").grid(row=4, column=0)

# sticky=E, columnspan=2 # in order to get it align right

# create another variable
gender= StringVar()

# create radio button
# to get the value from our radio button - in the callback function
ttk.Radiobutton(root,text="Female",value="Female", var=gender).grid(row=5, column=0)
ttk.Radiobutton(root,text="Male",value="Male", var=gender).grid(row=5, column=1)

root.geometry("500x450") # the size of the window
root.mainloop()

"""in this program we will create a meassage box"""

# from msilib.schema import Icon
from tkinter import *
from tkinter import ttk
# if we do not import we can not use meassge box for our applictaion
from tkinter import messagebox


root = Tk()


def callback():
   #1st parmrter will be title and then the text
   mbox = messagebox.askquestion("Delete", "Are you sure?", icon="warning")
   #can change icon by adding, icon="warning")
   if mbox == "yes" :
       print("Deleted")
   else:
       print("Not deleted")


def callback2():
   messagebox.showinfo("Succes", "Well Done!")
   print("You clicked OK!")


button1 = ttk.Button(root, text="Delete", command=callback).grid(row=0, column=0)
#  command will be defintion name will but will need function
button2 = ttk.Button(
root, text="Info", command=callback2).grid(row=0, column=1)
# can not run without function


root.geometry("350x250")
root.mainloop()
# In this program we will create a message box

#from msilib.schema import Icon
from tkinter import *
from tkinter import ttk
# if we do not import we cannot use message box for our application
from tkinter import messagebox


root = Tk()


def callback():
    # 1st parameter will be title and then the tezt
    mbox = messagebox.askquestion("Delete", "Are You Sure?", icon="warning")
    # can change icon by adding, (icon='warning")
    if mbox == "yes":
        print("Deleted")
    else:
        print("Not Deleted")


def callback2():
    messagebox.showinfo('Success',"Well Done !")
    print ("You clicked OK!")

button1 = ttk.Button(root, text='Delete', command=callback).grid(row=0, column=0)

# command will be defenition name but need function

button2 = ttk.Button(root, text="Info", command=callback2).grid(row=0, column=1)

# cannot run without function



root.geometry("350x250") # the size of the window
root.mainloop()  

