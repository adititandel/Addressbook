import sqlite3

import tkinter as tk
from tkinter import *

import addressbook_func


def load_gui(self):
    self.lbl_fname = tk.Label(self.master, text='First Name:', font=("Helvetica", 10))
    self.lbl_fname.grid(row=0, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lbl_lname = tk.Label(self.master, text='Last Name:', font=("Helvetica", 10))
    self.lbl_lname.grid(row=0, column=2, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lbl_street = tk.Label(self.master, text='Street:', font=("Helvetica", 10))
    self.lbl_street.grid(row=2, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lbl_city = tk.Label(self.master, text='City:', font=("Helvetica", 10))
    self.lbl_city.grid(row=6, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lbl_state = tk.Label(self.master, text='State:', font=("Helvetica", 10))
    self.lbl_state.grid(row=6, column=2, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lbl_zip = tk.Label(self.master, text='Zip code:', font=("Helvetica", 10))
    self.lbl_zip.grid(row=6, column=4, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lbl_zip = tk.Label(self.master, text='Zip code:', font=("Helvetica", 10))
    self.lbl_zip.grid(row=6, column=4, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lbl_first = tk.Label(self.master, font=("Helvetica", 10))
    self.lbl_first.place(x=140, y=275, anchor='sw')

    self.txt_fname = tk.Entry(self.master, text='', font=("Helvetica", 8))
    self.txt_fname.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N + E + W)
    self.txt_lname = tk.Entry(self.master, text='', font=("Helvetica", 8))
    self.txt_lname.grid(row=1, column=2, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N + E + W)
    self.txt_street = tk.Entry(self.master, text='', font=("Helvetica", 8))
    self.txt_street.grid(row=5, column=0, rowspan=1, columnspan=5, padx=(30, 40), pady=(0, 0), sticky=N + E + W)
    self.txt_city = tk.Entry(self.master, text='', font=("Helvetica", 8))
    self.txt_city.grid(row=7, column=0, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N + E + W)
    self.txt_state = tk.Entry(self.master, text='', font=("Helvetica", 8))
    self.txt_state.grid(row=7, column=2, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N + E + W)
    self.txt_zip = tk.Entry(self.master, text='', font=("Helvetica", 8))
    self.txt_zip.grid(row=7, column=4, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N + E + W)

    self.btn_add = tk.Button(self.master, width=10, height=2, text='Add',
                             command=lambda: addressbook_func.onAdd(self))
    self.btn_add.grid(row=15, column=0, padx=(10, 0), pady=(45, 10), sticky=W)
    self.btn_first = tk.Button(self.master, width=10, height=2, text='First',
                               command=lambda: addressbook_func.onFirst(self))
    self.btn_first.grid(row=15, column=1, padx=(5, 1), pady=(45, 10), sticky=W)
    self.btn_next = tk.Button(self.master, width=10, height=2, text='Next',
                              command=lambda: addressbook_func.onNext(self))
    self.btn_next.grid(row=15, column=2, padx=(5, 2), pady=(45, 10), sticky=W)
    self.btn_previous = tk.Button(self.master, width=10, height=2, text='Previous',
                                  command=lambda: addressbook_func.onPrevious(self))
    self.btn_previous.grid(row=15, column=3, padx=(5, 2), pady=(45, 10), sticky=W)
    self.btn_last = tk.Button(self.master, width=10, height=2, text='Last',
                              command=lambda: addressbook_func.onLast(self))
    self.btn_last.grid(row=15, column=4, padx=(5, 4), pady=(45, 10), sticky=W)
    self.btn_update = tk.Button(self.master, width=10, height=2, text='Update',
                                command=lambda: addressbook_func.onUpdate(self))
    self.btn_update.grid(row=15, column=5, padx=(5, 5), pady=(45, 10), sticky=W)

    conn = sqlite3.connect('db_addressbook.db')
    with conn:
        cursor1 = conn.cursor()
        cursor2 = conn.cursor()
        cursor1.execute("""Select max(id) from tbl_addressbook""")
        self.bttn_clicks1 = cursor1.fetchone()[0]
        cursor2.execute("""Select min(id) from tbl_addressbook""")
        self.bttn_clicks2 = cursor2.fetchone()[0]
    self.bttn_check1 = 0
    self.bttn_check2 = 0
    self.bttn_check3 = 0
    self.bttn_check4 = 0
    self.bttn_check5 = 0

    addressbook_func.create_db()


if __name__ == "__main__":
    pass
