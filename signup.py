from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import runpy  
try:
    conn = sqlite3.connect('admin.db')
    mk = conn.cursor()
    mk.execute('''CREATE TABLE users
                 (fname text, lname text, mail text PRIMARY KEY, phone int, password text, status boolean)''')
    mk.execute('''CREATE TABLE admin
                 (fname text, lname text, mail text PRIMARY KEY, phone int, password text, status boolean)''')
    conn.commit()
    conn.close()
except:
    pass

 
conn = sqlite3.connect('admin.db')
c = conn.cursor()
c.execute("SELECT COUNT(*) FROM admin")
result = c.fetchone()[0]
if result == 0:
    data = ('Super', 'User', 'admin2@gmail.com', 9841888358, 'password123', False)
    conn.execute('INSERT INTO admin (fname, lname, mail, phone, password, status) VALUES (?, ?, ?, ?, ?, ?)', data)
    conn.commit()

conn.close()
def dashin():
    group.destroy()
    runpy.run_path("dash.py")
group=Tk()
group.configure(bg= "antique white")
group.title("Coffee Couture")
group.geometry("980x600+300+100")
group.resizable(False,False)
group.iconbitmap('favicon.ico')
# Main logo of our cafe
logo=Image.open('11.png')
team=ImageTk.PhotoImage(logo)
lbl=Label(group,image=team, bg="antique white").place(x=8,y=7)
FOnt=Label(lbl,text="Speciality | Sustainable | Smiles",fg='black',bg='antique white',font=('Arial Rounded MT Bold', 15))
FOnt.place(x=110,y=465)
FOnt2=Label(lbl,text="100% Nepali Arabica Beans",fg='black',bg='antique white',font=('Arial Rounded MT Bold', 15))
FOnt2.place(x=139,y=495)
frame=Frame(group,width=380,height=850,bg="antique white").place(x=580,y=70)
heading=Label(frame,text="Sign in",fg="Black",bg="antique white",font=('Arial Narrow', 28,'bold'))
heading.place(x=680,y=90)

 ######---------------------------For In and Out focus of email
def in_enter1(e):
    entry.delete(0,END)

def in_leave1(e):
    name=entry.get()
    if name=='':
        entry.insert(0,'Email Address')
        entry.config(fg="AntiqueWhite4")
entry=Entry(frame,fg="AntiqueWhite4",border=0,bg='antique white',font=('Microsoft YaHei UI Light', 12,'bold'))
entry.place(x=603,y=186)
entry.insert(0,'Email Address')
entry.bind('<FocusIn>',in_enter1)
entry.bind('<FocusOut>',in_leave1)
Frame(frame,width=285,height=2,bg='black').place(x=600,y=209)
######------------------for changing user's entry config
def email_change_font(event):
    if entry.get() != "Email Address":
        entry.config(font=("Bahnschrift", 14),fg="Black")
entry.bind("<Key>",email_change_font)
######-----------------For In and Out focus of password in email address
def in_enter(e):
    secnd.delete(0,END)
def in_leave(e):
    name=secnd.get()
    if name=='':
        secnd.insert(0,'Password')
        secnd.config(fg="AntiqueWhite4")
secnd=Entry(frame,fg="AntiqueWhite4",border=0,bg='antique white',font=('Microsoft YaHei UI Light', 12,'bold'))
secnd.place(x=603,y=253)
secnd.insert(0,'Password')
secnd.bind('<FocusIn>',in_enter)
secnd.bind('<FocusOut>',in_leave)
######------------------------- for changing user's entry config in password
Frame(frame,width=285,height=2,bg='black').place(x=600,y=277)
def password_change_font(event):
    if secnd.get() != "Password":
        secnd.config(font=("Bahnschrift", 14),fg="Black")
