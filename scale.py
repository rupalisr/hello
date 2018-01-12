import tkinter
def sel():
    selection="value="+str(var.get())
    label=tkinter.Label(top,text=selection)
    label.pack()
top=tkinter.Tk()
var=tkinter.IntVar()
scale=tkinter.Scale(top,variable=var,activebackground="blue",bg="white",
                    fg="pink",orient=tkinter.VERTICAL,troughcolor="yellow",cursor=
                    "arrow",length=170)
scale.set(270)
scale.pack_configure()
button=tkinter.Button(top,text="Get scale value",command=sel,activebackground="pink",activeforeground="green",bg="blue",bd=5,width=20)
button.pack()
top.mainloop()





















+
