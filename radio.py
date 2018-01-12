import tkinter
def selection():
    selection="you selected the option "+str(var.get())
    label=tkinter.Label(top,text=selection,cursor="dot",bg="blue",bd=5,font=5)
    label.pack()
top=tkinter.Tk()
var=tkinter.IntVar()
R1=tkinter.Radiobutton(top,command=selection,text="option 1",variable=var,value=1,
                       selectcolor="green",activebackground="blue",activeforeground="pink",
                       bg="pink",cursor="arrow")
R1.pack()
R2=tkinter.Radiobutton(top,command=selection,text="option 2",variable=var,value=2,
                       selectcolor="green",activebackground="blue",activeforeground="pink",
                       bg="pink",cursor="arrow")
R2.pack()
R3=tkinter.Radiobutton(top,command=selection,text="option 3",variable=var,value=3,
                       selectcolor="green",activebackground="blue",activeforeground="pink",
                       bg="pink",cursor="arrow")
R3.pack()
top.mainloop()


