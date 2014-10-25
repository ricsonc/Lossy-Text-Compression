import scipy.fftpack as sfft
import Tkinter
from Tkinter import *

def convert(text):
	return sfft.dct([float(ord(char)) for char in text], norm='ortho')

def uconvert(nums):
	return [chr(int(round(num))%256) for num in sfft.idct(nums, norm='ortho')]

def nround(x, prec):
	prec = float(prec)+1e-100
	if x >= 0:
		corr = .5
	else:
		corr = -.5
	return int(x/prec+corr)*prec

def codeblock(text, cmatrix):
	uc = convert(text)
	uc = [nround(uc[x],cmatrix[x]) for x in xrange(len(uc))]
	return ''.join(uconvert(uc))

def codeall(text,cmatrix, bsiz = 8):
	ntext = []
	for x in xrange(0,len(text),bsiz):
		ntext.append(codeblock(text[x:x+bsiz],cmatrix))
	return ''.join(ntext)

class Window(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, background = "grey")
		self.parent = parent
		#
		self.parent.title("lossy text compression sim")
		self.pack(fill=BOTH, expand = 1)
		#
		self.inptextlab = "'hello world. this is a lossy text compression simulator' #input the string here w/ quotes"
		self.bsizlab ="8 #pick the length of the coefficient matrix."
		self.cmatrixlab ="[1.5,1.3,1.2,1.1,1.1,1.0,1.0,1.0] #this is the coefficient vector."
		#
		self.inptext = Entry(self, bg = 'white', width=200)
		self.inptext.grid(column = 0, row = 1)
		self.inptext.insert(0,self.inptextlab)
		self.cmatrix = Entry(self, bg = 'white', width=200)
		self.cmatrix.grid(column = 0, row = 2)
		self.cmatrix.insert(0,self.cmatrixlab)
		self.bsiz = Entry(self, bg = 'white', width=200)
		self.bsiz.grid(column = 0, row = 3)
		self.bsiz.insert(0,self.bsizlab)
		self.ouptext = Entry(self, bg = 'white', width=200)
		self.ouptext.grid(column = 0, row = 4)
		#
		self.pack()
	def loop(self):
		error = False
		try:
			exec("inptext =" +self.inptext.get())
			exec("cmatrix =" + self.cmatrix.get())
			exec("bsiz =" + self.bsiz.get())
		except:
			error = True
		if not error and bsiz <= len(cmatrix):
			self.ouptext.delete(0,END)
			self.ouptext.insert(0,codeall(inptext, cmatrix, bsiz))
		self.after(10,self.loop)
		
root = Tk() 
g = Window(root)
root.after(10,g.loop)
root.mainloop()