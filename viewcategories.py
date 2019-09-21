from tkinter import *
from PIL import Image,ImageTk
from connectionfile import *
from gamefile import *
class viewcategories():
    def abc(self,event,obj):
        self.root.destroy()
        gamefile(obj)
    def __init__(self):
        self.root = Tk()
        self.root.title('CHOOSE GAME CATEGORY')
        self.frame = Frame(self.root, width=800, height=500)
        self.frame.grid(row=0, column=0)
        self.canvas = Canvas(self.frame, bg='#FFFFFF', width=800, height=500, scrollregion=(0, 0, 1200, 1200))
        self.hbar = Scrollbar(self.frame, orient=HORIZONTAL)
        self.hbar.pack(side=BOTTOM, fill=X)
        self.hbar.config(command=self.canvas.xview)
        self.vbar = Scrollbar(self.frame, orient=VERTICAL)
        self.vbar.pack(side=RIGHT, fill=Y)
        self.vbar.config(command=self.canvas.yview)
        self.canvas.config(width=800, height=500)
        self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)
        self.canvas.config(background="#FFA500")
        m=20
        n=70
        conn=connectionfile.connect('')
        cr=conn.cursor()
        query='select * from categories'
        cr.execute(query)
        result=cr.fetchall()
        i=0
        l=[]
        c=[]
        for row in result:
            self.a=str("im")+str(i)
            self.a = Image.open("categoryimages/"+row[1]).resize((200, 200),Image.ANTIALIAS)
            self.v="photo"+str(i)
            self.v = ImageTk.PhotoImage(self.a)
            l.append(self.v)
            c.append(row[0])
        x=[]
        for j in range(0,len(l)):
            x.append("self."+str(c[j]))
        for j in range(0,len(x)):
            self.cn = str("lb") + str(j)
            x[j] = Label(self.canvas, width=200, height=200, image=l[j])
            self.cn = Label(self.canvas, width=10, height=1,text=c[j])
            x[j].place(x=m, y=n)
            self.cn.place(x=m+55,y=n+205)
            self.cn.configure(background="#FFFFFF")
            x[j].bind("<Button-1>", lambda y=0,v=c[j]: self.abc(y,v))
            if j % 3 == 0 and j != 0:
                n = n + 210
                m = 20
            else:
                m = m + 210
            i = i + 1
        self.root.mainloop()

