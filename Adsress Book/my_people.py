from tkinter import *
from tkinter import ttk
import mysql.connector
import add_people
import datetime
from tkinter import messagebox
import update_people
import display_con
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="phonebook",)
mycursor = db.cursor()
class mypeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("400x600")
        self.resizable(False,False)
        self.title("My people")
        # Frames/////////////////////////////////////////////
        # Frames/////////////////////////////////////////////
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=450, bg="#74b9ff")
        self.bottom.pack(fill=X)
        # styling///////////////////
        # Heading,image and date in top frame
        self.top_image = PhotoImage(file="pimgs\icon2.png")
        self.toplbl = Label(self.top, image=self.top_image, bg="white")
        self.toplbl.grid(row=0, column=0, padx=40)
        self.heading = Label(self.top, text="My Phone book",font="centaur 14", bg="white")
        self.heading.grid(row=0, column=1)
        self.today = str(datetime.datetime.today()).split()
        self.heading_time = Label(
            self.top, text="Date: "+self.today[0], font="centaur 11", bg="white")
        self.heading_time.place(x=285, y=5)
        self.listbox=Listbox(self.bottom,width=33,height=28,bg="white")
        self.listbox.grid(row=0,column=0,padx=(20,0),pady=(5,0))
        self.scroll=Scrollbar(self.bottom,orient=VERTICAL)
        self.scroll.configure(command=self.listbox.yview())
        self.listbox.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=1,sticky=N+S,pady=(5,0))
        # adding value to listbox
        # adding value to listbox
        mycursor.execute("SELECT * From conntacts")
        result = mycursor.fetchall()
        # adding value to listbox
        for x in range(len(result)):
            self.listbox.insert(x,str(result[x][0])+"-"+str(result[x][1]))
        # Add btn////////////////
        # Add btn////////////////
        # Add btn////////////////
        self.btnicon2 = PhotoImage(file="pimgs\icon4.png")
        self.add_people = Button(self.bottom, image=self.btnicon2, compound=LEFT,text="Add People", font="centaur 11", bg="white", width=100,command=self.add_peoplee)
        self.add_people.grid(row=0,column=4,sticky=N,pady=(5,0))
        # btn2nd/////////////////////
        self.btnicon3 = PhotoImage(file="pimgs\\btn2.png")
        self.update_people = Button(self.bottom, image=self.btnicon3, compound=LEFT,text="Update", font="centaur 11", bg="white", width=100,command=self.updatee)
        self.update_people.place(x=239,y=45)
        # btn3rd/////////
        self.btnicon4 = PhotoImage(file="pimgs\\btn3.png")
        self.display_people = Button(self.bottom, image=self.btnicon4, compound=LEFT,text="Display", font="centaur 11", bg="white", width=100,command=self.displa)
        self.display_people.place(x=239, y=85)
        # btn4th///////
        self.btnicon5 = PhotoImage(file="pimgs\\btn4.png")
        self.delete_people = Button(self.bottom, image=self.btnicon5, compound=LEFT,text="Delete", font="centaur 11", bg="white", width=100,command=self.dele)
        self.delete_people.place(x=239, y=125)
    def add_peoplee(self):
        adde=add_people.addpeople()
        self.destroy()
    def updatee(self):
        itm = self.listbox.curselection()
        dell = str(self.listbox.get(itm))
        done = dell.split("-")
        mycursor.execute(f"SELECT * FROM conntacts WHERE id={done[0]}")
        resulti=mycursor.fetchall()
        update_people.updateppl(
            resulti[0][0], resulti[0][1], resulti[0][2], resulti[0][3], resulti[0][4], resulti[0][1])
    def displa(self):
        itm = self.listbox.curselection()
        dell = str(self.listbox.get(itm))
        done = dell.split("-")
        mycursor.execute(f"SELECT * FROM conntacts WHERE id={done[0]}")
        resulti=mycursor.fetchall()
        display_con.disp(
            resulti[0][0], resulti[0][1], resulti[0][2], resulti[0][3], resulti[0][5], resulti[0][4])
    def dele(self):
        itm=self.listbox.curselection()
        dell=str(self.listbox.get(itm))
        done=dell.split("-")
        mboxi=messagebox.askquestion("Waning","You are about Delete a Person")
        try:
            if str(mboxi) =="yes":
                mycursor.execute(f"DELETE FROM conntacts WHERE id={done[0]}",)
                db.commit()
                self.listbox.delete(itm)
        except:
            mbox1=messagebox.showinfo("info","person is not deleted")