secnd.bind("<Key>",password_change_font)    
#-----------------------------------------------------------------------------
def login():
    conn = sqlite3.connect('admin.db')
    c = conn.cursor()
    mail = entry.get()
    password = secnd.get()
    if (mail=="" or mail=="Email Address") or (password=="" or password=="Password"):
        messagebox.showerror("Error","One or More Fields Empty.")
    elif "@" and ".com" not in mail:
        messagebox.showerror("Error","Invalid Email")
    elif len(password)<7:
        messagebox.showerror("Error","Password must be more than 7 characters")
    else:
        c.execute("SELECT * FROM users WHERE mail=? AND password=?", (mail, password))
        user_result = c.fetchone()
        c.execute("SELECT * FROM admin WHERE mail=? AND password=?", (mail, password))
        admin_result = c.fetchone()
        if user_result or admin_result:
            if user_result:
                c.execute("UPDATE users SET status=? WHERE mail=? AND password=?", (True, mail, password))
            elif admin_result:
                c.execute("UPDATE admin SET status=? WHERE mail=? AND password=?", (True, mail, password))
            conn.commit()
            conn.close() 
            messagebox.showinfo("Success", "You have successfully logged in!")
            dashin()
        else:
            conn.close() # Close the database connection
            messagebox.showerror("Error", "Invalid login credentials. Please try again.")

 #####----------------------------Dont have an account/ SIgn in
btn=Button(frame,width=40,pady=9,text='Sign in',bg='#C18A81',cursor='hand2',fg='white',border=0, command=login).place(x=600,y=295)
lbl=Label(frame,text="Don't have an account?",fg='black',bg='antique white',font=('Microsoft YaHei UI Light', 11,'bold'))
lbl.place(x=600,y=340)
#####-----------------------------------------------Eye button
def hide():
    eyeclose1.config(file="close.png")
    if secnd.get() != "Password":    
        secnd.config(show="*")

 

    eyebutton.config(command=show,bg="antique white")

 

def show():

 

    eyeclose1.config(file="open.png")

 

    secnd.config(show="")

 

    eyebutton.config(command=hide,bg="antique white")

 

eyeclose1=PhotoImage(file="open.png")

 

eyebutton=Button(frame,image=eyeclose1,border=0,command=hide,activebackground="antique white",bg="antique white",cursor="hand2")

 

eyebutton.place(x=860,y=254)

 

##########################################################################

 

def signinnn():

 

        frame=Frame(group,width=380,height=850,bg="antique white").place(x=580,y=70)

 

        heading=Label(frame,text="Sign in",fg="Black",bg="antique white",font=('Arial Narrow', 28,'bold'))

 

        heading.place(x=680,y=90)

 

        ######---------------------------For In and Out focus of email

 

        def in_enter1(e):

 

            entry.delete(0,END)

 

        def in_leave1(e):

 

            name=entry.get()

 

            if name=='':

 

                entry.insert(0,'Email Address')

 

                entry.config(fg="AntiqueWhite4")

 

        entry=Entry(frame,fg="AntiqueWhite4",border=0,bg='antique white',font=('Microsoft YaHei UI Light', 12,'bold'))

 

        entry.place(x=603,y=186)

 

        entry.insert(0,'Email Address')

 

        entry.bind('<FocusIn>',in_enter1)

 

        entry.bind('<FocusOut>',in_leave1)

 

        Frame(frame,width=285,height=2,bg='black').place(x=600,y=209)

 

        ######------------------for changing user's entry config

 

        def email_change_font(event):

 

            if entry.get() != "Email Address":

 

                entry.config(font=("Bahnschrift", 14),fg="Black")

 

        entry.bind("<Key>",email_change_font)

 

        ######-----------------For In and Out focus of password in email address

 

 

 

        def in_enter(e):

 

            secnd.delete(0,END)

 

        def in_leave(e):

 

            name=secnd.get()

 

            if name=='':

 

                secnd.insert(0,'Password')

 

                secnd.config(fg="AntiqueWhite4")

 

        secnd=Entry(frame,fg="AntiqueWhite4",border=0,bg='antique white',font=('Microsoft YaHei UI Light', 12,'bold'))

 

        secnd.place(x=603,y=253)

 

        secnd.insert(0,'Password')

 

        secnd.bind('<FocusIn>',in_enter)

 

        secnd.bind('<FocusOut>',in_leave)

 

 

 

        ######------------------------- for changing user's entry config in password

 

        Frame(frame,width=285,height=2,bg='black').place(x=600,y=277)

 

        def password_change_font(event):

 

            if secnd.get() != "Password":

 

                secnd.config(font=("Bahnschrift", 14),fg="Black")

 

        secnd.bind("<Key>",password_change_font)    

 

 

 

        #####----------------------------Dont have an account/ SIgn up

 

        btn=Button(frame,width=40,pady=9,text='Sign in',bg='#C18A81',cursor='hand2',fg='white',border=0)

 

        btn.place(x=600,y=295)

 

        lbl=Label(frame,text="Don't have an account?",fg='black',bg='antique white',font=('Microsoft YaHei UI Light', 11,'bold'))

 

        lbl.place(x=600,y=340)

 

        #####-----------------------------------------------Eye button

 

        def hide():

 

            eyeclose1.config(file="close.png")

 

            if secnd.get() != "Password":    

 

                secnd.config(show="*")

 

            eyebutton.config(command=show,bg="antique white")

 

        def show():

 

            eyeclose1.config(file="open.png")

 

            secnd.config(show="")

 

            eyebutton.config(command=hide,bg="antique white")

 

        eyeclose1=PhotoImage(file="open.png")

 

        eyebutton=Button(frame,image=eyeclose1,border=0,command=hide,activebackground="antique white",bg="antique white",cursor="hand2")

 

        eyebutton.place(x=860,y=254)

 

        signup=Button(frame,text='Sign up',command=signupp,fg='sky blue',bg='antique white',cursor='hand2',font=('Microsoft YaHei UI Light', 11,'bold'),border=0)

 

        signup.place(x=785,y=338)

 

