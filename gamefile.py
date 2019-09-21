from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfile
from PIL import Image,ImageTk
from connectionfile import *
from shutil import copyfile
from os import path
from pathlib import Path
# pip install pyttsx3 pypiwin32
import pyttsx3
from viewcategories import *
class gamefile:
    sq = ''
    ga = ''
    gl = []
    il = 0
    cl = 0
    ae = []
    ic = 0
    qindex=0
    sc=0
    def __init__(self,cname):
        self.imageindex = 0
        self.root = Tk()
        self.root.title("GAME")
        self.root.geometry("1000x550")
        self.alphabets=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.images=["hangimages/hanged.jpg","hangimages/hanged1.jpg","hangimages/hanged2.jpg","hangimages/hanged3.jpg","hangimages/hanged4.jpg","hangimages/hanged5.jpg","hangimages/hanged6.jpg"]
        self.lbcat=Label(self.root,text=cname)
        self.score=StringVar()
        self.question = StringVar()
        self.lbscore=Label(self.root,textvariable=self.score)
        self.lbquestion=Label(self.root,textvariable=self.question)
        self.lbquestion.config(bg='white', fg='black')
        labelfont = ('times', 10, 'bold')
        self.lbquestion.config(font=labelfont)
        self.lbquestion.config(height=10, width=70)
        conn=connectionfile.connect('')
        cr=conn.cursor()
        query='select score from score'
        cr.execute(query)
        result=cr.fetchone()
        query2="select * from questions where catname='"+cname+"' ORDER BY rand() LIMIT 10"
        cr.execute(query2)
        result2=cr.fetchall()
        self.questions=[]
        for row in result2:
            sl=[]
            sl.append(row[1])
            sl.append(row[2])
            self.questions.append(sl)
        ep=self.splitstring(str(self.questions[self.qindex][0]))
        self.question.set(str(ep[0]+"\n"+ep[1]))
        self.sq=str(self.questions[self.qindex][0])
        self.ga=str(self.questions[self.qindex][1])
        self.gl = list(self.ga)
        self.ll=[]
        for i in range(0,len(self.gl)):
            self.ll.append("_")
        self.sc=result[0]
        self.score.set("score "+str(self.sc))
        im = Image.open(self.images[self.imageindex]).resize((200, 200), Image.ANTIALIAS)  # This is the correct location and spelling for my image location
        self.photo = ImageTk.PhotoImage(im)
        self.lbphoto = Label(self.root, width=200, height=200, image=self.photo)
        self.btsuggest=Button(self.root,text="EXIT GAME",command=self.exitgame)
        self.bthint=Button(self.root,text="HINT",command=self.hint)
        self.lbcat.grid(row=0,column=0,padx=5,pady=5)
        self.lbscore.grid(row=0,column=2,pady=5)
        self.lbphoto.place(x=20, y=70)
        self.lbphoto.grid(row=1, column=1)
        self.lbquestion.grid(row=1,column=2,padx=5)
        self.btsuggest.grid(row=4,column=0,padx=5)
        self.bthint.grid(row=4,column=2)
        self.frame = Frame(self.root, width=700, height=300)
        self.frame.grid(row=5, column=0,columnspan=7,pady=5)
        self.canvas = Canvas(self.frame, bg='#FFFFFF', width=300, height=300)
        self.canvas.config(width=700, height=300)
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)
        self.canvas.config(background="#FFA500")
        u=5
        w=5
        self.svll=[]
        for i in range(0,len(self.ll)):
            self.sv="var"+str(i)
            self.sv=StringVar()
            self.ll[i] = Label(self.canvas,textvariable=self.sv, width=5, height=1)
            self.sv.set("_")
            self.ll[i].place(x=u, y=w)
            self.svll.append(self.sv)
            u=u+30
        m=20
        n=100
        self.bl=[]
        for k in range(0,len(self.alphabets)):
            v1 = self.alphabets[k] + ""
            self.t=self.alphabets[k]
            self.t = Button(self.canvas, text=v1, width=5, height=1)
            self.t.place(x=m, y=n)
            self.t.bind("<Button-1>", lambda y=0, v=v1: self.buttonpress(y, v))
            if k % 10 == 0 and k != 0:
                n = n + 30
                m = 20
            else:
                m = m + 30
            self.bl.append(self.t)
        self.root.config(background="#FFA500")
        self.root.mainloop()
    def buttonpress(self,event,bt):
        print(bt)
        w=str(bt)
        w=w.lower();
        flag =True
        for i in range(0,len(self.ae)):
            if w==str(self.ae[i]):
                flag=False
                break
        if self.qindex>3:
            showinfo('', 'Game Over')
            # One time initialization
            engine = pyttsx3.init()

            # Set properties _before_ you add things to say
            engine.setProperty('rate', 150)  # Speed percent (can go over 100)
            engine.setProperty('volume', 0.9)  # Volume 0-1

            # Queue up things to say.
            # There will be a short break between each one
            # when spoken, like a pause between sentences.
            engine.say("Game over!")
            engine.say("Now try next category")

            # Flush the say() queue and play the audio
            engine.runAndWait()

            # Program will not continue execution until
            # all speech is done talking

            self.root.destroy()
        if flag==True:
            indexl = []
            length = 0
            # print('length gl ' + str(len(self.gl)) + str(" ") + w)
            for i in range(0, len(self.gl)):
                if w == str(self.gl[i]):
                    # print('match ' + str(self.gl[i]) + " " + w)
                    indexl.append(i)
            length = len(indexl)
            # print('length ' + str(length) + '  index ' + str(indexl))
            if length == 0:
                # print('if')
                self.ic = self.ic + 1
                self.ae.append(w)
                if self.imageindex == 5:
                    self.imageindex = self.imageindex + 1
                    im = Image.open(self.images[self.imageindex]).resize((200, 200),
                                                                         Image.ANTIALIAS)  # This is the correct location and spelling for my image location
                    self.photo = ImageTk.PhotoImage(im)
                    self.lbphoto = Label(self.root, width=200, height=200, image=self.photo)
                    self.lbphoto.grid(row=1, column=1)
                    showinfo('', 'you loss')
                    # One time initialization
                    engine = pyttsx3.init()

                    # Set properties _before_ you add things to say
                    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
                    engine.setProperty('volume', 0.9)  # Volume 0-1

                    # Queue up things to say.
                    # There will be a short break between each one
                    # when spoken, like a pause between sentences.
                    engine.say("You've lost the game!")
                    engine.say("You can try next question")
                    engine.say("Exact answer is "+self.ga)

                    # Flush the say() queue and play the audio
                    engine.runAndWait()

                    # Program will not continue execution until
                    # all speech is done talking


                    conn = connectionfile.connect('')
                    cr = conn.cursor()
                    query = "update  score set score='" + str(self.sc) + "'"
                    cr.execute(query)
                    conn.commit()
                    for i in range(0, len(self.alphabets)):
                        self.bl[i].configure(bg="white")
                    self.sq = ''
                    self.ga = ''
                    ln=len(self.gl)
                    self.gl.clear()
                    self.il = 0
                    self.cl = 0
                    self.ae.clear()
                    self.ic = 0
                    if self.qindex <9:
                        self.qindex = self.qindex + 1
                        ep = self.splitstring(str(self.questions[self.qindex][0]))

                        self.question.set(str(ep[0] + "\n" + ep[1]))
                        self.sq = str(self.questions[self.qindex][0])
                        self.ga = str(self.questions[self.qindex][1])
                        self.gl = list(self.ga)
                        self.ll = []
                        for i in range(0, len(self.gl)):
                            self.ll.append("_")
                        u = 5
                        w = 5
                        self.svll.clear()
                        c=0
                        for i in range(0, len(self.ll)):
                            self.sv = "var" + str(i)
                            self.sv = StringVar()
                            self.ll[i] = Label(self.canvas, textvariable=self.sv, width=5, height=1)
                            self.sv.set("_")
                            self.ll[i].place(x=u, y=w)
                            self.svll.append(self.sv)
                            u = u + 30
                            c=i
                        diff=ln-len(self.gl)
                        # print('diff '+str(diff)+"  c "+str(c)+" temp "+str(ln)+"  ll"+str(len(self.gl)))
                        if ln>len(self.ll):
                            for i in range(0, diff):
                                self.ll.append("_")
                                c = c + 1
                                self.sv = "var" + str(i)
                                self.sv = StringVar()
                                self.ll[c] = Label(self.canvas, textvariable=self.sv, width=5, height=1)
                                self.sv.set("")
                                self.ll[c].place(x=u, y=w)
                                self.svll.append(self.sv)
                                u = u + 30
                        self.imageindex = 0
                        im = Image.open(self.images[self.imageindex]).resize((200, 200),
                                                                             Image.ANTIALIAS)  # This is the correct location and spelling for my image location
                        self.photo = ImageTk.PhotoImage(im)
                        self.lbphoto = Label(self.root, width=200, height=200, image=self.photo)
                        self.lbphoto.grid(row=1, column=1)
                    else:
                        showinfo('', 'Game Over')
                        self.root.destroy()
                else:
                    for i in range(0, len(self.alphabets)):
                        if self.alphabets[i] == bt:
                            self.bl[i].configure(bg="red")
                    self.imageindex = self.imageindex + 1
                    im = Image.open(self.images[self.imageindex]).resize((200, 200),
                                                                         Image.ANTIALIAS)  # This is the correct location and spelling for my image location
                    self.photo = ImageTk.PhotoImage(im)
                    self.lbphoto = Label(self.root, width=200, height=200, image=self.photo)
                    self.lbphoto.grid(row=1, column=1)
            else:
                # print('else')
                self.cl = self.cl + length
                self.ae.append(w)
                for i in range(0, len(self.alphabets)):
                    if self.alphabets[i] == bt:
                        self.bl[i].configure(bg="green")
                for i in range(0, len(indexl)):
                    self.svll[indexl[i]].set(w)
                if self.cl == len(self.gl):
                    showinfo('', 'you win')
                    # One time initialization
                    engine = pyttsx3.init()

                    # Set properties _before_ you add things to say
                    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
                    engine.setProperty('volume', 0.9)  # Volume 0-1

                    # Queue up things to say.
                    # There will be a short break between each one
                    # when spoken, like a pause between sentences.
                    engine.say("You've won the game!")
                    engine.say("Now try next question")

                    # Flush the say() queue and play the audio
                    engine.runAndWait()

                    # Program will not continue execution until
                    # all speech is done talking

                    self.sc = self.sc + 5
                    self.score.set("score " + str(self.sc))
                    conn = connectionfile.connect('')
                    cr = conn.cursor()
                    query = "update  score set score='" + str(self.sc) + "'"
                    cr.execute(query)
                    conn.commit()
                    for i in range(0, len(self.alphabets)):
                        self.bl[i].configure(bg="white")
                    self.sq = ''
                    self.ga = ''
                    ln=len(self.gl)
                    self.gl.clear()
                    self.il = 0
                    self.cl = 0
                    self.ae.clear()
                    self.ic = 0
                    if self.qindex < 9:
                        self.qindex = self.qindex + 1
                        ep = self.splitstring(str(self.questions[self.qindex][0]))

                        self.question.set(str(ep[0] + "\n" + ep[1]))
                        self.sq = str(self.questions[self.qindex][0])
                        self.ga = str(self.questions[self.qindex][1])
                        self.gl = list(self.ga)
                        self.ll = []
                        for i in range(0, len(self.gl)):
                            self.ll.append("_")
                        u = 5
                        w = 5
                        self.svll.clear()
                        c=0
                        for i in range(0, len(self.ll)):
                            self.sv = "var" + str(i)
                            self.sv = StringVar()
                            self.ll[i] = Label(self.canvas, textvariable=self.sv, width=5, height=1)
                            self.sv.set("_")
                            self.ll[i].place(x=u, y=w)
                            self.svll.append(self.sv)
                            u = u + 30
                            c=i
                        diff = ln - len(self.ll)
                        # print('diff ' + str(diff) + "  c " + str(c) + " temp " + str(ln) + "  ll" + str(len(self.gl)))
                        if ln > len(self.gl):
                            for i in range(0, diff):
                                self.ll.append("_")
                                c = c + 1
                                self.sv = "var" + str(i)
                                self.sv = StringVar()
                                self.ll[c] = Label(self.canvas, textvariable=self.sv, width=5, height=1)
                                self.sv.set("")
                                self.ll[c].place(x=u, y=w)
                                self.svll.append(self.sv)
                                u = u + 30
                        self.imageindex = 0
                        im = Image.open(self.images[self.imageindex]).resize((200, 200),
                                                                             Image.ANTIALIAS)  # This is the correct location and spelling for my image location
                        self.photo = ImageTk.PhotoImage(im)
                        self.lbphoto = Label(self.root, width=200, height=200, image=self.photo)
                        self.lbphoto.grid(row=1, column=1)
                    else:
                        showinfo('', 'Game Over')
                        self.root.destroy()
    def hint(self):
        if self.sc>0:
            flag = True
            w = ''
            bt = ''
            for i in range(0, len(self.gl)):
                w = self.gl[i]
                if w not in self.ae:
                    flag = False
                    break
            if self.qindex>3:
                showinfo('', 'Game Over')
                # One time initialization
                engine = pyttsx3.init()

                # Set properties _before_ you add things to say
                engine.setProperty('rate', 150)  # Speed percent (can go over 100)
                engine.setProperty('volume', 0.9)  # Volume 0-1

                # Queue up things to say.
                # There will be a short break between each one
                # when spoken, like a pause between sentences.
                engine.say("Game over!")
                engine.say("Now try next category")

                # Flush the say() queue and play the audio
                engine.runAndWait()

                # Program will not continue execution until
                # all speech is done talking

                self.root.destroy()
            if flag == False:
                w = w.lower();
                bt = w.upper()
                flag = True
                for i in range(0, len(self.ae)):
                    if w == str(self.ae[i]):
                        flag = False
                        break
                if flag == True:
                    indexl = []
                    length = 0
                    # print('length gl ' + str(len(self.gl)) + str(" ") + w)
                    for i in range(0, len(self.gl)):
                        if w == str(self.gl[i]):
                            # print('match ' + str(self.gl[i]) + " " + w)
                            indexl.append(i)
                    length = len(indexl)
                    # print('length ' + str(length) + '  index ' + str(indexl))
                    if length == 0:
                        # print('if')
                        self.ic = self.ic + 1
                        self.ae.append(w)
                        if self.imageindex == 5:
                            self.imageindex = self.imageindex + 1
                            im = Image.open(self.images[self.imageindex]).resize((200, 200),
                                                                                 Image.ANTIALIAS)  # This is the correct location and spelling for my image location
                            self.photo = ImageTk.PhotoImage(im)
                            self.lbphoto = Label(self.root, width=200, height=200, image=self.photo)
                            self.lbphoto.grid(row=1, column=1)
                            showinfo('', 'you loss')
                            # One time initialization
                            engine = pyttsx3.init()

                            # Set properties _before_ you add things to say
                            engine.setProperty('rate', 150)  # Speed percent (can go over 100)
                            engine.setProperty('volume', 0.9)  # Volume 0-1

                            # Queue up things to say.
                            # There will be a short break between each one
                            # when spoken, like a pause between sentences.
                            engine.say("You've lost the game!")
                            engine.say("You can try next question")
                            engine.say("Exact answer is "+self.ga)

                            # Flush the say() queue and play the audio
                            engine.runAndWait()

                            # Program will not continue execution until
                            # all speech is done talking

                            conn = connectionfile.connect('')
                            cr = conn.cursor()
                            query = "update  score set score='" + str(self.sc) + "'"
                            cr.execute(query)
                            conn.commit()
                            for i in range(0, len(self.alphabets)):
                                self.bl[i].configure(bg="white")
                            self.sq = ''
                            self.ga = ''
                            ln=len(self.gl)
                            self.gl.clear()
                            self.il = 0
                            self.cl = 0
                            self.ae.clear()
                            self.ic = 0
                            if self.qindex < 9:
                                self.qindex = self.qindex + 1
                                ep = self.splitstring(str(self.questions[self.qindex][0]))
                                self.question.set(str(ep[0] + "\n" + ep[1]))
                                self.sq = str(self.questions[self.qindex][0])
                                self.ga = str(self.questions[self.qindex][1])
                                self.gl = list(self.ga)
                                self.ll = []
                                for i in range(0, len(self.gl)):
                                    self.ll.append("_")
                                u = 5
                                w = 5
                                c=0
                                self.svll.clear()
                                for i in range(0, len(self.ll)):
                                    self.sv = "var" + str(i)
                                    self.sv = StringVar()
                                    self.ll[i] = Label(self.canvas, textvariable=self.sv, width=5, height=1)
                                    self.sv.set("_")
                                    self.ll[i].place(x=u, y=w)
                                    self.svll.append(self.sv)
                                    u = u + 30
                                    c=i
                                diff = ln - len(self.gl)
                                # print('diff ' + str(diff) + "  c " + str(c) + " temp " + str(ln) + "  ll" + str(len(self.gl)))
                                if ln > len(self.ll):
                                    for i in range(0, diff):
                                        self.ll.append("_")
                                        c = c + 1
                                        self.sv = "var" + str(i)
                                        self.sv = StringVar()
                                        self.ll[c] = Label(self.canvas, textvariable=self.sv, width=5, height=1)
                                        self.sv.set("")
                                        self.ll[c].place(x=u, y=w)
                                        self.svll.append(self.sv)
                                        u = u + 30
                                self.imageindex = 0
                                im = Image.open(self.images[self.imageindex]).resize((200, 200),
                                                                                     Image.ANTIALIAS)  # This is the correct location and spelling for my image location
                                self.photo = ImageTk.PhotoImage(im)
                                self.lbphoto = Label(self.root, width=200, height=200, image=self.photo)
                                self.lbphoto.grid(row=1, column=1)
                            else:
                                showinfo('', 'Game Over')
                                self.root.destroy()
                        else:
                            for i in range(0, len(self.alphabets)):
                                if self.alphabets[i] == bt:
                                    self.bl[i].configure(bg="red")
                            self.imageindex = self.imageindex + 1
                            im = Image.open(self.images[self.imageindex]).resize((200, 200),
                                                                                 Image.ANTIALIAS)  # This is the correct location and spelling for my image location
                            self.photo = ImageTk.PhotoImage(im)
                            self.lbphoto = Label(self.root, width=200, height=200, image=self.photo)
                            self.lbphoto.grid(row=1, column=1)
                    else:
                        # print('else')
                        self.cl = self.cl + length
                        self.ae.append(w)
                        for i in range(0, len(self.alphabets)):
                            if self.alphabets[i] == bt:
                                self.bl[i].configure(bg="green")
                        for i in range(0, len(indexl)):
                            self.svll[indexl[i]].set(w)
                        self.sc = self.sc - 5
                        self.score.set("score " + str(self.sc))
                        if self.cl == len(self.gl):
                            showinfo('', 'you win')
                            # One time initialization
                            engine = pyttsx3.init()

                            # Set properties _before_ you add things to say
                            engine.setProperty('rate', 150)  # Speed percent (can go over 100)
                            engine.setProperty('volume', 0.9)  # Volume 0-1

                            # Queue up things to say.
                            # There will be a short break between each one
                            # when spoken, like a pause between sentences.
                            engine.say("You've won the game!")
                            engine.say("Now try next question")

                            # Flush the say() queue and play the audio
                            engine.runAndWait()

                            # Program will not continue execution until
                            # all speech is done talking

                            conn = connectionfile.connect('')
                            cr = conn.cursor()
                            query = "update  score set score='" + str(self.sc) + "'"
                            cr.execute(query)
                            conn.commit()
                            for i in range(0, len(self.alphabets)):
                                self.bl[i].configure(bg="white")
                            self.sq = ''
                            self.ga = ''
                            ln=len(self.gl)
                            self.gl.clear()
                            self.il = 0
                            self.cl = 0
                            self.ae.clear()
                            self.ic = 0
                            if self.qindex <9:
                                self.qindex = self.qindex + 1
                                ep = self.splitstring(str(self.questions[self.qindex][0]))
                                self.question.set(str(ep[0] + "\n" + ep[1]))
                                self.sq = str(self.questions[self.qindex][0])
                                self.ga = str(self.questions[self.qindex][1])
                                self.gl = list(self.ga)
                                self.ll = []
                                for i in range(0, len(self.gl)):
                                    self.ll.append("_")
                                u = 5
                                w = 5
                                c=0
                                self.svll.clear()
                                for i in range(0, len(self.ll)):
                                    self.sv = "var" + str(i)
                                    self.sv = StringVar()
                                    self.ll[i] = Label(self.canvas, textvariable=self.sv, width=5, height=1)
                                    self.sv.set("_")
                                    self.ll[i].place(x=u, y=w)
                                    self.svll.append(self.sv)
                                    u = u + 30
                                    c=i
                                diff = ln - len(self.gl)
                                # print('diff ' + str(diff) + "  c " + str(c) + " temp " + str(ln) + "  ll" + str(len(self.gl)))
                                if ln > len(self.ll):
                                    for i in range(0, diff):
                                        self.ll.append("_")
                                        c = c + 1
                                        self.sv = "var" + str(i)
                                        self.sv = StringVar()
                                        self.ll[c] = Label(self.canvas, textvariable=self.sv, width=5, height=1)
                                        self.sv.set("")
                                        self.ll[c].place(x=u, y=w)
                                        self.svll.append(self.sv)
                                        u = u + 30
                                self.imageindex = 0
                                im = Image.open(self.images[self.imageindex]).resize((200, 200),
                                                                                     Image.ANTIALIAS)  # This is the correct location and spelling for my image location
                                self.photo = ImageTk.PhotoImage(im)
                                self.lbphoto = Label(self.root, width=200, height=200, image=self.photo)
                                self.lbphoto.grid(row=1, column=1)
                            else:
                                showinfo('', 'Game Over')
                                self.root.destroy()

        else:
            showinfo('', 'score is not enough for hint')
            # One time initialization
            engine = pyttsx3.init()

            # Set properties _before_ you add things to say
            engine.setProperty('rate', 150)  # Speed percent (can go over 100)
            engine.setProperty('volume', 0.9)  # Volume 0-1

            # Queue up things to say.
            # There will be a short break between each one
            # when spoken, like a pause between sentences.
            engine.say("score is not enough for hint!")
            engine.say("sorry")

            # Flush the say() queue and play the audio
            engine.runAndWait()

            # Program will not continue execution until
            # all speech is done talking
    def exitgame(self):
         self.root.destroy()
    def splitstring(self,v):
        str = v+"                                                          ";
        # Stores the length of the string
        length = len(str);
        # n determines the variable that divide the string in 'n' equal parts
        n = 2;
        temp = 0;
        chars = int(length / n);
        # Stores the array of string
        equalStr = [];
        # Check whether a string can be divided into n equal parts
        if (length % n != 0):
            # print("Sorry this string cannot be divided into " + str(n) + " equal parts.");
            if length>30:
                part1 = str[0: 60];
                part2=str[61:]
                equalStr.append(part1)
                equalStr.append(part2)
            else:
                equalStr.append(str)
                equalStr.append("")
            return equalStr
        else:
            for i in range(0, length, chars):
                # Dividing string in n equal part using substring()
                part = str[i: i + chars];
                equalStr.append(part);
            print("Equal parts of given string are");
            # for i in equalStr:
                # print(i);
            return equalStr






