r"""Date: 12/3/2020
    Author: Nguyen Quoc Cuong
"""
from tkinter import * 
import os.path as osp
from PIL import ImageTk,Image
from Component import Component
import cv2 as cv
from tkinter import filedialog
import os.path


class Image_executer(Component):
	r"""A Titlebar class for image executor area 

    Args:
        master(tkinter.Tk): reference to the window
    """

	IMAGE_PATH = 'image/icon-image-512.png'
	PREVIOUS_PATH = 'image/previos_arrow.png'
	NEXT_PATH = 'image/next_arrow.jpg'
	SETTING_PATH = 'image/settings.png'
	PADY = (15,15)
	PADX = (5,5)
	BUTTON_PADY = 165
	HEIGHT = 600
	WIDTH = 200
	IMAGE_SIZE = (460,380)
	MAX_ELEMENT = 40
	BG = '#fcba03'

	def __init__(self,master):
		super(Image_executer, self).__init__(master,height=Image_executer.HEIGHT,width=Image_executer.WIDTH,bg =Image_executer.BG)
		self.it = -1
		self.pq = []
		self.is_enabled = True
		self.firstbutton_img = ImageTk.PhotoImage(Image.open(osp.join(osp.dirname(osp.abspath(__file__)),
			Image_executer.PREVIOUS_PATH)))
		self.firstbutton = Button(self,image=self.firstbutton_img,state='disabled',command=self.Return_back)
		self.firstbutton.grid(row=0,column=0,pady=Image_executer.BUTTON_PADY,sticky=N)

		self.original = Image.open(Image_executer.IMAGE_PATH)
		self.image = ImageTk.PhotoImage(self.original.resize(Image_executer.IMAGE_SIZE,Image.ANTIALIAS))
		self.display = Canvas(self, bd=0, highlightthickness=0,width=Image_executer.IMAGE_SIZE[0])
		self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")
		self.display.grid(row=0,column=1,pady=Image_executer.PADY, sticky=N+S)

		self.secondbutton_img = ImageTk.PhotoImage(Image.open(osp.join(osp.dirname(osp.abspath(__file__)),
			Image_executer.NEXT_PATH)))
		self.secondbutton = Button(self,image=self.secondbutton_img,state='disabled',command=self.Come_next)
		self.secondbutton.grid(row=0,column = 2,pady=Image_executer.BUTTON_PADY,sticky=N)

		self.optionframe = Component(self,bg = Image_executer.BG)

		self.seventhbutton_img = ImageTk.PhotoImage(Image.open(osp.join(osp.dirname(osp.abspath(__file__)),
			Image_executer.SETTING_PATH)))
		self.seventhbutton = Button(self,image=self.seventhbutton_img,command=self.Switch)
		self.seventhbutton.grid(row=1,column=0,padx=Image_executer.PADX,sticky=N)

		self.thirdbutton = Button(self.optionframe,text='Load an image',width=12,command=self.Load)
		self.thirdbutton.grid(row=0,column = 1,padx=Image_executer.PADX)

		self.fourthbutton = Button(self.optionframe,text='Capture',width=12,command=self.Capture)
		self.fourthbutton.grid(row=0,column = 2,padx=Image_executer.PADX)

		self.eighthbutton = Button(self.optionframe,text='Save',width=12,state='disabled',command=self.Save)
		self.eighthbutton.grid(row=0,column = 3,padx=Image_executer.PADX)

		self.fifthbutton = Button(self.optionframe,text='Delete',width=12,state='disabled',command=self.Remove_from_queue)
		self.fifthbutton.grid(row=0,column = 4,padx=Image_executer.PADX)

		self.sixthbutton = Button(self.optionframe,text='Visualize',width=12,state='disabled',command=self.Visualize)
		self.sixthbutton.grid(row=0,column = 5,padx=Image_executer.PADX)

		self.optionframe.grid(row=1,column=1,columnspan=2,sticky=W)
		self.empty_frame = Component(self,bg = Image_executer.BG,width=515,height=40)
		self.empty_frame.grid(row=1,column=1,columnspan=2,sticky=W)
		self.empty_frame.Disable()

		self.grid(row=2,column=1,columnspan=2,sticky=W)

	def Switch(self):
		if self.is_enabled==True:
			self.empty_frame.Enable()
			self.is_enabled=False
		else:
			self.optionframe.Enable()
			self.Reset_state()
			self.is_enabled=True

	def Reset_state(self):
		r"""
            Reset state of the button
        """
		if len(self.pq) >= 2:
			self.firstbutton.configure(state='normal')
			self.secondbutton.configure(state='normal')
		else:
			self.firstbutton.configure(state='disabled')
			self.secondbutton.configure(state='disabled')

		if len(self.pq) > 0:
			self.fifthbutton.configure(state='normal')
			self.eighthbutton.configure(state='normal')
		else:
			self.fifthbutton.configure(state='disabled')
			self.eighthbutton.configure(state='disabled')

		if len(self.pq) > 0 and self.pq[self.it][1]==True:
			self.sixthbutton.configure(state='normal')
		else:
			self.sixthbutton.configure(state='disabled')

	def Change_image(self,image):
		r"""
            Args:
                image(numpy array): image to display next
            Display another image in the image executor area
        """
		image = Image.fromarray(image)
		#convert to image object
		self.image = ImageTk.PhotoImage(image.resize(Image_executer.IMAGE_SIZE,Image.ANTIALIAS))
		#resize and convert to ImageTk which can be displayed
		self.display.delete("IMG")
		#remove the old image
		self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")

	def Add_to_queue(self,element):
		r"""
            Args:
                element(tuple): (image,False) if this image element is loaded or captured
                				(image,True,original_image,effect) if this image is tranformed from original image by effect
            Return image array after being converted
            Example:
        """
		self.pq.append(element)
		if len(self.pq) > Image_executer.MAX_ELEMENT:
			del self.pq[0]
		#delete the first element of the queue if its length grows over limit
		self.it = len(self.pq)-1
		self.Reset_state()

	def Remove_from_queue(self):
		r"""
            Delete an element from the queue
        """
		del self.pq[self.it]
		if len(self.pq)==0:
			self.it = -1
			self.Change_image(cv.imread(Image_executer.IMAGE_PATH))
			self.Reset_state()
			return 
		else:
			if self.it >= len(self.pq):
			    self.it = len(self.pq) - 1
			self.Change_image(self.pq[self.it][0])
			self.Reset_state()

	def Transform(self,original_img,img,effect):
		self.Change_image(img)
		self.Add_to_queue((img,True,original_img,effect))
		self.Reset_state()

	def Return_back(self):
		r"""
            Display previos image in the queue 
        """
		if self.it == 0:
			self.it = len(self.pq)-1
		else:
			self.it = self.it - 1
		self.Change_image(self.pq[self.it][0])
		self.Reset_state()

	def Come_next(self):
		r"""
            Display next image in the queue
        """
		if self.it == len(self.pq)-1:
			self.it = 0
		else:
			self.it = self.it + 1
		self.Change_image(self.pq[self.it][0])
		self.Reset_state()

	def Load(self):
		r"""
            Load an image from local directory 
        """
		self.path = filedialog.askopenfilename(initialdir = os.path.dirname(os.path.abspath(__file__)),title = "Select file",
			                                    filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
		if len(self.path) == 0:
			return
		img = cv.cvtColor(cv.imread(self.path),cv.COLOR_BGR2RGB)
		self.Change_image(img)
		self.Add_to_queue((img,False))

	def Capture(self):
		r"""
            Capture an image and display
        """
		cam = cv.VideoCapture(0, cv.CAP_DSHOW)
		cv.namedWindow('Capturing')
		while True:
			ret,frame = cam.read()
			cv.imshow('Capturing',frame)
			if not ret:
				break
			key = cv.waitKey(1)
			if key%256 ==27:
				print("Escape hit, closing...")
				break
			#Escape if hit Esc 
			elif key%256 == 32:
				frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
				self.Change_image(frame)
				self.Add_to_queue((frame,False))
				break
			#Capture if hit Space
		cam.release()
		cv.destroyAllWindows()

	def Visualize(self):
		r"""
            Visualize image and its original image
        """
		self.showing_windows = Toplevel()
		self.display_img2 = ImageTk.PhotoImage(Image.fromarray(self.pq[self.it][0]).resize(Image_executer.IMAGE_SIZE,Image.ANTIALIAS))
		self.display_img1 = ImageTk.PhotoImage(Image.fromarray(self.pq[self.it][2]).resize(Image_executer.IMAGE_SIZE,Image.ANTIALIAS))
		label1 = Label(self.showing_windows,image=self.display_img1)
		label2 = Label(self.showing_windows,image=self.display_img2)
		label3 = Label(self.showing_windows,text=self.pq[self.it][3])
		label1.grid(row=0,column=0)
		label2.grid(row=0,column=1)
		label3.grid(row=1,column=0,columnspan=2)

	def Save(self):
		r"""
			Save the current displayed image
		"""
		self.savepath = filedialog.asksaveasfilename(initialdir = os.path.dirname(os.path.abspath(__file__)),title = "Save as",
			                filetypes = (("PNG files","*.png"),("jpeg files","*.jpg"),("all files","*.*")))
		cv.imwrite(self.savepath,cv.cvtColor(self.pq[self.it][0],cv.COLOR_BGR2RGB))