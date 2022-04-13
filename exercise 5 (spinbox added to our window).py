""" in this program we will add a spinbox - which provides
a range o values to the user who can select one. it is used
where user is given some fixed values to choose from."""
#spinbox is only available in Tkinter not in the ttk module

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
        #this is where to get our gender value to show when we run the program
        print("Gender is: " + gender.get())
        print(months.get())
        print(year.get())


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
lblpass = ttk.Label(text='Your Password :')
lbltitle.grid(row=0,column=0,columnspan=2)
lblname.grid(row=1,column=0,sticky=W)
lblpass.grid(row=2,column=0)
entry.grid(row=1,column=1)
entry2.grid(row=2,column=1)
button.grid(row=3,column=1,sticky=W+E,pady=5)

#checkbox
chvar = IntVar() #check box variable
chvar.set(0) #set to 0 (zero) - means not checked

#create another variable
gender = StringVar()

#create radio button
#to get the value from our radio button - in the callback function
ttk.Radiobutton(root,text='Female',value='Female',
                var=gender).grid(row=5,column=0)
ttk.Radiobutton(root,text='male',value='Male',
                var=gender).grid(row=5,column=1)

#checkbox variable
cbox = Checkbutton(root,text='Remember Me', variable=chvar,font='Arial 16').grid(row=4,column=0,sticky=E,columnspan=2)
#in order to get it align right




"""create combobox where our first parameter will be root
and the second will be textvariable(months) and use gird geometry manager
for combobox (where it will be on the window)
when the application is run the run the combo box is empty
need to create variables for our combo box which we will
do now"""
months = StringVar() #StringVar is mt function
#combobox = ttk.combobox(root,textvariable=months,values=('('Jan','Feb','Mar','Apr')).grid(row=6,column=0)
# #tuple list of months
#ttk.combobox(root,textvariable=months,values=('('Jan','Feb','Mar','Apr')state='readonly')
# #.grid(row=6,colum=0)#tuple list of months
numbers = []
for i in range(0,10):
    numbers.append(i)

comboBox = ttk.Combobox(root,textvariable=months,
                        values=(numbers),state='readonly').grid(row=6,column=0) #tuple of values
#create spinbox - 'from' is a speical keyword for python-#
#so we need to use _after it.
year = StringVar()
Spinbox(root,from_=1990, to=2022, textvariable=year).grid(row=6,column=1)
#use grid geometry Manager to our window
#but we are able to edit the values in the spin box
#so you need to add the 'redonly' function for spinbox
#spinbox(root, from_=1990, to=2022, textvariable=years,
#state='readonly').grid(row=6,column=1
#to get the value to print out when program is run add a print statementin function block
#print(year.get())

root.geometry("500x450") # the size of the window
root.mainloop()

                     
