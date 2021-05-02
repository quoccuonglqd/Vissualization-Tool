from __future__ import absolute_import
from tkinter import *
import os
from PIL import ImageTk,Image
from Component import Component
from Titlebar import Titlebar
from Modebar import Modebar
from Image_executer import Image_executer 
from algorithms.algorithm import Algorithm

class NewRoot(Tk):    
    def __init__(self):
        Tk.__init__(self)
        self.attributes('-alpha', 0.0)

class MyMain(Toplevel):
    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.overrideredirect(1)

    def on_close(self):
        self.master.destroy()
        self.destroy()

class Application(object):
	HEIGHT = 600
	WIDTH = 800

	def __init__(self,master):
		self.master = master
		self.titlebar = Titlebar(self.master)
		self.modeoptionbar = Modebar(self.master)
		self.image_executer = Image_executer(self.master)
		self.bt = Button(self.master,command=self.Transform,text='gray scale')
		self.bt.grid(row=2,column=0)

	def Run(self):
		window_height = Application.HEIGHT
		window_width = Application.WIDTH
		screen_width = self.master.winfo_screenwidth()
		screen_height = self.master.winfo_screenheight()
		x_cordinate = int((screen_width/2) - (window_width/2))
		y_cordinate = int((screen_height/2) - (window_height/2))
		self.master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
		self.master.mainloop()

	def Close(self):
		self.master.on_close()

	def Transform(self):
		t = Algorithm()
		img = t.Color_space_convert(img=self.image_executer.pq[self.image_executer.it][0], src_cs = 'RGB', dst_cs = 'GRAY')
		self.image_executer.Transform(self.image_executer.pq[self.image_executer.it][0],img,'Gray scale')

rootofroot = NewRoot()
root = MyMain(rootofroot)
a = Application(root)
a.Run()
