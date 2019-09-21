from tkinter.ttk import *
from tkinter import *
from tkinter.messagebox import *
from connectionfile import *
class addquestions:
    def addquestion(self):
        if self.tbquestion.get("1.0",END)=="":
            showinfo("","Enter  question")
        elif self.tbanswer.get()=="":
            showinfo("","Enter  answer")
        elif self.cbcatname.get()=="" :
            showinfo("","Choose  Category")
        else:
            conn=connectionfile.connect('')
            cr=conn.cursor()
            s="insert into questions values(NULL ,'"+self.tbquestion.get("1.0",END)+"','"+self.tbanswer.get()+"','"+self.cbcatname.get()+"')"
            cr.execute(s)
            conn.commit()
            showinfo("","Question Added Sucessfully")
            self.tbquestion.delete("1.0",END)
            self.tbanswer.delete(0,END)
            self.cbcatname.current(0)
            self.cbcatname.set('')
    def __init__(self):
        self.root=Tk()
        self.root.geometry("800x400")
        self.lb1 = Label(self.root, text="Enter Question")
        self.lb2 = Label(self.root, text="Enter Answer")
        self.lb5 = Label(self.root, text="Choose  Category*")
        self.bt1=Button(self.root,text="Add Question",command=self.addquestion,bg="blue")
        self.tbquestion=Text(self.root,width=25,height=10)
        self.tbanswer = Entry(self.root, width=25)
        self.cbcatname = Combobox(self.root)
        conn = connectionfile.connect('')
        cr = conn.cursor()
        s = "select * from categories"
        cr.execute(s)
        p = cr.fetchall()
        dbvalues=[]
        for row in p:
            dbvalues.append(row[0])
        self.cbcatname['values']=dbvalues
        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=1, column=0)
        self.tbquestion.grid(row=0,column=1,padx=10,pady=10)
        self.tbanswer.grid(row=1, column=1, padx=10, pady=10)
        self.lb5.grid(row=2, column=0)
        self.cbcatname.grid(row=2,column=1,padx=10,pady=30)
        self.bt1.grid(row=3,column=1)
        self.root.mainloop()
x=addquestions()
