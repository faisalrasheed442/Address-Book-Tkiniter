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


class addpeople(Toplevel):
    def __init__(self):
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
        self.heading = Label(self.top, text="Add_people",font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        self.today = str(datetime.datetime.today()).split()
        self.heading_time = Label(
            self.top, text="Date: "+self.today[0], font="centaur 11", bg="white")
        self.heading_time.place(x=285, y=5)
        # Label 1
        self.name = Label(self.bottom, text="Name",
                          font="centaur 11", bg="#74b9ff")
        self.name.place(x=40,y=10)
        self.name1 = Entry(self.bottom, font="centaur 11", bg="white")
        self.name1.place(x=120,y=10)
        # label2
        self.sir_name = Label(self.bottom, text="Sir Name",
                          font="centaur 11", bg="#74b9ff")
        self.sir_name.place(x=40,y=40)
        self.sir_name1 = Entry(self.bottom, font="centaur 11", bg="white")
        self.sir_name1.place(x=120,y=40)
        # label 3
        self.emaill = Label(self.bottom, text="Email",
                          font="centaur 11", bg="#74b9ff")
        self.emaill.place(x=40,y=70)
        self.emaill1 = Entry(self.bottom, font="centaur 11", bg="white")
        self.emaill1.place(x=120,y=70)
        # label4
        self.phone = Label(self.bottom, text="Phone No.",
                          font="centaur 11", bg="#74b9ff")
        self.phone.place(x=40,y=100)
        self.phone1 = Entry(self.bottom, font="centaur 11", bg="white")
        self.phone1.place(x=120,y=100)
        # # label 5
        self.adress = Label(self.bottom, text="Address",
                          font="centaur 11", bg="#74b9ff")
        self.adress.place(x=40,y=130)
        self.address1 = Text(self.bottom,width=23,height=12,wrap=WORD ,font="centaur 11", bg="white")
        self.address1.place(x=120,y=130)
        # btn/////////////////////
        self.btnicon2 = PhotoImage(file="pimgs\icon4.png")
        self.add_people = Button(self.bottom, image=self.btnicon2, compound=LEFT, text="Add People",
                                 font="centaur 11", bg="white", width=100,command=self.add_peoplenow)
        self.add_people.place(x=150, y=350)
    def add_peoplenow(self):
        try:
            mycursor = db.cursor()
            mycursor.execute(
                f"INSERT INTO conntacts (Name,Sir_Name,Email,mobile,Address) VALUES('%s','%s','%s','%s','%s')" % (self.name1.get(), self.sir_name1.get(), self.emaill1.get(), self.phone1.get(), self.address1.get(1.0, "end-1c")))
            db.commit()
            mbox=messagebox.showinfo("Sucess","conntact has been added")
            self.destroy()
        except:
            mbox=messagebox.showerror("Warning","Please Enter Missing fileds")
