from Tkinter import*

class Application(Frame):
	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widget()
		self.fact=1

	def create_widget(self):
		self.label=Label(self,text="Enter the number you want to find factorial for:")
		self.label.grid(row=0,column=0,sticky=W)

		self.n=Entry(self)
		self.n.grid(row=1,column=0,sticky=W)

		self.button1=Button(self,text="Find",command=self.factorial)
		self.button1.grid(row=1,column=1,sticky=W)
		
		self.text=Text(width=40,height=20,wrap=WORD)
		self.text.grid(row=3,column=0,sticky=W)
		
	def factorial(self):
		self.fact=1
		p=int(self.n.get())
		for i in range(1,p+1):
			self.fact=self.fact*i
		self.display()
		
			
	def display(self):
		self.text.delete(0.0,END)
		self.text.insert(0.0,"The facorial of "+str(self.n.get())+ " is "+str(self.fact))


root=Tk()
root.title("Factorial of a Number")
root.geometry("500x500")

app=Application(root)

root.mainloop()	

		
				
	


