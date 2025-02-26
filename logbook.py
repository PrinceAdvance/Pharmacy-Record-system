# -*- coding: utf-8 -*-
"""
Created on Sun May  7 08:01:44 2023

@author: Admin
"""

import tkinter as tk
from tkinter import ttk  
import os
import openpyxl

root = tk.Tk()
root.title("Patient Recording System")



# enter data code
def enter_data():
    firstname = name_of_patient_combobox.get()
    surname = surname_combobox.get()
    date_id = date_id_Entry.get()
    prescribed_drug = truck_id_combobox.get()
    Doctor = Doctor_Entry.get()

    print("First name: ",firstname, "Surname: ", surname)
    print("Equipment: ", prescribed_drug)
    print("Date: ", date_id)
    print("Doctor: ", Doctor)

    filepath = "C:\\Users\\Admin\\Desktop\\MyPython Projects\\Tkinter Projects\\logbook project\\logbook.py.xlsx"

    if not os.path.exists(filepath):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        heading = ['first name','Surname','Date','Equipment','Doctor']
        sheet.append(heading)
        workbook.save(filepath)
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    sheet.append([firstname, surname, prescribed_drug,date_id, Doctor]) 
    workbook.save(filepath)   

canvas = tk.Canvas(root, width = 300, height = 300)
canvas.pack()

frame = tk.Frame(canvas)
frame.pack()

#first frame
frame1 = tk.LabelFrame(frame, text = "User Information", )
frame1.grid(row = 0, column = 0, padx = 20, pady = 20)

name_of_patient = tk.Label(frame1, text = "First name")
name_of_patient.grid(row = 0, column = 0)

surname = tk.Label(frame1, text = "Surname")
surname.grid(row = 0, column = 4)

date_id = tk.Label(frame1, text = "Date")
date_id.grid(row = 0, column = 6)
  
prescribed_drug = tk.Label(frame1, text = "Drug")
prescribed_drug.grid(row = 2, column = 0)

Doctor = tk.Label(frame1, text = "Doctor")
Doctor.grid(row = 2, column = 4)

name_of_patient_combobox = ttk.Combobox(frame1,values = ["perogozin"])
surname_combobox = ttk.Combobox(frame1,values = [""])
truck_id_combobox = ttk.Combobox(frame1,values = [""])
Doctor_Entry = tk.Entry(frame1)
date_id_Entry = tk.Entry(frame1)


name_of_patient_combobox.grid(row = 1, column = 0)
surname_combobox.grid(row = 1, column = 4)
truck_id_combobox.grid(row = 3, column = 0)
Doctor_Entry.grid(row = 3, column = 4)
date_id_Entry.grid(row = 1, column = 6)



for widget in frame1.winfo_children():
    widget.grid_configure(padx = 10,pady = 5)

# frame 2
frame2 = tk.LabelFrame(frame)
frame2.grid(row = 1,column = 0)

# Button
button = tk.Button(frame2,text = "Enter Data",command = enter_data)
button.grid(row = 0)

root.mainloop() 