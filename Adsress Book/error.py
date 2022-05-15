# import sqlite3
from tkinter import messagebox

# db = sqlite3.connect('store.db')
# c=db.cursor()
# def verify_login(table,email,password):
#     details = c.execute(f"SELECT * from'{table}' WHERE email ='{email}' And password='{password}'").fetchall()
#     return details
# # c.execute("CREATE TABLE f (id INTEGER PRIMARY KEY, name varchar(20), email varchar(20), password varchar(20))")
# # c.execute("INSERT INTO f (name,email,password) VALUES('faisal','dsd','2345')")
# # x=c.execute("SELECT * FROM f WHERE name='faisal' AND email='pp'").fetchall()
# x=verify_login("user","testing@gmail.com","test")
# print(x)
# # db.commit()
# # from tkinter import *
# # from tkinter import messagebox
# # messagebox.askyesno(title="s",message="Ss",optio)
x=messagebox.askyesno(title="Info",message="are you a new user")
if x=="yes":
    print("yes")
else:
    print("no")