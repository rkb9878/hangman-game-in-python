from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfile
from PIL import Image,ImageTk
from connectionfile import *
from shutil import copyfile
from os import path
from pathlib import Path
class addcategories:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("700x500")
        self.filename=''
        self.lb1=Label(self.root,text='Enter Category Name')
        self.tf1=Entry(self.root,width=25)
        self.lb2=Label(self.root,text='Choose Photo')
        self.bt1=Button(self.root,text='choose file',command=self.openfilechooser)
        self.bt2=Button(self.root,text='Add Category',command=self.addcategory)
        self.lb1.grid(row=0,column=1,padx=5,pady=10)
        self.tf1.grid(row=0,column=2,padx=5,pady=10)
        self.lb2.grid(row=1,column=1,padx=5,pady=10)
        self.bt1.grid(row=1,column=2,padx=5,pady=10)
        self.bt2.grid(row=2,column=2,padx=5,pady=10)
        self.root.mainloop()
    def openfilechooser(self):
        self.filename=askopenfile()
        print(self.filename.name)
        im = Image.open(self.filename.name).resize((200, 200), Image.ANTIALIAS)  # This is the correct location and spelling for my image location
        self.photo = ImageTk.PhotoImage(im)
        self.lbphoto = Label(self.root, width=200, height=200, image=self.photo)
        self.lbphoto.place(x=20, y=70)
        self.lbphoto.grid(row=1, column=3)
    def addcategory(self):
        cname=self.tf1.get()
        if cname=='':
            showinfo('','enter category name')
        elif self.filename=='':
            showinfo('','choose photo')
        else:
            conn=connectionfile.connect('')
            cr=conn.cursor()
            query1="select catname from categories where catname='"+cname+"'"
            cr.execute(query1)
            result=cr.fetchone()
            print(result)
            if result==None:
                fn=Path(self.filename.name).name
                query2="insert into categories values('"+cname+"','"+fn+"')"
                cr.execute(query2)
                conn.commit()
                p=path.realpath("categoryimages")
                p=p.replace('\\','//')+"//"+fn
                print(p)
                copyfile(self.filename.name, p)
                self.tf1.delete(0,END)
                self.filename=''
                showinfo('','category added successfully')
            else:
                showinfo('','same category already exists')
n=addcategories()

