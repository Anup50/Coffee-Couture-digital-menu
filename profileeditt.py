from tkinter import *
import sqlite3
from tkinter import messagebox
root = Tk()
root.title("User Details")
root.config(bg="black")
root.resizable(FALSE,FALSE)
root.geometry("320x300+600+200")

# create labels to display user details
fname_lbl = Label(root,fg="white",bg="black", text="First Name:",font=('Arial Rounded MT Bold', 15))
lname_lbl = Label(root, fg="white",bg="black",text="Last Name:",font=('Arial Rounded MT Bold', 15))
mail_lbl = Label(root,fg="white",bg="black", text="Email:",font=('Arial Rounded MT Bold', 15))
phone_lbl = Label(root, fg="white",bg="black",text="Phone:",font=('Arial Rounded MT Bold', 15))
password_lbl = Label(root,fg="white",bg="black", text="Password:",font=('Arial Rounded MT Bold', 15))
# create entry widgets for editing user details
fname_entry = Entry(root,width=20,font=('Arial Rounded MT Bold', 10))
lname_entry = Entry(root,width=20,font=('Arial Rounded MT Bold', 10))
phone_entry = Entry(root,width=20,font=('Arial Rounded MT Bold', 10))
password_entry = Entry(root,width=20,font=('Arial Rounded MT Bold', 10))

conn = sqlite3.connect('admin.db')
c = conn.cursor()
c.execute("SELECT * FROM users WHERE status=?", (True,))
user = c.fetchone()
conn.close()
# set default values for entry widgets
fname_entry.insert(END, user[0])
lname_entry.insert(END, user[1])
phone_entry.insert(END, user[3])
password_entry.insert(END, user[4])
# create label widget for displaying email
mail_val = StringVar(value=user[2])
mail_lbl_val = Label(root,textvariable=mail_val,width=20,font=('Arial Rounded MT Bold', 10))
# function to update user details in database
def update_user():
    fname = fname_entry.get()
    lname = lname_entry.get()
    phone = phone_entry.get()
    password = password_entry.get()
    if not fname or not lname or not phone or not password:
        messagebox.showerror("Error", "Please fill in all fields")
    elif len(phone) != 10 or not phone.isdigit():
        messagebox.showerror("Error", "Invalid phone number")
    elif len(password) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters")
    else:
        conn = sqlite3.connect('admin.db')
        c = conn.cursor()
        c.execute("UPDATE users SET fname=?, lname=?, phone=?, password=? WHERE mail=?",
                (fname, lname, phone, password, user[2]))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","User details updated!")
# function to clear default value on click
def clear_default(event):
    if event.widget.get() == event.widget.default_value:
        event.widget.delete(0, END)
# set default value for entry widgets
fname_entry.default_value = user[0]
lname_entry.default_value = user[1]
phone_entry.default_value = ""
password_entry.default_value = user[4]
# bind click event to clear default value
fname_entry.bind("<Button-1>", clear_default)
lname_entry.bind("<Button-1>", clear_default)
phone_entry.bind("<Button-1>", clear_default)
password_entry.bind("<Button-1>", clear_default)
# create button to update user details
update_btn = Button(root,width=20,fg="white", bg="red",font=('Arial Rounded MT Bold', 10),bd=0,text="Update", command=update_user)
# create label to display status message
status_lbl = Label(root, text="")
# place labels and entry widgets in grid
fname_lbl.grid(row=0, column=0, sticky=W)
lname_lbl.grid(row=1, column=0, sticky=W)
mail_lbl.grid(row=2, column=0, sticky=W)
phone_lbl.grid(row=3, column=0, sticky=W)
password_lbl.grid(row=4, column=0, sticky=W)
fname_entry.grid(row=0, column=1, padx=10, pady=10)
lname_entry.grid(row=1, column=1, padx=10, pady=10)
mail_lbl_val.grid(row=2, column=1, padx=10, pady=10)
phone_entry.grid(row=3, column=1, padx=10, pady=10)
password_entry.grid(row=4, column=1, padx=10, pady=10)
update_btn.grid(row=5, column=1, pady=10)
root.mainloop()