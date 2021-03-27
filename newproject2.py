from tkinter import *
from newproject import mainfunc
from newproject3 import mainfunct
from newproject4 import mainfunction

class Level(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("250x250")
        self.resizable(False,False)        

        button1=Button(self,text="Easy",width=12,bg="black",fg="white",command=self.easy)
        button1.place(x=80,y=80)

        button2=Button(self,text="Medium",width=12,bg="black",fg="white",command=self.medium)
        button2.place(x=80,y=110)

        button3=Button(self,text="Hard",width=12,bg="black",fg="white",command=self.hard)
        button3.place(x=80,y=140)

    def easy(self):
        easy=mainfunc()
 
    def medium(self):
        medium=mainfunct()

    def hard(self):
        hard=mainfunction()
