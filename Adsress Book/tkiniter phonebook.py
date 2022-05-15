from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import my_people
import datetime
from tkinter import messagebox
import add_people
class application():
    def __init__(self,master):
        self.master=master
        # creating frames/////////////////////////////////
        # creating frames/////////////////////////////////
        self.top = Frame(master, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=450, bg="#74b9ff")
        self.bottom.pack(fill=X )
    # styling///////////////////
        # Heading,image and date in top frame
        self.top_image = PhotoImage(file="pimgs\icon2.png")
        self.toplbl=Label(self.top,image=self.top_image,bg="white")
        self.toplbl.grid(row=0,column=0,padx=40)
        self.heading =Label(self.top, text="My Phone book",font="centaur 14",bg="white")
        self.heading.grid(row=0,column=1)
        self.today=str(datetime.datetime.today()).split()
        self.heading_time = Label(self.top, text="Date: "+self.today[0],font="centaur 11", bg="white")
        self.heading_time.place(x=285 ,y=5)
        # Buttons main window
        # Buttons main window
        # Buttons main window
        self.btnicon1=PhotoImage(file="pimgs\icon3.png")
        self.person=Button(self.bottom,image=self.btnicon1,compound=LEFT,text="My People",font="centaur 11", bg="white",width=100,command=self.openpeople)
        self.person.place(x=150,y=10)
        # btn 2nd
        self.btnicon2=PhotoImage(file="pimgs\icon4.png")
        self.add_people = Button(self.bottom, image=self.btnicon2, compound=LEFT,text="Add People", font="centaur 11", bg="white", width=100, command=self.add_peoplee)
        self.add_people.place(x=150,y=70)
        # btn 3rd
        self.btnicon3=PhotoImage(file="pimgs\icon5.png")
        self.about_us=Button(self.bottom,image=self.btnicon3,compound=LEFT,text="About us",font="centaur 11", bg="white",width=100,command=self.about_us)
        self.about_us.place(x=150,y=130)
    def openpeople(self):
        people=my_people.mypeople()

    def add_peoplee(self):
        add_people.addpeople()
    def about_us(self):
        self.mbox = messagebox.showinfo(
            "About Us", "Created By Malik Faisal For more Info Contact on faisalrasheed442@gmail.com")
# Main function
def main():
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("vista")
    root.geometry("400x600")
    # root.resizable(width=False, height=False)
    root.iconbitmap("D:\python\Tkiniter GUI work\Adsress Book\pimgs\icon.ico")
    app=application(root)
    root.mainloop()
if __name__ == "__main__":
    main()
