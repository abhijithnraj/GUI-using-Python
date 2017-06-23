from Tkinter import *

class Application(Frame):
	def __init__(self,master):
		
		Frame.__init__(self,master)
		
		self.grid()
		self.create_widget()
		self.counter=0

	def create_widget(self):
		
		self.button1=Button(self,text="+",command=self.increment)
		self.button1.grid(row=0,column=0,sticky=W)

		self.text=Text(self,width=20,height=10,wrap=WORD)
		self.text.grid(row=0,column=1,sticky=W)
		
		self.button2=Button(self,text="-",command=self.decrement)
		self.button2.grid(row=0,column=2,sticky=W)

	def increment(self):
		
		self.counter+=1
		self.display()

	def decrement(self):
			
		self.counter-=1
		self.display()

	def display(self):
		self.text.delete(0.0,END)
		self.text.insert(0.0,self.counter)


root=Tk()
root.title("GUI")
root.geometry("1000x1000")

app=Application(root)

root.mainloop()

