import tkinter as tk
import sqlite3
from tkinter import messagebox
def delete_user(mail):
    conn = sqlite3.connect('admin.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE mail=?", (mail,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "User deleted successfully!")

window = tk.Tk()
window.title("User Details")
listbox = tk.Listbox(window, width=80)
listbox.pack(padx=10, pady=10)
# Fetch user details from database and display them in the listbox
conn = sqlite3.connect('admin.db')
c = conn.cursor()
c.execute("SELECT * FROM users")
rows = c.fetchall()
for row in rows:
    fname, lname, mail, phone, password, status = row
    listbox.insert(tk.END, f"{fname} {lname} | {mail} | {phone} | {password} | {'Active' if status else 'Inactive'}")
# button to delete the selected user
def on_delete():
    # Get the selected item
    selection = listbox.curselection()
    if len(selection) == 0:
        messagebox.showerror("Error", "Please select a user to delete!")
        return
    item = listbox.get(selection[0])
    mail = item.split('|')[1].strip()
    # Confirm deletion
    result = messagebox.askyesno("Confirm", f"Are you sure you want to delete user {mail}?")
    if result:
        # Delete the user
        delete_user(mail)
        # Remove the item from the listbox
        listbox.delete(selection[0])
delete_button = tk.Button(window, text="Delete User", command=on_delete)
delete_button.pack(padx=10, pady=10)
window.mainloop()