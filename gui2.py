import tkinter
top=tkinter.Tk()
lb=tkinter.Listbox(top,selectbackground="red",selectmode="MULTIPLE",fg="white",bg="green",cursor="dot",font=20,bd=5,height=5)
lb.insert(1,"python")
lb.insert(2,"c")
lb.insert(3,"c++")
lb.insert(4,"java")
lb.insert(5,"php")
lb.pack()
