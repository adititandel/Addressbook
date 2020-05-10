import os
import sqlite3

from tkinter import *
from tkinter import messagebox


def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width / 2) - (w / 2))
    y = int((screen_height / 2) - (h / 2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)


def create_db():
    conn = sqlite3.connect('db_addressbook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_addressbook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_street TEXT, \
            col_city TEXT, \
            col_state TEXT, \
            col_zip TEXT \
            );")

        conn.commit()
    conn.close()


def count_records(cur):
    cur.execute("""SELECT COUNT(*) FROM tbl_addressbook""")
    count = cur.fetchone()[0]
    return cur, count


def onAdd(self):
    conn = sqlite3.connect('db_addressbook.db')
    with conn:
        cursor1 = conn.cursor()
        cursor2 = conn.cursor()
        cursor1.execute("""Select max(id) from tbl_addressbook order by id DESC""")
        self.bttn_clicks1 = cursor1.fetchone()[0]
        cursor2.execute("""Select min(id) from tbl_addressbook""")
        self.bttn_clicks2 = cursor2.fetchone()[0]
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # normalize the data to keep it consistent in the database
    var_fname = var_fname.strip()  # This will remove any blank spaces before and after the user's entry
    var_lname = var_lname.strip()
    var_fname = var_fname.title()  # This will ensure that the first character in each word is capitalized
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname, var_lname))  # combine our normailzed names into a fullname
    var_street = self.txt_street.get().strip()
    var_city = self.txt_city.get().strip()
    var_state = self.txt_state.get().strip()
    var_zip = self.txt_zip.get().strip()

    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_street) > 0) and (len(var_city) > 0) and (
            len(var_state) > 0) and (len(var_zip) > 0):
        conn = sqlite3.connect('db_addressbook.db')
        with conn:
            cursor = conn.cursor()

            # Check the database for existance of the fullname, if so we will alert user and disregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_addressbook WHERE col_fullname = '{}'""".format(
                var_fullname))  # ,(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0:  # if this is 0 then there is no existance of the fullname and we can add new data
                print("chkName: {}".format(chkName))
                cursor.execute(
                    """INSERT INTO tbl_addressbook (col_fname,col_lname,col_fullname,col_street,col_city,col_state,
                    col_zip) VALUES (?,?,?,?,?,?,?)""",
                    (var_fname, var_lname, var_fullname, var_street, var_city, var_state, var_zip))

            else:
                messagebox.showerror("Name Error",
                                     "'{}' already exists in the database! Please choose a different name.".format(
                                         var_fullname))
                onClear(self)  # call the function to clear all of the textboxes
            if (len(var_street) == 0) and (len(var_city) == 0) and (len(var_state) == 0) and (
                    len(var_zip) == 0):
                messagebox.showerror("Missing Text Error", "Please ensure that there is data in all four fields.")
        onClear(self)
        conn.commit()
        conn.close()


def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_street.delete(0, END)
    self.txt_city.delete(0, END)
    self.txt_state.delete(0, END)
    self.txt_zip.delete(0, END)


