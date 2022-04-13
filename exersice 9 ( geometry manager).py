"""In this program we wil learn how to use Place Geometry Mangaer.
Place Geometry Manager allows us exact control over the widget
locations and sizes.
We can use absolute position and size for our widgets"""
"""We will create a login form for our application"""

from tkinter import *
root = Tk()

title = Label(root,text="Place Geometry Manager",
              font=(("Verdana"),15))
name_txt = Label(root,text="Name :")
pass_txt = Label(root,text="Password :")
name_input = Entry(root, width=30)
pass_input = Entry(root, width=30)

#Label = Label(root,text="Click me")
#Label.config(text="Click Me",fg="Black")

#Label.config(bg="Red") # backgrounf colour


#create button
button = Button(root,text='save')
button2 = Button(root,text='Click Me')
#use geometry mangager to show our widget
title.place(x=100, y=20) #x and y are in pixel - and that
#distance from the edges of the window
# Run your application to see the placement of the widget

#placement of other widgets
name_txt.place(x=20,y=80)
name_input.place(x=100,y=80)
pass_txt.place(x=20,y=110)
pass_input.place(x=100,y=110)

# placement of button
button.place(x=250, y=150)
button2.place(relx=0.5,rely=0.5,anchor='center')


root.geometry("450x450+650+350") #here the 650+350 means that we
#will locate our window on our screen. This means our tkinter window's
#x location is 650 and y loaction is 350

root.mainloop()
