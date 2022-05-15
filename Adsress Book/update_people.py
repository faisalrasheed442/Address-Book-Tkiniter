from tkinter import *
from tkinter import ttk
import mysql.connector
import datetime
from tkinter import messagebox
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="phonebook",)
mycursor = db.cursor()
class updateppl(Toplevel):
    def __init__(self,idi,n,s,e,p,a):
        self.n=n
        self.s=s
        self.e=e
        self.p=p
        self.a=a
        self.idi=idi
        Toplevel.__init__(self)
        self.geometry("400x600")
        self.resizable(False, False)
        self.title("Add People")
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=450, bg="#74b9ff")
        self.bottom.pack(fill=X)
        # styling///////////////////
        # Heading,image and date in top frame
        self.top_image = PhotoImage(file="pimgs\\add_people.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        self.heading = Label(self.top, text="Add_people",
                             font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        self.today = str(datetime.datetime.today()).split()
        self.heading_time = Label(
            self.top, text="Date: "+self.today[0], font="centaur 11", bg="white")
        self.heading_time.place(x=285, y=5)
        # Label 1
        self.name = Label(self.bottom, text="Name",
                          font="centaur 11", bg="#74b9ff")
        self.name.place(x=40, y=10)
        self.name1 = Entry(self.bottom, font="centaur 11", bg="white")
        self.name1.insert(0,self.n)
        self.name1.place(x=120, y=10)
        # label2
        self.sir_name = Label(self.bottom, text="Sir Name",
                              font="centaur 11", bg="#74b9ff")
        self.sir_name.place(x=40, y=40)
        self.sir_name1 = Entry(self.bottom, font="centaur 11", bg="white")
        self.sir_name1.insert(0, self.s)
        self.sir_name1.place(x=120, y=40)
        # label 3
        self.emaill = Label(self.bottom, text="Email",
                            font="centaur 11", bg="#74b9ff")
        self.emaill.place(x=40, y=70)
        self.emaill1 = Entry(self.bottom, font="centaur 11", bg="white")
        self.emaill1.insert(0, self.e)
        self.emaill1.place(x=120, y=70)
        # label4
        self.phone = Label(self.bottom, text="Phone No.",
                           font="centaur 11", bg="#74b9ff")
        self.phone.place(x=40, y=100)
        self.phone1 = Entry(self.bottom, font="centaur 11", bg="white")
        self.phone1.insert(0, self.p)
        self.phone1.place(x=120, y=100)
        # # label 5
        self.adress = Label(self.bottom, text="Address",
                            font="centaur 11", bg="#74b9ff")
        self.adress.place(x=40, y=130)
        self.address1 = Text(self.bottom, width=23, height=12,
                             wrap=WORD, font="centaur 11", bg="white")
        self.address1.insert(INSERT,self.a)
        self.address1.place(x=120, y=130)
        # btn/////////////////////
        self.btnicon2 = PhotoImage(file="pimgs\\btn2.png")
        self.add_people = Button(self.bottom, image=self.btnicon2, compound=LEFT, text="Update",
                                 font="centaur 11", bg="white", width=100, command=self.Update)
        self.add_people.place(x=150, y=350)

    def Update(self):
        try:
            self.ad = self.address1.get(1.0, "end-1c")
            sql_update = "UPDATE conntacts SET Name='%s', Sir_Name='%s', Email='%s', Mobile='%s', Address='%s' WHERE id='%s'" % (self.name1.get(), self.sir_name1.get(), self.emaill1.get(), self.phone1.get(),self.ad, self.idi)
            db.commit()
            # self.destroy()
        except:
            self.ad = self.address1.get(1.0, "end-1c")
            print(
                f"{self.name1.get()},{self.sir_name1.get()},{self.emaill1.get()},{self.phone1.get()}, {self.ad}")
            mbox = messagebox.showerror(
                "Warning", "Please Enter Missing fileds")