def signupp():

 

    frame00=Frame(group,width=380,height=450,bg="antique white").place(x=580,y=70)

 

    heading9=Label(frame00,text="Sign up",fg="Black",bg="antique white",font=('Arial Narrow', 28,'bold'))

 

    heading9.place(x=680,y=60)

 

 

 

    def in_enter100(e):

 

        entry22.delete(0,END)

 

    def in_leave100(e):

 

        name11=entry22.get()

 

        if name11=='':

 

            entry22.insert(0,'First name')

 

            entry22.config(fg="AntiqueWhite4")

 

    entry22=Entry(frame00,fg="AntiqueWhite4",border=0,bg='antique white',font=('Microsoft YaHei UI Light', 12,'bold'))

 

    entry22.place(x=603,y=165)

 

    entry22.insert(0,'First name')

 

    entry22.bind('<FocusIn>',in_enter100)

 

    entry22.bind('<FocusOut>',in_leave100)

 

    Frame(frame00,width=155,height=2,bg='black').place(x=600,y=188)

 

    ######------------------for changing user's entry config

 

    def email_change_font90(event):

 

        if entry22.get() != "First name":

 

            entry22.config(font=("Bahnschrift", 14),fg="Black")

 

    entry22.bind("<Key>",email_change_font90)

 

    ###################################

 

    def in_enter10011(e):

 

        entry221.delete(0,END)

 

    def in_leave10011(e):

 

        name111=entry221.get()

 

        if name111=='':

 

            entry221.insert(0,'Last name')

 

            entry221.config(fg="AntiqueWhite4")

 

    entry221=Entry(frame00,fg="AntiqueWhite4",border=0,bg='antique white',font=('Microsoft YaHei UI Light', 12,'bold'))

 

    entry221.place(x=783,y=165)

 

    entry221.insert(0,'Last name')

 

    entry221.bind('<FocusIn>',in_enter10011)

 

    entry221.bind('<FocusOut>',in_leave10011)

 

    Frame(frame00,width=155,height=2,bg='black').place(x=780,y=188)

 

    ######------------------for changing user's entry config

 

    def email_change_font9071(event):

 

        if entry221.get() != "Last name":

 

            entry221.config(font=("Bahnschrift", 14),fg="Black")

 

    entry221.bind("<Key>",email_change_font9071)

 

    ######-----------------For In and Out focus of password in email address

 

 

 

    def in_enter111(e):

 

        secnd23.delete(0,END)

 

    def in_leave111(e):

 

        name55=secnd23.get()

 

        if name55=='':

 

            secnd23.insert(0,'Email')

 

            secnd23.config(fg="AntiqueWhite4")

 

    secnd23=Entry(frame00,fg="AntiqueWhite4",border=0,bg='antique white',font=('Microsoft YaHei UI Light', 12,'bold'))

 

    secnd23.place(x=603,y=223)

 

    secnd23.insert(0,'Email')

 

    secnd23.bind('<FocusIn>',in_enter111)

 

    secnd23.bind('<FocusOut>',in_leave111)

 

 

 

    ######------------------------- for changing user's entry config in password

 

    Frame(frame00,width=285,height=2,bg='black').place(x=600,y=247)

 

    def password_change_font23(event):

 

        if secnd23.get() != "Email":

 

            secnd23.config(font=("Bahnschrift", 14),fg="Black")

 

    secnd23.bind("<Key>",password_change_font23)

 

    #-----------------------------------------------------

 

    def in_enter3(e):

 

        entry5.delete(0,END)

 

    def in_leave3(e):

 

        name34=entry5.get()

 

        if name34=='':

 

            entry5.insert(0,'Create password')

 

            entry5.config(fg="AntiqueWhite4")

 

    entry5=Entry(frame00,fg="AntiqueWhite4",border=0,bg='antique white',font=('Microsoft YaHei UI Light', 12,'bold'))

 

    entry5.place(x=603,y=359)

 

    entry5.insert(0,'Create password')

 

    entry5.bind('<FocusIn>',in_enter3)

 

    entry5.bind('<FocusOut>',in_leave3)

 

    Frame(frame00,width=285,height=2,bg='black').place(x=600,y=383)

 

    ######------------------for changing user's entry config

 

    def email_change_font4(event):

 

        if entry5.get() != "Create password":

 

            entry5.config(font=("Bahnschrift", 14),fg="Black")

 

    entry5.bind("<Key>",email_change_font4)  

 

    def hide3():

 

        eyeclose1.config(file="close.png")

 

        if entry5.get() != "Create password":

 

            entry5.config(show="*")

 

        eyebutton.config(command=show3,bg="antique white")

 

    def show3():

 

        eyeclose1.config(file="open.png")

 

        entry5.config(show="")

 

        eyebutton.config(command=hide3,bg="antique white")

 

    eyeclose1=PhotoImage(file="open.png")

 

    eyebutton=Button(frame00,image=eyeclose1,border=0,command=hide3,activebackground="antique white",bg="antique white",cursor="hand2")

 

    eyebutton.place(x=860,y=360)

 

    def in_enter4(e):

 

        entry6.delete(0,END)

 

    def in_leave4(e):

 

        name1=entry6.get()

 

        if name1=='':

 

            entry6.insert(0,'Contact no.')

 

            entry6.config(fg="AntiqueWhite4")

 

    entry6=Entry(frame00,fg="AntiqueWhite4",border=0,bg='antique white',font=('Microsoft YaHei UI Light', 12,'bold'))

 

    entry6.place(x=603,y=290)

 

    entry6.insert(0,'Contact no.')

 

    entry6.bind('<FocusIn>',in_enter4)

 

    entry6.bind('<FocusOut>',in_leave4)

 

    Frame(frame00,width=285,height=2,bg='black').place(x=600,y=315)

 

    ######------------------for changing user's entry config

 

    def email_change_font6(event):

 

        if entry6.get() != "Contact no.":

 

            entry6.config(font=("Bahnschrift", 14),fg="Black")

 

    entry6.bind("<Key>",email_change_font6)

 

    ###-------------------------------

 

    def in_enter5(e):

 

        entry7.delete(0,END)

 

    def in_leave5(e):

 

        name3=entry7.get()

 

        if name3=='':

 

            entry7.insert(0,'Confirm Password')

 

            entry7.config(fg="AntiqueWhite4")

 

    entry7=Entry(frame00,fg="AntiqueWhite4",border=0,bg='antique white',font=('Microsoft YaHei UI Light', 12,'bold'))

 

    entry7.place(x=603,y=428)

 

    entry7.insert(0,'Confirm password')

 

    entry7.bind('<FocusIn>',in_enter5)

 

    entry7.bind('<FocusOut>',in_leave5)

 

    Frame(frame00,width=285,height=2,bg='black').place(x=600,y=452)

 

    ######------------------for changing user's entry config

 

    def email_change_font7(event):

 

        if entry7.get() != "Confirm password":

 

            entry7.config(font=("Bahnschrift", 14),fg="Black")

 

    entry7.bind("<Key>",email_change_font7)

 

    ###-----------------------------------------------

 

    def hide5():

 

        eyeclose5.config(file="close.png")

 

        if entry7.get() != "Confirm password":

 

            entry7.config(show="*")

 

        eyebutton00.config(command=show5,bg="antique white")

 

    def show5():

 

        eyeclose5.config(file="open.png")

 

        entry7.config(show="")

 

        eyebutton00.config(command=hide5,bg="antique white")

 

    eyeclose5=PhotoImage(file="open.png")

 

    eyebutton00=Button(frame00,image=eyeclose5,border=0,command=hide5,activebackground="antique white",bg="antique white",cursor="hand2")

 

    eyebutton00.place(x=860,y=429)

 

    ####----------------------------Dont have an account/ SIgn up

    #verification and insert function

    def verify():

        a=entry22.get()

        last_name=entry221.get()

        b=secnd23.get()

        d=entry6.get()

        e=entry5.get()

        f=entry7.get()

 

        if (a=="" or a=="First Name") or (b=="" or b=="Email") or (last_name=="" or last_name=="Last Name") or (d=="" or d=="Phone Number") or (e=="" or e=="Create Password") or (f=="" or f=="Confirm Password"):

            messagebox.showerror("Error","One or More Fields Empty.")

        elif "@" and ".com" not in b:

            messagebox.showerror("Error","Invalid Email")

        elif len(f)<7 or len(e)<7:

            messagebox.showerror("Error","Password must be more than 7 characters")

        elif len(d)!=10:

            messagebox.showerror("Error","Invalid Phone Number Length")

        elif f!=e:

            messagebox.showerror("Error","Password Mismatched")

        else:

            conn=sqlite3.connect('admin.db')

            c=conn.cursor()

            c.execute("INSERT INTO users VALUES (:fname,:lname,:mail,:phone,:password, :status)",{

                'fname':a,

                'lname':last_name,

                'mail':b,

                'phone':d,

                'password':e,

                'status': False

            })

            conn.commit()

            conn.close()

            messagebox.showinfo("Success","Registration Successful!")

            signinnn()

 

    btn123=Button(frame00,width=40,pady=9,text='Sign up',bg='#C18A81',cursor='hand2',fg='white',border=0, command=verify)

 

    btn123.place(x=600,y=469)

 

    lbl123=Label(frame00,text="Already have an account?",fg='black',bg='antique white',font=('Microsoft YaHei UI Light', 11,'bold'))

 

    lbl123.place(x=600,y=512)

 

    signup22=Button(frame00,text='Sign in',command=signinnn,fg='sky blue',bg='antique white',cursor='hand2',font=('Microsoft YaHei UI Light', 11,'bold'),border=0)

 

    signup22.place(x=804,y=510)

 