def onUpdate(self):
    conn = sqlite3.connect('db_addressbook.db')
    with conn:
        cursor1 = conn.cursor()
        cursor2 = conn.cursor()
        cursor1.execute("""Select max(id) from tbl_addressbook order by id DESC""")
        self.bttn_clicks1 = cursor1.fetchone()[0]
        cursor2.execute("""Select min(id) from tbl_addressbook""")
        self.bttn_clicks2 = cursor2.fetchone()[0]

    var_street = self.txt_street.get().strip()  # normalize the data to maintain database integrity
    var_city = self.txt_city.get().strip()
    var_state = self.txt_state.get().strip()
    var_zip = self.txt_zip.get().strip()
    var_fname = self.txt_fname.get().strip()
    var_lname = self.txt_lname.get().strip()
    var_fullname = ("{} {}".format(var_fname, var_lname))
    if (len(var_street) > 0) and (len(var_city) > 0) and (len(var_state) > 0) and (
            len(var_zip) > 0) and (len(var_fname) > 0) and (len(var_lname) > 0):  # ensure that there is data present
        conn = sqlite3.connect('db_addressbook.db')
        with conn:
            cur = conn.cursor()

            # count records to see if the user's changes are already in
            # the database...meaning, there are no changes to update.
            cur.execute("""SELECT COUNT(col_street) FROM tbl_addressbook WHERE col_street = '{}'""".format(var_street))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_city) FROM tbl_addressbook WHERE col_city = '{}'""".format(var_city))
            count2 = cur.fetchone()[0]
            print(count2)
            cur.execute("""SELECT COUNT(col_state) FROM tbl_addressbook WHERE col_state = '{}'""".format(var_state))
            count3 = cur.fetchone()[0]
            print(count3)
            cur.execute("""SELECT COUNT(col_zip) FROM tbl_addressbook WHERE col_zip = '{}'""".format(var_zip))
            count4 = cur.fetchone()[0]
            print(count4)

            if count == 0 or count2 == 0 or count3 == 0 or count4 == 0:
                # if proposed changes are not already in the database, then proceed
                response = messagebox.askokcancel("Update Request",
                                                  "The following changes ({}) and ({}) and ({}) and "
                                                  "({}) will be implemented "
                                                  "\n\nProceed with the update request?".format(

                                                      var_street, var_city, var_state, var_zip))
                print(response)
                if response:
                    conn = sqlite3.connect('db_addressbook.db')
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_addressbook SET col_street = '{0}',col_city = '{1}',col_state = 
                        '{2}', col_zip = '{3}' WHERE col_fullname='{4}'""".format(
                            var_street, var_city, var_state, var_zip, var_fullname))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request", "No changes have been made")
            else:
                messagebox.showinfo("No changes detected",
                                    "The updated information already exist in database.\n\nYour update request has "
                                    "been cancelled.")
            onClear(self)
        conn.close()

    onClear(self)


def onPrevious(self):
    self.bttn_clicks1 -= 1
    self.bttn_check1 += 1
    conn = sqlite3.connect('db_addressbook.db')
    with conn:
        cursor2 = conn.cursor()
        cursor2.execute("""Select min(id) from tbl_addressbook""")
        self.bttn_clicks2 = cursor2.fetchone()[0]

        cur2 = conn.cursor()
        cur2.execute("""Select max(id) from tbl_addressbook""")
        maxValue = cur2.fetchone()[0]
        if self.bttn_check1 == maxValue:
            messagebox.showerror("First Row Error", "This is the first record present in database.")
            self.bttn_check2 = 0
        elif self.bttn_check3 == 1 and self.bttn_check5 == 0:
            messagebox.showerror("Last Row Error", "This is the last record in the database.")
            self.bttn_check3 = 0
        else:

            conn = sqlite3.connect('db_addressbook.db')
            with conn:
                cursor = conn.cursor()

                cursor.execute("""SELECT * FROM tbl_addressbook WHERE ID=(?)""", [self.bttn_clicks1])
                varBody = cursor.fetchall()

                for data in varBody:
                    self.txt_fname.delete(0, END)
                    self.txt_fname.insert(0, data[1])
                    self.txt_lname.delete(0, END)
                    self.txt_lname.insert(0, data[2])
                    self.txt_street.delete(0, END)
                    self.txt_street.insert(0, data[4])
                    self.txt_city.delete(0, END)
                    self.txt_city.insert(0, data[5])
                    self.txt_state.delete(0, END)
                    self.txt_state.insert(0, data[6])
                    self.txt_zip.delete(0, END)
                    self.txt_zip.insert(0, data[7])
            self.lbl_first.configure(
                text='Current address index: {}  |  Number of addresses: {}'.format(self.bttn_clicks1,
                                                                                    maxValue))
            conn.close()


