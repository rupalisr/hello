import tkinter
top=tkinter.Tk()
l1=tkinter.Label(top,text="enter your name:")
l2=tkinter.Label(top,text="password:")
e1=tkinter.Entry(top,bg="pink",fg="green")
e2=tkinter.Entry(top,bg="pink",fg="green")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0,sticky=tkinter.E)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
bt=tkinter.Button(top,text="OK",bg="red",activebackground="black",activeforeground="green"
                  ,relief=tkinter.RAISED,width=7)
bt.grid(row=2,column=1)
top.mainloop()
