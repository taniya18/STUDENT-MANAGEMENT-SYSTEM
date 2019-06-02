import tkinter as tk
import student1 as st
from tkinter import ttk
import sqlite3
mainWindow=tk.Tk()
mainWindow.geometry("1200x850+0+0")
mainWindow.title("STUDENT MANAGEMENT")
heading_label=tk.Label(mainWindow,font=("arial",20,'bold'),text="STUDENT MANAGEMENT",pady=20,padx=20)
heading_label.grid(row=0,column=1)
heading_label=tk.Label(mainWindow,font=("arial",20,'bold'),text="ENTER STUDENT NAME",pady=20,padx=20)
heading_label.grid(row=1,column=0)
name_field=tk.Entry(mainWindow,font=("arial",20,'bold'))
name_field.grid(row=1,column=1)
heading_label2=tk.Label(mainWindow,font=("arial",20,'bold'),text="ENTER STUDENT COLLEGE",pady=20,padx=20)
heading_label2.grid(row=2,column=0)
name_field2=tk.Entry(mainWindow,font=("arial",20,'bold'))
name_field2.grid(row=2,column=1)
heading_label3=tk.Label(mainWindow,font=("arial",20,'bold'),text="ENTER STUDENT ADDRESS",pady=20,padx=20)
heading_label3.grid(row=3,column=0)
name_field3=tk.Entry(mainWindow,font=("arial",20,'bold'))
name_field3.grid(row=3,column=1)
heading_label4=tk.Label(mainWindow,font=("arial",20,'bold'),text="ENTER STUDENT PHONE",pady=20,padx=20)
heading_label4.grid(row=4,column=0)
name_field4=tk.Entry(mainWindow,font=("arial",20,'bold'))
name_field4.grid(row=4,column=1)


def create_data():
    print("table created")
    st.create_table()


def ValueInput():
    name=name_field.get()
    college=name_field2.get()
    address=name_field3.get()
    phone=int(name_field4.get())

    st.insert_record(name,college,address,phone)
    print("data input successful")

def retrieve_record():
    print("record reyrieved")
    st.display_record()

def close_file():
    print("connection closed")
    st.close_database()
def destroyRootWindow():
    mainWindow.destroy()

button=tk.Button(mainWindow,font=("arial",20,'bold'),text="create table",command=lambda: create_data())
button.grid(row=5,column=0)
button=tk.Button(mainWindow,font=("arial",20,'bold'),text="save record",command=lambda: ValueInput())
button.grid(row=5,column=1)
button=tk.Button(mainWindow,font=("arial",20,'bold'),text="display record",command=lambda: retrieve_record())
button.grid(row=5,column=2)
button=tk.Button(mainWindow,font=("arial",20,'bold'),text="close record",command=lambda: close_file())

mainWindow.mainloop()
