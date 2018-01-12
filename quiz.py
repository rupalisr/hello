import tkinter
import tkinter.messagebox
question=[
    "The national language of india is",
    "The national flower of india is",
    "the pink city is",
    "the national bird of india is",
    "(a+b)^2"
    ]
options=[
    ["english","hindi","telgu","japenese"],
    ["lilly","rose","sunflower","lotus"],
    ["jaipur","patna","kashmir","bengal"],
    ["cock","parrot","peacock","piegon"],
    ["a^2-b^2","a^2+b^2+2*a*b","(a*b)(a*b)","aaaaa"],
]
answer=[2,4,1,3,2]
class quiz:
    def __init__(self,top):
        self.label=tkinter.Label(top,text="GENERAL KNOWLEDEGE",bg="pink",bd=5)
        self.label.pack(side=tkinter.TOP)
        self.la=tkinter.Label(top,text=" ")
        self.la.pack(side=tkinter.TOP)
        self.opt_selected=tkinter.IntVar()
        self.qn=0
        self.correct=0
        self.ques=self.create_q(top,self.qn)
        self.opts=self.create_options(top,4)
        self.display_q(self.qn)
        self.status_bar=self.create_status_bar(top)
        self.create_but(top)
    def create_status_bar(self,top):
        status_bar=tkinter.Label(top,text="click to get answer",bd=1,relief=tkinter.RAISED,anchor='w')
        status_bar.pack(side=tkinter.BOTTOM,fill="x")
        return status_bar
        
    def create_but(self,top):
         button=tkinter.Button(top,text="Back",command=self.back_btn,activebackground="pink"
                                   ,activeforeground="white",bg="yellow",fg="black",width=10)
         button.pack(side=tkinter.BOTTOM)
         button=tkinter.Button(top,text="next",command=self.next_btn,activebackground="pink"
                                   ,activeforeground="white",bg="yellow",fg="black",width=10)
         button.pack(side=tkinter.BOTTOM)
        
    def create_q(self,top,qn):
        w=tkinter.Label(top,text=question[qn],bg="green",cursor="circle")
        w.pack()
        return w
    def create_options(self,top,n):
        b_val=0
        b=[]
        while b_val<n:
            btn=tkinter.Radiobutton(top,text="foo",variable=self.opt_selected,
                                    value=b_val+1)
            b.append(btn)
            btn.pack(side=tkinter.TOP,anchor="w")
            b_val=b_val+1
        return b    
    def display_q(self,qn):
        b_val=0
        self.opt_selected.set(0)
        self.ques["text"]=question[qn]
        for op in options[qn]:
            self.opts[b_val]["text"]=op
            b_val=b_val+1
    def check_q(self,qn):
        if self.opt_selected.get()==answer[qn]:
            return True
        return False
    
    def print_results(self):
        result="Score: "+str(self.correct)+"/"+str(len(question))
        tkinter.messagebox.showinfo("Final result:",result)
    def back_btn(self):
        print("go back")   
    def next_btn(self):
        if self.check_q(self.qn):
            self.status_bar["text"]="Correct"
            self.correct=self.correct+1
        else:
           self.status_bar["text"]="wrong"
        self.qn=self.qn+1
        if self.qn>=len(question):
            self.print_results()
        else:
            self.display_q(self.qn)
        
top=tkinter.Tk()
app=quiz(top)
top.mainloop()
            
