from tkinter import *
from tkinter.ttk import Notebook,Progressbar,Combobox
import motivational
import day
import learning
import life
import positive
import strength
import winning
import failure
import times
import success
import money
import change
import funny
import learning
import work
import student
import random


class Quotes:
    def __init__(self,root):
        self.root=root
        self.root.title("Quotes")
        self.root.geometry("500x410")
        self.root.iconbitmap("logo6.ico")
        self.root.resizable(0,0)


        quotes_category=StringVar()


        def on_enter1(e):
            but_quotes['background']="black"
            but_quotes['foreground']="cyan"  
        def on_leave1(e):
            but_quotes['background']="SystemButtonFace"
            but_quotes['foreground']="SystemButtonText"\
                           

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"


#==========================================#

        def clear():
            quotes_category.set("select quotes category")
            text.delete(1.0,"end")


        def quotes():
            text.delete(1.0,"end")
            if quotes_category.get()=="Motivational":            
                ran=random.randint(0,69)
                text.insert("end",motivational.quotes[ran])
            
            if quotes_category.get()=="Day":
                ran=random.randint(0,31)                         
                text.insert("end",day.quotes[ran])


            if quotes_category.get()=="Positive":
                ran=random.randint(0,26)               
                text.insert("end",positive.quotes[ran])          


            if quotes_category.get()=="Strength":
                ran=random.randint(0,28)               
                text.insert("end",strength.quotes[ran])          


            if quotes_category.get()=="Life":
                ran=random.randint(0,30)               
                text.insert("end",life.quotes[ran])              


            if quotes_category.get()=="Winning":
                ran=random.randint(0,23)               
                text.insert("end",winning.quotes[ran])            



            if quotes_category.get()=="Failure":
                ran=random.randint(0,10)               
                text.insert("end",failure.quotes[ran])             


            if quotes_category.get()=="Time":
                ran=random.randint(0,28)               
                text.insert("end",times.quotes[ran])                


            if quotes_category.get()=="Success":
                ran=random.randint(0,19)               
                text.insert("end",success.quotes[ran])              


            if quotes_category.get()=="Money":
                ran=random.randint(0,23)               
                text.insert("end",money.quotes[ran])                  


            if quotes_category.get()=="Change":
                ran=random.randint(0,26)               
                text.insert("end",change.quotes[ran])                   

            if quotes_category.get()=="Funny":
                ran=random.randint(0,9)               
                text.insert("end",funny.quotes[ran])                 

            if quotes_category.get()=="Learning":
                ran=random.randint(0,25)               
                text.insert("end",learning.quotes[ran])                   

            if quotes_category.get()=="Student":
                ran=random.randint(0,24)               
                text.insert("end",student.quotes[ran])                      

            if quotes_category.get()=="Work":
                ran=random.randint(0,9)               
                text.insert("end",work.quotes[ran])                        

 
#=================frame===================#
        mainframe=Frame(self.root,width=500,height=410,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        topframe=Frame(mainframe,width=495,height=200,relief="ridge",bd=3)
        topframe.place(x=0,y=0)

        bottomframe=Frame(mainframe,width=495,height=205,relief="ridge",bd=3,bg="red")
        bottomframe.place(x=0,y=200)

#==============================================================================================#
        lab_select=LabelFrame(topframe,text="Daily Quotes",font=('times new roman',12,'bold'),width=490,height=194,bg="gray77")
        lab_select.place(x=0,y=0)

        list_quotes=["Motivational","Day","Positive","Strength","Life","Winning","Learning","Failure","Time","Success","Money","Change","Funny","Learning","Student","Work"]
        list_quotes_combo=Combobox(lab_select,values=list_quotes,font=('arial',12),width=25,state="readonly",textvariable=quotes_category)
        list_quotes_combo.set("select quotes category")
        list_quotes_combo.place(x=120,y=10)

        but_quotes=Button(lab_select,text="Quotes",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=quotes)
        but_quotes.place(x=40,y=100)
        but_quotes.bind("<Enter>",on_enter1)
        but_quotes.bind("<Leave>",on_leave1)

        but_clear=Button(lab_select,text="Clear",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=clear)
        but_clear.place(x=300,y=100)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)


#=============================================================================#
        scol=Scrollbar(bottomframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(bottomframe,height=10,width=58,font=('times new roman',12,'bold'),yscrollcommand=scol.set,relief="sunken",bd=3,bg="black",fg="white")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)



if __name__ == "__main__":
    root=Tk()
    app=Quotes(root)
    root.mainloop()
