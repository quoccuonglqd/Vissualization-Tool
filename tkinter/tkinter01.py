from tkinter import *
from PIL import Image, ImageTk

cnt=0

def switch():
    x.lift()

root = Tk()
x = Label(root,text='label 1')
x.grid(row=0,column=0)
y = Label(root,text='label 2')
y.grid(row=0,column=0)
button = Button(root,text='click me',command=switch)
button.grid(row=0,column=1)
root.mainloop()