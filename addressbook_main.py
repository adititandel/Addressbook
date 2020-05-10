import tkinter as tk
from tkinter import *

import addressbook_func
import addressbook_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(580, 300)
        self.master.maxsize(580, 300)
        addressbook_func.center_window(self, 580, 300)
        self.master.title("Address Book")

        self.master.protocol("WM_DELETE_WINDOW", lambda: addressbook_func.ask_quit(self))

        addressbook_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