signup=Button(frame,text='Sign up',command=signupp,fg='sky blue',bg='antique white',cursor='hand2',font=('Microsoft YaHei UI Light', 11,'bold'),border=0)

 

signup.place(x=785,y=338)

 

 

 

######################################################

 

######-----------------------------------------DO you wanna exit

 

def on_closing():

 

    exit=Tk()

 

    exit.config(bg="#FAFAFA")

 

    exit.geometry("585x135+500+350")

 

    exit.overrideredirect(1)

 

    blablabla=Label(exit,text="Are you sure you want to exit application?",bg="#FAFAFA",bd=0,fg="Black",font=("Bahnschrift",13))

 

    blablabla.place(x=10,y=40)

 

    exit.resizable(FALSE,FALSE)

 

    button=Button(exit,text="Yes",fg="White",bg='grey',cursor='hand2',bd=0,width=7,command=quit,height=0,font=("Bahnschrift",14))

 

    button.place(x=390,y=90)

 

    button.bind("<Enter>",lambda event: button.config(bg="#D3D3D3"))

 

    button.bind("<Leave>",lambda event: button.config(bg="grey"))

 

    button2=Button(exit,text="No",fg="black",bg='#D3D3D3',bd=0,cursor='hand2',width=7,command=exit.destroy,height=0,font=("Bahnschrift",14))

 

    button2.place(x=490,y=90)

 

    button=Button(exit,text="Yes",fg="White",bg='grey',cursor='hand2',bd=0,width=7,command=quit,height=0,font=("Bahnschrift",14))

 

    button.place(x=390,y=90)

 

    button.bind("<Enter>",lambda event: button.config(bg="#D3D3D3"))

 

    button.bind("<Leave>",lambda event: button.config(bg="grey"))

 

    button2.bind("<Enter>",lambda event: button2.config(bg="#EDECE3"))

 

    button2.bind("<Leave>",lambda event: button2.config(bg="#D3D3D3"))

 

    Frame1=Frame(exit,bg="grey",height=26,width=700)

 

    Frame1.place(x=0,y=0)

 

group.protocol("WM_DELETE_WINDOW", on_closing)

 

group.mainloop()