import tkinter
def clicked():
    bt=tkinter.Toplevel(top)
    button=tkinter.Button(bt,text="do nothing with this button",activebackground="orange",activeforeground="pink",width=20,bg="yellow",height=10)
    button.pack() 

top=tkinter.Tk()    
m=tkinter.Menu(top)
top.config(menu=m)
submenu_file=tkinter.Menu(m,tearoff=0)
m.add_cascade(label="File",menu=submenu_file)
submenu_file.add_command(label="New",command=clicked)
submenu_file.add_command(label="Open",command=clicked)
submenu_file.add_command(label="Save",command=clicked)
submenu_file.add_command(label="Save as..",command=clicked)
submenu_file.add_command(label="Close",command=clicked)
submenu_file.add_separator()
submenu_file.add_command(label="Exit",command=top.quit)
submenu_edit=tkinter.Menu(m,tearoff=0)
m.add_cascade(label="Edit",menu=submenu_edit)
submenu_edit.add_command(label="Cut",command=clicked)
submenu_edit.add_command(label="Copy",command=clicked)
submenu_edit.add_command(label="Paste",command=clicked)
submenu_edit.add_separator()
submenu_edit.add_command(label="Delete",command=clicked)
submenu_edit.add_command(label="Select All",command=clicked)
submenu_help=tkinter.Menu(m,tearoff=0)
m.add_cascade(label="Help",menu=submenu_help)
submenu_help.add_command(label="Help Index",command=clicked)
submenu_help.add_command(label="About",command=clicked)
submenu_help.add_separator()
submenu_help.add_command(label="Help",command=clicked)
top.mainloop()





