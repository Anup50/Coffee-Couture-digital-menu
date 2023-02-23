import sqlite3
import tkinter as tk
from tkinter import messagebox
import runpy
admin_conn = sqlite3.connect('admin.db')
admin_cursor = admin_conn.cursor()
# query to get the active user
active_user_query = "SELECT mail, fname, lname FROM users WHERE status = 1"
admin_cursor.execute(active_user_query)
# fetch the active user
active_user = admin_cursor.fetchone()
if active_user is None:
    messagebox.showerror("Error", "No active user found.")
    admin_conn.close()
    exit()
# create connection to orders.db to get the latest order for the active user
orders_conn = sqlite3.connect('orders.db')
orders_cursor = orders_conn.cursor()
# query to get the latest order for the active user
latest_order_query = "SELECT * FROM orders WHERE user_mail = ? ORDER BY timestamp DESC LIMIT 1"
orders_cursor.execute(latest_order_query, (active_user[0],))
# fetch the latest order for the active user
latest_order = orders_cursor.fetchone()
if latest_order is None:
    messagebox.showerror("Error", "No orders found for active user.")
    orders_conn.close()
    admin_conn.close()
    exit()
# close the database connections
orders_conn.close()
admin_conn.close()
# create billing GUI and display latest order for active user
root = tk.Tk()
root.title("Bill")
root.geometry("560x200+500+200")
root.resizable(False,False)
root.resizable(False,False)
root.iconbitmap('11.png')
root.config(bg="black")
# create labels for the latest order and active user
name_label = tk.Label(root, fg="white" ,bg="black",bd=0,text="Name:",font=('Arial Narrow', 15,'bold'))
name_label.grid(row=0, column=0)
name_value = tk.Label(root, fg="white" ,bg="black",bd=0,text=f"{active_user[1]} {active_user[2]}",font=('Arial Narrow', 15))
name_value.grid(row=0, column=1)
item_name_label = tk.Label(root,fg="white" ,bg="black",bd=0, text="Item Name",font=('Arial Narrow', 15,'bold'))
item_name_label.place(x=0,y=50)
item_name_value = tk.Label(root, bg="black",bd=0, fg="white",text=latest_order[2],font=('Arial Narrow', 15))
item_name_value.place(x=0,y=80)
quantity_label = tk.Label(root,bg="black",bd=0,fg="white" ,text="Quantity:",font=('Arial Narrow', 15,'bold'))
quantity_label.place(x=120,y=50)
quantity_value = tk.Label(root, bg="black",bd=0,fg="white",text=latest_order[3],font=('Arial Narrow', 15))
quantity_value.place(x=145, y=80)
price_label = tk.Label(root,bg="black",bd=0, fg="white" ,text="Price:",font=('Arial Narrow', 15,'bold'))
price_label.place(x=240,y=50)
price_value = tk.Label(root,bg="black",bd=0,fg="white", text=latest_order[4],font=('Arial Narrow', 15))
price_value.place(x=240,y=80)
total_price_label = tk.Label(root, bg="black",bd=0,fg="white" ,text="Total Price:",font=('Arial Narrow', 15,'bold'))
total_price_label.place(x=340,y=150)
total_price_value = tk.Label(root,bg="black",bd=0,fg="white" , text=latest_order[5],font=('Arial Narrow', 15))
total_price_value.place(x=440,y=150)
time_label = tk.Label(root,fg="white" ,bg="black",bd=0, text="Date/Time:",font=('Arial Narrow', 15,'bold'))
time_label.place(x=300,y=0)
time_value = tk.Label(root,bg="black",bd=0, fg="white" ,text=latest_order[6],font=('Arial Narrow', 15))
time_value.place(x=400,y=0)
root.mainloop()