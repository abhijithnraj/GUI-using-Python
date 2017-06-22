#The basic widget with button and label

from Tkinter import*

root=Tk()
root.title("Simple GUI")

app=Frame(root)
app.grid()

label=Label(app,text="This is the label for the switch below:")
label.grid()

button=Button(app)
button.grid()
button["text"]="Button"

