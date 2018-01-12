import tkinter
top=tkinter.Tk()
scroll=tkinter.Scrollbar(top,activebackground="blue",bg="pink",bd=5,
                         cursor="arrow",elementborderwidth=6)
scroll.pack(side='right',fill='y')
mylist=tkinter.Listbox(top,yscrollcommand=scroll.set,
                       bg="yellow",fg="black")
for i in range(1,101):
    mylist.insert(tkinter.END,"this is line number "+str(i))
mylist.pack(side='left',fill='both')
scroll.config(command=mylist.yview)
mylist.mainloop()
