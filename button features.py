import tkinter
top=tkinter.Tk()
b1=tkinter.Button(top,text="flat",relief=tkinter.FLAT)
b2=tkinter.Button(top,text="groove",relief=tkinter.GROOVE)
b3=tkinter.Button(top,text="raised",relief=tkinter.RAISED)
b4=tkinter.Button(top,text="sunken",relief=tkinter.SUNKEN)
b5=tkinter.Button(top,text="ridge",relief=tkinter.RIDGE)
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
top.mainloop()

