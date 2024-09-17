#
# Python Ver:   3.12.5
#
# Author:       Ozan S.
#
# Purpose:      Student Tracking Assignment

import tkinter as tk
from tkinter import *
import student_tracking_gui
import student_tracking_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.title("Student Tracking")
        self.master.minsize(500, 300)
        self.master.maxsize(500, 300)

# Load widgets
        student_tracking_gui.load_gui(self)

# Load Database     
        student_tracking_func.create_db(self)
        student_tracking_func.refresh_student_list(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
