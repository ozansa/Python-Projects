import sqlite3
from tkinter import END, messagebox  

def create_db(self):
    conn = sqlite3.connect('student_tracking.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tbl_students (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                fname TEXT,
                lname TEXT,
                phone TEXT,
                email TEXT,
                course TEXT
            );
        """)
        conn.commit()
    conn.close()


def add_student(self):
    fname = self.txt_fname.get().strip()
    lname = self.txt_lname.get().strip()
    phone = self.txt_phone.get().strip()
    email = self.txt_email.get().strip()
    course = self.txt_course.get().strip()

    if fname and lname and phone and email and course:
        conn = sqlite3.connect('student_tracking.db')
        with conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO tbl_students (fname, lname, phone, email, course)
                VALUES (?, ?, ?, ?, ?)
            """, (fname, lname, phone, email, course))
            conn.commit()
        conn.close()
        refresh_student_list(self)
        clear_form(self)
    else:
        messagebox.showerror("Input Error", "All fields are required")


def refresh_student_list(self):
    self.lst_students.delete(0, END)
    conn = sqlite3.connect('student_tracking.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM tbl_students")
        students = cur.fetchall()
        for student in students:
            display_text = f"{student[1]} {student[2]} | {student[3]} | {student[4]} | {student[5]}"
            self.lst_students.insert(END, display_text)
    conn.close()


def delete_student(self):
    selected_student = self.lst_students.curselection()
    if selected_student:
        student = self.lst_students.get(selected_student).split(" | ")
        fname, lname = student[0].split(" ")
        conn = sqlite3.connect('student_tracking.db')
        with conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM tbl_students WHERE fname=? AND lname=?", (fname, lname))
            conn.commit()
        conn.close()
        refresh_student_list(self)
    else:
        messagebox.showerror("Selection Error", "Please select a student to delete!!")


def clear_form(self):
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)
    self.txt_course.delete(0, END)
