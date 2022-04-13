from tkinter import *
root = Tk()


root.title("Frames")

#create frame using frame construtor method
# to make frame visible - use background colour (bg)
frame = Frame(root,height=300,width=300,bg='red')
frame.pack() # using geometry manager for frame

root.geometry('650x650+450+200')
root.mainloop()
