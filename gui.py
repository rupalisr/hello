from tkinter import*
import tkinter
top=tkinter.Tk()
checkbox1=IntVar()
checkbox2=IntVar()
c1=Checkbutton(top,text="Music",variable=checkbox1,offvalue=0,onvalue=1,
               height=5,width=20,bg="green",cursor="dot",bd=20,font=30,fg="yellow",highlightcolor="cyan",
               selectcolor="blue",activebackground="orange",activeforeground="black")
c2=Checkbutton(top,text="video",variable=checkbox2,offvalue=0,onvalue=1,
               height=5,width=20,activebackground="orange",activeforeground="black",
               bg="green",cursor="dot",bd=20,font=30,fg="yellow",highlightcolor="cyan",
               selectcolor="blue")
c1.pack()
c2.pack()
