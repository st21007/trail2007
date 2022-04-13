"""In this program we will add radio buttons"""


from tkinter import * #import everthing from TK
from tkinter import ttk

root = Tk()

def callback():  #callback function
    print("Your Name :"+entry.get())
    print("Your Password :"+entry2.get())
    if chvar.get() ==1: #means the checkbox is checked
        print("Remember me selected")
    else:
        print("not selected")
        print(gender.get())   # this is where to get our gender value to show when we run the program


#create entry boxes
entry = ttk.Entry(root,width=30)
entry2 = ttk.Entry(root, width=30)
entry.insert(0,"Please enter your name: ") #size of the field for entry
entry2.insert(0,"Please enter your Password:")

#add a button to the window
#the differnce in this exercise is that we are configuring
button=ttk.Button(root,text='Enter')
#our button with
button.config(command=callback)  #with the callback function
     
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
cbox = Checkbutton(root,text='Remember Me', variable=chvar,font='Arial 16').grid(row=4,column=0,sticky=E,columnspan=2)
#in order to get it align right

#create another gender variable
gender= StringVar()

#create radio button
#to get the vale from our radio button - in the callback function
ttk.Radiobutton(root,text='Female',value='Female',var=gender).grid(row=5,column=0)
ttk.Radiobutton(root,text='Male',value='Male',var=gender).grid(row=5,column=1)

root.geometry("500x450")  # the size of the window
root.mainloop()
