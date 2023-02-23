from tkinter import *

 

from PIL import ImageTk, Image

 

import sqlite3

from tkinter import messagebox

import runpy

 

try:

    conn = sqlite3.connect('orders.db')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS orders

                    (id INTEGER PRIMARY KEY AUTOINCREMENT,

                    user_mail TEXT,

                    item_name TEXT,

                    quantity INTEGER,

                    price REAL,

                    total_price REAL,

                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')

 

    conn.commit()

    conn.close()

 

except:

    pass

 

def order_popup(item_name, item_price):

    popup = Toplevel()

    popup.title("Order")

    popup.geometry("300x200")

    popup.config(bg="#EEE3CB")

    popup.iconbitmap('billl.avif')

    popup.resizable(False,False)

    quantity = IntVar()

    quantity.set(1)

   

    price_label = Label(popup, text="Price: Rs" + str(item_price), bg="#EEE3CB",fg="black",font=("Bahnschrift", 14))

    price_label.pack(pady=10)

   

    quantity_label = Label(popup, text="Quantity:",bg="#EEE3CB",font=("Bahnschrift", 14))

    quantity_label.pack()

   

    quantity_spinbox = Spinbox(popup,from_=1, to=10, textvariable=quantity, font=("Bahnschrift", 14))

    quantity_spinbox.pack(pady=10)

   

    def update_price():

        price = item_price * quantity.get()

        price_label.config(text="Price: Rs" + str(price))

    def place_order():



        conn_orders = sqlite3.connect('orders.db')

        c_orders = conn_orders.cursor()

       


        order_data = (item_name, quantity.get(), item_price, item_price * quantity.get())

 



        conn_admin = sqlite3.connect('admin.db')

        c_admin = conn_admin.cursor()

       

    

        c_admin.execute("SELECT mail FROM users WHERE status = ?", (True,))

        email = c_admin.fetchone()[0]

       

      

        c_orders.execute('INSERT INTO orders (item_name, quantity, price, total_price, user_mail, timestamp) VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)', (item_name, quantity.get(), item_price, item_price * quantity.get(), email))

       

        # Commit and close the connections

        conn_orders.commit()

        conn_orders.close()

        conn_admin.close()

       

        # Close the popup window

        popup.destroy()

 

   

    order_button = Button(popup,cursor="hand2",bg="#967E76",text="Order",bd=0, width=12,font=("Helvetica", 14), command=place_order)

    order_button.pack(pady=10)

    quantity_spinbox.config(command=update_price)

   

    popup.mainloop()

 

coffee=Tk()

 

coffee.title("Coffee Couture")

 

coffee.configure(bg="black")

 

coffee.attributes('-fullscreen',TRUE)

 

def exittt():

    coffee.destroy()

    runpy.run_path("dash.py")

 

heading=Frame(coffee,bg="black",width=1700,height=40)

 

heading.place(x=0,y=38)

 



 

exit=Frame(coffee,bg="grey",width=1700,height=31)

 

exit.place(x=0,y=0)

 

title=Label(coffee,text="Coffee Couture",bg="black",bd=0,fg="antique white",font=("Britannic Bold",40))

 

title.place(x=610,y=40)

 

# welcome=Label(heading,text='" Indulge in the taste of happiness at our cafe "',bg="black",bd=0,fg="white",font=("Britannic Bold",25))

 

# coffee.iconbitmap('favicon.ico')

 

# welcome.place(x=440,y=0)

 

frame1=Frame(coffee,width=250,height=330,bg="white")

 

frame1.place(x=40,y=125)

 

frame2=Frame(coffee,width=250,height=330,bg="white")

 

frame2.place(x=340,y=125)

 

frame3=Frame(coffee,width=250,height=330,bg="white")

 

frame3.place(x=640,y=125)

 

frame4=Frame(coffee,width=250,height=330,bg="white")

 

frame4.place(x=940,y=125)

 

frame5=Frame(coffee,width=250,height=330,bg="white")

 

frame5.place(x=1240,y=125)

 

frame6=Frame(coffee,width=250,height=330,bg="white")

 

frame6.place(x=40,y=500)

 

frame7=Frame(coffee,width=250,height=330,bg="white")

 

frame7.place(x=340,y=500)

 

frame8=Frame(coffee,width=250,height=330,bg="white")

 

frame8.place(x=640,y=500)

 

frame9=Frame(coffee,width=250,height=330,bg="white")

 

frame9.place(x=940,y=500)

 

frame10=Frame(coffee,width=250,height=330,bg="white")

 

frame10.place(x=1240,y=500)

 

label1=Label(frame1,text="Cappuccino",fg="black",bd=0,bg="white",font=("Bahnschrift",16))

 

label1.place(x=70,y=230)

 

label2=Label(frame2,text="Macchiato",fg="black",bd=0,bg="white",font=("Bahnschrift",16))

 

label2.place(x=72,y=230)

 

label3=Label(frame3,text="Mocha",fg="black",bd=0,bg="white",font=("Bahnschrift",16))

 

label3.place(x=88,y=230)

 

label4=Label(frame4,text="Latte",fg="black",bd=0,bg="white",font=("Bahnschrift",16))

 

label4.place(x=88,y=230)

 

label5=Label(frame5,text="Americano",fg="black",bd=0,bg="white",font=("Bahnschrift",16))

 

label5.place(x=72,y=230)

 

label6=Label(frame6,text="Cold Brew",fg="black",bd=0,bg="white",font=("Bahnschrift",16))

 

label6.place(x=72,y=230)

 

label7=Label(frame7,text="Espresso",fg="black",bd=0,bg="white",font=("Bahnschrift",16))

 

label7.place(x=74,y=230)

 

label8=Label(frame8,text="Cortado",fg="black",bd=0,bg="white",font=("Bahnschrift",16))

 

label8.place(x=80,y=230)

 

label9=Label(frame9,text="Irish Coffee",fg="black",bd=0,bg="white",font=("Bahnschrift",16))

 

label9.place(x=68,y=230)

 

label10=Label(frame10,text="Flat White",fg="black",bd=0,bg="white",font=("Bahnschrift",16))

 

label10.place(x=70,y=230)

 

frame11=Frame(frame1,bg="#8D5524",bd=0,width=250,height=100)

 

frame11.place(x=0,y=260)

 

frame12=Frame(frame2,bg="#8D5524",bd=0,width=250,height=100)

 

frame12.place(x=0,y=260)

 

frame13=Frame(frame3,bg="#8D5524",bd=0,width=250,height=100)

 

frame13.place(x=0,y=260)

 

frame14=Frame(frame4,bg="#8D5524",bd=0,width=250,height=100)

 

frame14.place(x=0,y=260)

 

frame15=Frame(frame5,bg="#8D5524",bd=0,width=250,height=100)

 

frame15.place(x=0,y=260)

 

frame16=Frame(frame6,bg="#8D5524",bd=0,width=250,height=100)

 

frame16.place(x=0,y=260)

 

frame17=Frame(frame7,bg="#8D5524",bd=0,width=250,height=100)

 

frame17.place(x=0,y=260)

 

frame18=Frame(frame8,bg="#8D5524",bd=0,width=250,height=100)

 

frame18.place(x=0,y=260)

 

frame19=Frame(frame9,bg="#8D5524",bd=0,width=250,height=100)

 

frame19.place(x=0,y=260)

 

frame20=Frame(frame10,bg="#8D5524",bd=0,width=250,height=100)

 

frame20.place(x=0,y=260)

 

price=Frame(frame1,bd=0,bg="#FDDDC7",width=70,height=25)

 

price.place(x=0,y=180)

 

logo1=Image.open('cappuccino.jpg')

 

coffee1=ImageTk.PhotoImage(logo1)

 

lbl1=Label(coffee,image=coffee1, bg="antique white").place(x=40,y=125)

 

pricelabel1=Label(frame1,text="Rs-250/",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",12))

 

pricelabel1.place(x=62,y=264)

 

pricelabel1=Label(frame1,text="Price :",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",13))

 

pricelabel1.place(x=4,y=263)

 

pricelabel2=Label(frame2,text="Rs-200/",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",12))

 

pricelabel2.place(x=62,y=264)

 

pricelabel2=Label(frame2,text="Price :",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",13))

 

pricelabel2.place(x=4,y=263)

 

pricelabel3=Label(frame3,text="Rs-400/",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",12))

 

pricelabel3.place(x=62,y=264)

 

pricelabel3=Label(frame3,text="Price :",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",13))

 

pricelabel3.place(x=4,y=263)

 

pricelabel4=Label(frame4,text="Rs-350/",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",12))

 

pricelabel4.place(x=62,y=264)

 

pricelabel4=Label(frame4,text="Price :",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",13))

 

pricelabel4.place(x=4,y=263)

 

pricelabel5=Label(frame5,text="Rs-450/",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",12))

 

pricelabel5.place(x=62,y=264)

 

pricelabel5=Label(frame5,text="Price :",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",13))

 

pricelabel5.place(x=4,y=263)

 

pricelabel6=Label(frame6,text="Rs-270/",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",12))

 

pricelabel6.place(x=62,y=264)

 

pricelabel6=Label(frame6,text="Price :",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",13))

 

pricelabel6.place(x=4,y=263)

 

pricelabel7=Label(frame7,text="Rs-350/",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",12))

 

pricelabel7.place(x=62,y=264)

 

pricelabel7=Label(frame7,text="Price :",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",13))

 

pricelabel7.place(x=4,y=263)

 

pricelabel8=Label(frame8,text="Rs-600/",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",12))

 

pricelabel8.place(x=62,y=264)

 

pricelabel8=Label(frame8,text="Price :",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",13))

 

pricelabel8.place(x=4,y=263)

 

pricelabel9=Label(frame9,text="Rs-220/",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",12))

 

pricelabel9.place(x=62,y=264)

 

pricelabel9=Label(frame9,text="Price :",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",13))

 

pricelabel9.place(x=4,y=263)

 

pricelabel10=Label(frame10,text="Rs-200/",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",12))

 

pricelabel10.place(x=62,y=264)

 

pricelabel10=Label(frame10,text="Price :",bg="#8D5524",fg="#50CAAD",font=("Arial Rounded MT Bold",13))

 

pricelabel10.place(x=4,y=263)

 

# quantity=Entry(frame1,bd=0)

 

# quantity.place(x=114,y=265,width=70,height=21)

 

# plus=Button(frame1,text='+',bg='white',cursor='hand2',bd=0,fg="Black",width=2,height=0)

 

# plus.place(x=90,y=265)

 

# minus=Button(frame1,text="-",bg='white',cursor='hand2',bd=0,fg="Black",width=2,height=0)

 

# minus.place(x=188,y=265)

 

order1=Button(frame1,text="Order",bg="#F7E092",bd=0,fg="Black",cursor='hand2',font=("Bahnschrift",11),width=20,height=0, command=lambda: order_popup("Cappuchino",250))

 

order1.place(x=50,y=295)

 

order2=Button(frame2,text="Order",bg="#F7E092",bd=0,fg="Black",cursor='hand2',font=("Bahnschrift",11),width=20,height=0, command=lambda: order_popup("Macchiato",200))

 

order2.place(x=50,y=295)

 

order3=Button(frame3,text="Order",bg="#F7E092",bd=0,fg="Black",cursor='hand2',font=("Bahnschrift",11),width=20,height=0, command=lambda: order_popup("Mocha",400))

 

order3.place(x=50,y=295)

 

order4=Button(frame4,text="Order",bg="#F7E092",bd=0,fg="Black",cursor='hand2',font=("Bahnschrift",11),width=20,height=0, command=lambda: order_popup("Latte",350))

 

order4.place(x=50,y=295)

 

order5=Button(frame5,text="Order",bg="#F7E092",bd=0,fg="Black",cursor='hand2',font=("Bahnschrift",11),width=20,height=0, command=lambda: order_popup("Americano",250))

 

order5.place(x=50,y=295)

 

order6=Button(frame6,text="Order",bg="#F7E092",bd=0,fg="Black",cursor='hand2',font=("Bahnschrift",11),width=20,height=0, command=lambda: order_popup("Cold Brew",270))

 

order6.place(x=50,y=295)

 

order7=Button(frame7,text="Order",bg="#F7E092",bd=0,fg="Black",cursor='hand2',font=("Bahnschrift",11),width=20,height=0, command=lambda: order_popup("Expresso",350))

 

order7.place(x=50,y=295)

 

order8=Button(frame8,text="Order",bg="#F7E092",bd=0,fg="Black",cursor='hand2',font=("Bahnschrift",11),width=20,height=0, command=lambda: order_popup("Cortado",600))

 

order8.place(x=50,y=295)

 

order9=Button(frame9,text="Order",bg="#F7E092",bd=0,fg="Black",cursor='hand2',font=("Bahnschrift",11),width=20,height=0, command=lambda: order_popup("Irish Coffee",220))

 

order9.place(x=50,y=295)

 

order10=Button(frame10,text="Order",bg="#F7E092",bd=0,fg="Black",cursor='hand2',font=("Bahnschrift",11),width=20,height=0, command=lambda: order_popup("Flat White",200))

 

order10.place(x=50,y=295)

 

logo2=Image.open('Macchiato.jpg')

 

coffee2=ImageTk.PhotoImage(logo2)

 

lbl2=Label(coffee,image=coffee2, bg="antique white").place(x=340,y=125)

 

logo3=Image.open('Mocha.jpg')

 

coffee3=ImageTk.PhotoImage(logo3)

 

lbl3=Label(coffee,image=coffee3, bg="antique white").place(x=640,y=125)

 

logo4=Image.open('Latte.jpg')

 

coffee4=ImageTk.PhotoImage(logo4)

 

lbl4=Label(coffee,image=coffee4, bg="antique white").place(x=940,y=125)

 

logo5=Image.open('Americano.jpg')

 

coffee5=ImageTk.PhotoImage(logo5)

 

lbl5=Label(coffee,image=coffee5, bg="antique white").place(x=1240,y=125)

 

logo6=Image.open('ColdBrew.jpg')

 

coffee6=ImageTk.PhotoImage(logo6)

 

lbl6=Label(coffee,image=coffee6, bg="antique white").place(x=40,y=500)

 

logo7=Image.open('Espresso.jpg')

 

coffee7=ImageTk.PhotoImage(logo7)

 

lbl7=Label(coffee,image=coffee7, bg="antique white").place(x=340,y=500)

 

logo8=Image.open('Cortado.png')

 

coffee8=ImageTk.PhotoImage(logo8)

 

lbl8=Label(coffee,image=coffee8, bg="antique white").place(x=640,y=500)

 

logo9=Image.open('IrishCoffee.jpg')

 

coffee9=ImageTk.PhotoImage(logo9)

 

lbl9=Label(coffee,image=coffee9, bg="antique white").place(x=940,y=500)

 

logo10=Image.open('FlatWhite.jpg')

 

coffee10=ImageTk.PhotoImage(logo10)

 

lbl10=Label(coffee,image=coffee10, bg="antique white").place(x=1240,y=500)

 

def on_closing():

 

    tata=Tk()

 

    tata.config(bg="#FAFAFA")

 

    tata.geometry("585x135+500+350")

 

    tata.overrideredirect(1)

 

    blablabla=Label(tata,text="Are you sure you want to leave menu?",bg="#FAFAFA",bd=0,fg="Black",font=("Bahnschrift",13))

 

    blablabla.place(x=10,y=40)

 

    button2=Button(tata,text="No",fg="black",bg='#D3D3D3',bd=0,cursor='hand2',width=7,command=tata.destroy,height=0,font=("Bahnschrift",14))

 

    button2.place(x=490,y=90)

 

    button2.bind("<Enter>",lambda event: button2.config(bg="#EDECE3"))

 

    button2.bind("<Leave>",lambda event: button2.config(bg="#D3D3D3"))

 

    button=Button(tata,text="Yes",fg="White",bg='grey',cursor='hand2',bd=0,width=7,command=quit,height=0,font=("Bahnschrift",14))

 

    button.place(x=390,y=90)

 

    button.bind("<Enter>",lambda event: button.config(bg="#D3D3D3"))

 

    button.bind("<Leave>",lambda event: button.config(bg="grey"))

 

    Frame1=Frame(tata,bg="grey",height=26,width=700)

 

    Frame1.place(x=0,y=0)

 

coffee.protocol(on_closing)

 

bye=Button(exit,bg="grey",text="X",fg="white",command=on_closing,bd=0,width=4,height=1,cursor='hand2',font=("Verdana",13))

 

bye.place(x=1490,y=0)

 

bye.bind("<Enter>",lambda event: bye.config(bg="red"))

 

bye.bind("<Leave>",lambda event: bye.config(bg="grey"))

image552=Image.open('left.png')

coff3552=ImageTk.PhotoImage(image552)

home552=Button(coffee,image=coff3552,command=exittt,cursor='hand2',bg="black",bd=0)

home552.place(x=30,y=45)

home552.bind("<Enter>",lambda event: home552.config(bg="antique white"))

home552.bind("<Leave>",lambda event: home552.config(bg="black"))

coffee.mainloop()