from tkinter import *

from PIL import ImageTk, Image

import runpy

def exittt():

    coffeee.destroy()

    runpy.run_path ("dash.py")

coffeee=Tk()

coffeee.title("Coffee Couture")

coffeee.configure(bg="black")

coffeee.attributes('-fullscreen',TRUE)

lo=Image.open('90.jpg')

teams=ImageTk.PhotoImage(lo)

lbls=Label(coffeee,image=teams,bg="black",bd=0).place(x=50,y=31)

logo3s=Image.open('op.jpg')

team3s=ImageTk.PhotoImage(logo3s)

lbl3s=Label(coffeee,image=team3s,bd=0,bg="#010203").place(x=660,y=2)

logo1s=Image.open('lol.png')

team1s=ImageTk.PhotoImage(logo1s)

lbl2s=Label(coffeee,image=team1s,bd=0,bg="#010203").place(x=765,y=140)

snns=Label(coffeee,text="ABOUT US :",fg="white",bg="black",bd=0,font=("Bahnschrift SemiBold",27))

snns.place(x=990,y=125)

snn2s=Label(coffeee,text="Thank you!!",fg="white",bg="black",bd=0,font=("Bahnschrift SemiBold",25))

snn2s.place(x=1000,y=725)

def on_closing():

    tata=Tk()

    tata.config(bg="#FAFAFA")

    tata.geometry("585x135+500+350")

    tata.overrideredirect(1)

    blablabla=Label(tata,text="Are you sure you want to exit application?",bg="#FAFAFA",bd=0,fg="Black",font=("Bahnschrift",13))

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

exitss=Frame(coffeee,bg="grey",width=1700,height=31)

exitss.place(x=0,y=0)

byes=Button(exitss,bg="grey",command=on_closing,text="X",fg="white",bd=0,width=4,height=1,cursor='hand2',font=("Verdana",13))

byes.place(x=1490,y=0)

byes.bind("<Enter>",lambda event: byes.config(bg="red"))

byes.bind("<Leave>",lambda event: byes.config(bg="grey"))

image552=Image.open('left.png')

coff3552=ImageTk.PhotoImage(image552)

home552=Button(coffeee,image=coff3552,command=exittt,cursor='hand2',bg="black",bd=0)

home552.place(x=30,y=45)

home552.bind("<Enter>",lambda event: home552.config(bg="antique white"))

home552.bind("<Leave>",lambda event: home552.config(bg="black"))

 

coffeee.mainloop()