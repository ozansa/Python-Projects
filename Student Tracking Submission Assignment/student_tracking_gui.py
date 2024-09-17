#
# Python Ver:   3.12.5
#
# Author:       Ozan S.
#
# Purpose:      Student Tracking Assignment




import tkinter as tk
from tkinter import *
import student_tracking_func

def load_gui(self):
# Labels
    self.lbl_fname = tk.Label(self.master, text="First Name:")
    self.lbl_fname.grid(row=0, column=0, padx=(20, 0), pady=(10, 0), sticky=W)
    self.txt_fname = tk.Entry(self.master)
    self.txt_fname.grid(row=0, column=1, padx=(20, 0), pady=(10, 0), sticky=W)

    self.lbl_lname = tk.Label(self.master, text="Last Name:")
    self.lbl_lname.grid(row=1, column=0, padx=(20, 0), pady=(10, 0), sticky=W)
    self.txt_lname = tk.Entry(self.master)
    self.txt_lname.grid(row=1, column=1, padx=(20, 0), pady=(10, 0), sticky=W)

    self.lbl_phone = tk.Label(self.master, text="Phone Number:")
    self.lbl_phone.grid(row=2, column=0, padx=(20, 0), pady=(10, 0), sticky=W)
    self.txt_phone = tk.Entry(self.master)
    self.txt_phone.grid(row=2, column=1, padx=(20, 0), pady=(10, 0), sticky=W)

    self.lbl_email = tk.Label(self.master, text="E-mail:")
    self.lbl_email.grid(row=3, column=0, padx=(20, 0), pady=(10, 0), sticky=W)
    self.txt_email = tk.Entry(self.master)
    self.txt_email.grid(row=3, column=1, padx=(20, 0), pady=(10, 0), sticky=W)

    self.lbl_course = tk.Label(self.master, text="Current Course:")
    self.lbl_course.grid(row=4, column=0, padx=(20, 0), pady=(10, 0), sticky=W)
    self.txt_course = tk.Entry(self.master)
    self.txt_course.grid(row=4, column=1, padx=(20, 0), pady=(10, 0), sticky=W)

# Submit 
    self.btn_submit = tk.Button(self.master, text="SUBMIT", width=12, height=2, command=lambda: student_tracking_func.add_student(self))
    self.btn_submit.grid(row=5, column=1, padx=(20, 0), pady=(10, 0), sticky=W)

# Student List 
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.lst_students = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar1.set)
    self.scrollbar1.config(command=self.lst_students.yview)
    self.scrollbar1.grid(row=0, column=3, rowspan=7, padx=(0, 0), pady=(0, 0), sticky=N+E+S)
    self.lst_students.grid(row=0, column=2, rowspan=7, padx=(20, 0), pady=(0, 0), sticky=N+E+S+W)

# Delete 
    self.btn_delete = tk.Button(self.master, text="DELETE", width=12, height=2, command=lambda: student_tracking_func.delete_student(self))
    self.btn_delete.grid(row=6, column=1, padx=(20, 0), pady=(10, 0), sticky=W)
