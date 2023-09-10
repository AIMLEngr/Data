import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

notebook = ttk.Notebook(window)

O
def save_data():
    accepted = accept_var.get()
    if accepted=="Accepted":
        # User info

        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            region = nationality_combobox.get()

            # Course info
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()
            status = reg_status_var.get()

            print("Name: ", title, firstname, lastname, " || ", " Age: ", age)
            print("Region: ", region)
            print("Courses: ", numcourses, "Semesters: ", numsemesters)
            print("Status: ", status)
            print("---------------------------------------------------")

            #Create Table
            conn = sqlite3.connect("data.db")
            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
                    (firstname TEXT, lastname TEXT, title TEXT, age INT, region TEXT,
                    status TEXT, numcourses INT, numsemesters INT)
            '''
            conn.execute(table_create_query)

            #Insert Data
            data_insert_query = '''INSERT INTO Student_Data (firstname, lastname, title,
            age, region, status, numcourses, numsemesters) VALUES
            (?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (firstname, lastname, title, age, region,
                                 status, numcourses, numsemesters)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()

        else:
            tkinter.messagebox.showwarning(title="Error", message="First and Last name are required.")

    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms.")


notebook.add(Pinfo, text="Personal Info")
notebook.add(Comdata, text="Tab2")
notebook.pack()

window = tkinter.Tk()
window.title("Bio Data Sheet")


frame = tkinter.Frame(window)
frame.pack(padx=640, pady=480)

#Saving User Info
personal_info_frame = tkinter.LabelFrame(Pinfo, frame, text="Personal")
personal_info_frame.grid(row=0, column=0)
first_name_label = tkinter.Label(Pinfo, personal_info_frame, text="Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(Pinfo, personal_info_frame, text="Father Name")
last_name_label.grid(row=1, column=0)
CNIC_label = tkinter.Label(Pinfo, personal_info_frame, text="NIC Number")
CNIC_name_label.grid(row=2, column=0)
DOB_label = tkinter.Label(Pinfo, personal_info_frame, text="Date of Birth")
DOB_label.grid(row=2, column=1)

first_name_entry = tkinter.Entry(personal_info_frame)
last_name_entry = tkinter.Entry(personal_info_frame)
first_name_entry.grid(row=0, column=1)
last_name_entry.grid(row=1, column=1)
CNIC_entry = tkinter.Entry(personal_info_frame)
DOB_entry = tkinter.Entry(personal_info_frame)
CNIC_entry.grid(row=3, column=0)
DOB_entry.grid(row=3, column=1)


title_label = tkinter.Label(personal_info_frame, text="Title")
title_combobox = ttk.Combobox(personal_info_frame, value=["Mr.", "Ms.", "Mrs.", "Dr."])
title_label.grid(row=2, column=0)
title_combobox.grid(row=2, column=1)

age_label = tkinter.Label(personal_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(personal_info_frame, from_=18, to=80)
age_label.grid(row=3, column=0)
age_spinbox.grid(row=3, column=1)

nationality_label = tkinter.Label(personal_info_frame, text="Title")
nationality_combobox = ttk.Combobox(personal_info_frame, values=[Countries.py])
nationality_label.grid(row=4, column=0)
nationality_combobox.grid(row=4, column=1)

for widget in personal_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news")

registeration_label = tkinter.Label(courses_frame, text="Regiteration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registeration_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                          variable=reg_status_var, onvalue="Registered", offvalue="Not Regitered")
registeration_label.grid(row=0, column=0)
registeration_check.grid(row=0, column=1)

numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numcourses_label.grid(row=1, column=0)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=2, column=0)
numsemesters_spinbox.grid(row=2, column=1)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms & conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

#Button
button = tkinter.Button(frame, text="Submit & Save", command=save_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)





window.mainloop()
