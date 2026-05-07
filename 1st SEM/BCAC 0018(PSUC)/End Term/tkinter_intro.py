from tkinter import *

gui = Tk()
# Set window size
gui.geometry("500x1000")

#Button
#button1=Button(gui,text='Stop',command=gui.destroy)
#button1.pack() 

#CheckButton

c_button1=Checkbutton(gui,text='Male')
c_button2=Checkbutton(gui,text='Female')
c_button1.pack()
c_button2.pack()

#Canvas

canvas1=Canvas(gui,width=40,height=60,bd=20,bg='red')
canvas1.pack()

#Entry

e1=Entry(gui)
e2=Entry(gui)
e1.pack()
e2.pack()

#Frame

frame=Frame(gui)
frame.pack()

redbutton = Button(frame, text = 'Red', fg ='red')
redbutton.pack( side = LEFT)
greenbutton = Button(frame, text = 'Brown', fg='brown')
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text ='Blue', fg ='blue')
bluebutton.pack( side = LEFT )


#Label

label1=Label(gui,text="This is label")
label1.pack()

#Listbox

LB=Listbox(gui)
LB.insert(1,'Python')
LB.insert(2,'Java')
LB.insert(1,'C++')
LB.insert(1,'Web Technology')
LB.pack()

#MenuButton

mb = Menubutton(gui, text = "Language", relief = FLAT)   
mb.menu = Menu(mb)  
mb["menu"]=mb.menu  
mb.menu.add_checkbutton(label = "Hindi", variable=IntVar())  
mb.menu.add_checkbutton(label = "English", variable = IntVar())  
mb.pack()  

#Message

ourMessage="This is our text"
msgVar=Message(gui,text=ourMessage,bg='lightgreen')
msgVar.pack()

#RadioButton

rb1=Radiobutton(gui,text="Male",value=1)
rb2=Radiobutton(gui,text="Female",value=2)
rb1.pack()
rb2.pack()

#Scale

sc=Scale(gui,from_=0,to=42)
sc.pack()
sc1=Scale(gui,from_=0,to=200,orient=HORIZONTAL)
sc1.pack()

#Scrollbar

scbar=Scrollbar(gui)

mylist = Listbox(gui, yscrollcommand=scbar.set )
for i in range(100):
   mylist.insert(END, 'This is line number' + str(i))
mylist.pack( side = LEFT, fill = BOTH )
scbar.config(command = mylist.yview )
scbar.pack(side=RIGHT,fill=Y)

#Text

txt=Text(gui,height=2,width=20)
txt.pack()
#txt.insert(END,'This is text field')

#TopLevel

top=Toplevel(height=100,width=200,bg='yellow')
top.title("Python")

#SpinBox

spbox=Spinbox(gui,from_=0,to=10)
spbox.pack()


gui.mainloop()