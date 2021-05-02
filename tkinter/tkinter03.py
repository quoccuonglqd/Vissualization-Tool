from tkinter import *

class Popup_frame(Frame):
	def __init__(self,master):
		super.__init__(master)
		canvas = Canvas(masterbd=0, highlightthickness=0)
		canvas.grid(row=0, column=0)
		self.window = Frame(canvas)
		interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=tk.NW)
		def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)
        
