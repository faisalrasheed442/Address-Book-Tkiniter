import mysql.connector
from tkinter import *
import mysql
root=Tk()
root.geometry("400x400")
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="phonebook"
    )
mycursor=db.cursor()
# mycursor.execute("SELECT * From conntacts" )
mycursor.execute("SELECT * FROM conntacts WHERE id=0")
resulti=mycursor.fetchall()
for x in resulti:
    print(x)
# for y in range(len(x)):
#     box.insert(y,str(x[y][4])+"-"+str(x[y][0]))
