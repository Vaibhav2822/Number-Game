from tkinter import *
import random
import time
    
class mainfunct(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.title("Game")
        self.geometry("900x400+120+120")
        self.resizable(False,False)
       
        self.top=Frame(self,height=100,bg="white")
        self.top.pack(side=TOP,fill=X)
        self.bottom=Frame(self,height=600,bg="white")
        self.bottom.pack(side=BOTTOM,fill=X)
       
        self.label=Label(self.top,text="Choose correct number",pady=10,width=24,font="verdana 12 bold",bd=4,bg="black",fg="white")
        self.label.place(x=260,y=10)

        self.question_label=Label(self.bottom,text="Click on NEXT to get Questions",width=24,font="verdana 12 bold",bd=4,bg="black",fg="white")
        self.question_label.place(x=620,y=5)
         
        self.questions=Button(self.bottom,text="NEXT",width=15,font="veradana 11 bold",bd=2,command=self.question)
        self.questions.place(x=680,y=100)

        self.ques=Entry(self.bottom,width=30,bg="white")
        self.ques.place(x=660,y=60)

        self.score=Label(self.bottom,text="Score",padx=2,pady=2,width=15,font="veradana 11 bold",bd=2,bg="black",fg="white")
        self.score.place(x=250,y=250)

        self.your_answer=Label(self.bottom,text="Your Answer",padx=2,pady=2,width=15,font="veradana 11 bold",bd=2,bg="yellow",fg="blue")
        self.your_answer.place(x=20,y=200)

        self.entry=Entry(self.bottom,width=20,bg="black",fg="white",justify=RIGHT)
        self.entry.insert(INSERT,'0')
        self.entry.place(x=170,y=200)

        self.text=Entry(self.bottom,width=10,bd=1,bg="white",justify=RIGHT)
        self.text.insert(INSERT,'0')
        self.text.place(x=400,y=250)

        self.correct_text = Entry(self.bottom, width =15,bd=1,bg="white")
        self.correct_text.place(x=700,y=250)
        
        self.score = 0
        
        btn=[]  
        for i in range(11):
            btn.append(Button(self.bottom,text=str(i),width=10,font="arial 12 bold",bd=2,bg="green",fg="orange",command=lambda x=i:self.Number(x)))

        self.zero=Button(self.bottom,text="0",width=10,font="arial 12 bold",bd=2,bg="green",fg="orange",command=lambda x=0:self.Number(x))
        self.zero.place(x=470,y=20)

        self.delete=Button(self.bottom,text="Delete Answer",width=11,font="arial 12 bold",bd=2,bg="green",fg="orange",command=self.dele)
        self.delete.place(x=470,y=80)

        self.dot=Button(self.bottom,text=".",width=10,font="arial 12 bold",bd=2,bg="green",fg="orange",command=lambda x='.':self.Number(x))
        self.dot.place(x=470,y=140)

        self.minus=Button(self.bottom,text="-",width=10,font="arial 12 bold",bd=2,bg="green",fg="orange",command=lambda x='-':self.Number(x))
        self.minus.place(x=320,y=190)

        self.evaluate=Button(self.bottom,text="Evaluate",width=10,font="arial 12 bold",bd=2,bg="green",fg="orange",command=self.evaluate_result)
        self.evaluate.place(x=470,y=190)
         
       
        btn_index=1
        for i in range(0,3):
            for j in range(0,3):
                btn[btn_index].place(x=150*j+20,y=60*i+20)
                btn_index +=1


    def Number(self,x):
        if self.entry.get()=='0':
            al=self.entry.get()
            self.entry.delete(al)
            self.entry.insert(INSERT,str(x))
        else:
            length=len(self.entry.get())
            als=self.entry.insert(length,str(x))

           
    def dele(self):
       
        if self.entry.get()!='0':
            self.entry.delete(0,'end')
            self.entry.insert(0,'0')
        else:
            al=self.entry.get()
            self.entry.delete(al)
            self.entry.insert(INSERT,'0')        

    def question(self):
                ops=['+','-','*']
                num1=random.randint(11,100)
                num2=random.randint(11,100
                                    )
                operation=random.choice(ops)
                math=num1,operation,num2
               
                problem=self.ques.insert(INSERT,math)
               
                self.ques.delete(0,'end')
                self.ques.insert(INSERT,math)

    def evaluate_result(self):
 
            result=self.ques.get()
            res=eval(result)
            als = self.entry.get()
            al=int(als)
            self.correct_text.delete(0,'end')
            self.correct_text.insert(INSERT,res)   
            if res== al:
                self.score=self.score+1
                self.text.delete(0,'end')
                self.text.insert(INSERT,self.score)
                self.correct=Label(self.bottom,text="CORRECT",padx=2,pady=2,width=15,font="veradana 11 bold",bd=2,bg="yellow",fg="blue")
                self.correct.place(x=500,y=250)
            else:
                self.scor=self.score
                self.text.delete(0,'end')

                self.text.insert(INSERT,self.scor)
                self.wrong=Label(self.bottom,text="WRONG",padx=2,pady=2,width=15,font="veradana 11 bold",bd=2,bg="red",fg="blue")
                self.wrong.place(x=500,y=250)
                               
            self.entry.delete(0,'end')  
            self.entry.insert(INSERT,'0')
            self.ques.delete(0,'end')         

    
        
