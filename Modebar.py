r"""Date: 12/3/2020
    Author: Nguyen Quoc Cuong
"""
from tkinter import *
import os
from PIL import ImageTk,Image
from Component import Component

class Modebar(Component):
	r"""A Modebar class for displaying modebar

    Args:
        master(tkinter.Tk): reference to the window
    """
	MODEBAR_WIDTH = 90
	ROW1 = 0
	ROW2 = 1
	FIRSTBUTTON_WIDTH = 55
	FIRSTBUTTON_COLUMN = 0
	SECONDBUTTON_WIDTH = 55
	SECONDBUTTON_COLUMN = 1
	THIRDBUTTON_WIDTH = 112
	THIRDBUTTON_COLUMN = 0
	def __init__(self,master):
		super(Modebar, self).__init__(master,width=Modebar.MODEBAR_WIDTH)
		self.firstbutton = Button(self,text='Video',width=Modebar.FIRSTBUTTON_WIDTH)
		self.firstbutton.grid(row=Modebar.ROW1,column=Modebar.FIRSTBUTTON_COLUMN)
		self.firstbutton.bind('<Button-1>',self.Reset_mode)
		self.secondbutton = Button(self,text='Stream',width=Modebar.SECONDBUTTON_WIDTH)
		self.secondbutton.grid(row=Modebar.ROW1,column=Modebar.SECONDBUTTON_COLUMN)
		self.secondbutton.bind('<Button-1>',self.Reset_mode)
		self.thirdbutton = Button(self,text='Image',width=Modebar.THIRDBUTTON_WIDTH)
		self.thirdbutton.grid(row=Modebar.ROW2,column=Modebar.THIRDBUTTON_COLUMN,columnspan=2)
		self.thirdbutton.bind('<Button-1>',self.Reset_mode)
		self.grid(row=1,column=0,columnspan=2)

	def Reset_mode(self,event):
		r"""
			Reset order of 3 button "Video","Stream" and "Image"
        """
		str = event.widget.cget("text")
		if str=="Image":
			self.firstbutton.configure(text="Video")
			self.secondbutton.configure(text="Stream")
			self.thirdbutton.configure(text="Image")
			return
		if str=="Video":
			self.firstbutton.configure(text="Image")
			self.secondbutton.configure(text="Stream")
			self.thirdbutton.configure(text="Video")
			return
		if str=="Stream":
			self.firstbutton.configure(text="Image")
			self.secondbutton.configure(text="Video")
			self.thirdbutton.configure(text="Stream")
			return
