from tkinter import *
from newproject2 import Level

class mainfunc1(object):
    def __init__(self,master):

        self.master=master

        self.top=Frame(master,height=150,bg="white")
        self.top.pack(side=TOP,fill=X)

        self.button1=Button(self.top,text="Start",width=12,bg="black",fg="white",command=self.done)
        self.button1.place(x=200,y=50)

        self.button2=Button(self.top,text="Exit",width=12,bg="black",fg="white",command=master.destroy)
        self.button2.place(x=200,y=80)

    

    def done(self):
        new_page=Level()


    

def main():
    root=Tk()
    mai=mainfunc1(root)
    root.title("Main")
    root.geometry("500x150")
    root.resizable(False,False)
    root.mainloop()

if __name__=="__main__":
    main()