def onNext(self):
    self.bttn_clicks2 += 1
    self.bttn_check2 += 1
    self.bttn_check5 = 1
    conn = sqlite3.connect('db_addressbook.db')
    with conn:
        cursor1 = conn.cursor()
        cursor1.execute("""Select max(id) from tbl_addressbook order by id DESC""")
        self.bttn_clicks1 = cursor1.fetchone()[0]
        cur1 = conn.cursor()
        cur1.execute("""Select max(id) from tbl_addressbook""")
        maxValue = cur1.fetchone()[0]
        if self.bttn_check2 == maxValue:
            messagebox.showerror("Last Row Error", "This is the last record in the database.")
            self.bttn_check1 = 0
        elif self.bttn_check4 == 1:
            messagebox.showerror("Last Row Error", "This is the last record in the database.")
            self.bttn_check4 = 0
        else:
            conn = sqlite3.connect('db_addressbook.db')
            with conn:
                cursor = conn.cursor()
                cursor.execute("""SELECT * FROM tbl_addressbook WHERE ID=(?)""", [self.bttn_clicks2])
                varBody = cursor.fetchall()
                for data in varBody:
                    self.txt_fname.delete(0, END)
                    self.txt_fname.insert(0, data[1])
                    self.txt_lname.delete(0, END)
                    self.txt_lname.insert(0, data[2])
                    self.txt_street.delete(0, END)
                    self.txt_street.insert(0, data[4])
                    self.txt_city.delete(0, END)
                    self.txt_city.insert(0, data[5])
                    self.txt_state.delete(0, END)
                    self.txt_state.insert(0, data[6])
                    self.txt_zip.delete(0, END)
                    self.txt_zip.insert(0, data[7])
            self.lbl_first.configure(
                text='Current address index: {}  |  Number of addresses: {}'.format(self.bttn_clicks2,
                                                                                    maxValue))
            conn.close()


def onFirst(self):
    self.bttn_check2 = 0
    self.bttn_check3 = 1
    conn = sqlite3.connect('db_addressbook.db')
    with conn:
        cursor1 = conn.cursor()
        cursor2 = conn.cursor()
        cursor1.execute("""Select max(id) from tbl_addressbook order by id DESC""")
        self.bttn_clicks1 = cursor1.fetchone()[0]
        cursor2.execute("""Select min(id) from tbl_addressbook""")
        self.bttn_clicks2 = cursor2.fetchone()[0]

    conn = sqlite3.connect('db_addressbook.db')
    with conn:
        cursor = conn.cursor()

        cursor.execute(
            """SELECT col_fname,col_lname,col_street,col_city,col_state,col_zip FROM tbl_addressbook ORDER BY ID ASC 
            LIMIT 1""")
        varBody = cursor.fetchall()
        for data in varBody:
            self.txt_fname.delete(0, END)
            self.txt_fname.insert(0, data[0])
            self.txt_lname.delete(0, END)
            self.txt_lname.insert(0, data[1])
            self.txt_street.delete(0, END)
            self.txt_street.insert(0, data[2])
            self.txt_city.delete(0, END)
            self.txt_city.insert(0, data[3])
            self.txt_state.delete(0, END)
            self.txt_state.insert(0, data[4])
            self.txt_zip.delete(0, END)
            self.txt_zip.insert(0, data[5])
    self.lbl_first.configure(
        text='Current address index: {}  |  Number of addresses: {}'.format(self.bttn_clicks2, self.bttn_clicks1))
    conn.close()


def onLast(self):
    self.bttn_check1 = 0
    self.bttn_check4 = 1

    conn = sqlite3.connect('db_addressbook.db')
    with conn:
        cursor1 = conn.cursor()
        cursor2 = conn.cursor()
        cursor1.execute("""Select max(id) from tbl_addressbook order by id DESC""")
        self.bttn_clicks1 = cursor1.fetchone()[0]
        cursor2.execute("""Select min(id) from tbl_addressbook""")
        self.bttn_clicks2 = cursor2.fetchone()[0]

    conn = sqlite3.connect('db_addressbook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT col_fname,col_lname,col_street,col_city,col_state,col_zip FROM tbl_addressbook ORDER BY ID DESC 
            LIMIT 1""")
        varBody = cursor.fetchall()
        for data in varBody:
            self.txt_fname.delete(0, END)
            self.txt_fname.insert(0, data[0])
            self.txt_lname.delete(0, END)
            self.txt_lname.insert(0, data[1])
            self.txt_street.delete(0, END)
            self.txt_street.insert(0, data[2])
            self.txt_city.delete(0, END)
            self.txt_city.insert(0, data[3])
            self.txt_state.delete(0, END)
            self.txt_state.insert(0, data[4])
            self.txt_zip.delete(0, END)
            self.txt_zip.insert(0, data[5])
        self.lbl_first.configure(
            text='Current address index: {}  |  Number of addresses: {}'.format(self.bttn_clicks1, self.bttn_clicks1))
    conn.close()


if __name__ == "__main__":
    pass
