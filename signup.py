from tkinter import *
from tkinter import messagebox
import customtkinter 
from PIL import Image, ImageTk
import mysql.connector



customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

home=Tk()
home.geometry("926x520+50+30")
home.configure(bg='#101010')
home.resizable(False,False)
home.title("MarkApp")

#####function
def Sign():
    home.destroy()
    import login
    
def connect_database():
    if user.get()==''or user.get()=='Enter Username' or password.get()=='' or password.get()=='Enter Password' or confpassword.get()=='' or confpassword.get()=='Confirm Password':
        messagebox.showerror('Error!','All Fields Required')
    elif password.get()!=confpassword.get():
        messagebox.showerror('Error!','The password and confirmation password should be same')
    else:
        try:
            con=mysql.connector.connect(host='localhost', user='root',password='')
            cursor=con.cursor()    
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return
        try:
            query='CREATE DATABASE userdata'
            cursor.execute(query)
            query='USE userdata'
            cursor.execute(query)
            query='create table data(username varchar(50) primary key not null,password varchar(20),s1 int,s2 int,s3 int,s4 int)'
            cursor.execute(query)
        except:
            query='USE userdata'
            cursor.execute(query)
        
        query = 'SELECT * FROM data WHERE username=%s'
        cursor.execute(query, (user.get(),))  # Notice the comma after user.get()

        row = cursor.fetchone()
        if row is not None:
            messagebox.showerror('Error', 'Username Already Exists')

        else:
            query='insert into data(username,password) values(%s,%s)'
            cursor.execute(query,(user.get(),password.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration Successful')
            Sign()

############
img1 = ImageTk.PhotoImage(Image.open("Home TextureQ.png"))
canvas = customtkinter.CTkCanvas(home,bg='#101010',bd=0, highlightthickness=0)
canvas.create_image(0, 0, image=img1, anchor=NW)

canvas.pack(fill='both', expand=True)
# l1=customtkinter.CTkLabel(master=home, image=img1, text=" ")
frame = customtkinter.CTkFrame(master=home, width=500, height=480, fg_color="#101010")
frame.pack_propagate(0)
frame.place(relx=0.5,rely=0.5,anchor='center')


logo=ImageTk.PhotoImage(file="MarkApp Logo.png")
l2=customtkinter.CTkLabel(master=frame, image=logo, text=" ")


l2.place(relx=0.5,rely=0.2,anchor='center')

wlo=Label(frame,text='Create Your Account',font=('Lexend Regular',14),fg='#c2c2c2',bg='#101010')
wlo.place(relx=0.5,rely=0.32,anchor='center')

#############################Username
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Enter Username')
user=Entry(frame,width=32,fg='#656565',bg='#101010',border=0,font=('Lexend Light',11),insertbackground='#656565')
user.place(x=100,y=190)
user.insert(0,'Enter Username')
Frame(frame,width=310,height=1,bg='#656565').place(x=95,y=220)
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


#############################Password
def on_enter(e):
    password.delete(0, 'end')
def on_leave(e):
    name=password.get()
    if name=='':
        password.insert(0,'Enter Password')
password=Entry(frame,width=32,fg='#656565',bg='#101010',border=0,font=('Lexend Light',11),insertbackground='#656565')
password.place(x=100,y=250,)
password.insert(0,'Enter Password')
Frame(frame,width=310,height=1,bg='#656565').place(x=95,y=278)
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

#############################confPassword
def on_enter(e):
    confpassword.delete(0, 'end')
def on_leave(e):
    name=confpassword.get()
    if name=='':
        confpassword.insert(0,'Confirm Password')
confpassword=Entry(frame,width=32,fg='#656565',bg='#101010',border=0,font=('Lexend Light',11),insertbackground='#656565')
confpassword.place(x=100,y=308,)
confpassword.insert(0,'Confirm Password')
Frame(frame,width=310,height=1,bg='#656565').place(x=95,y=336)
confpassword.bind('<FocusIn>', on_enter)
confpassword.bind('<FocusOut>', on_leave)

###################################

login=customtkinter.CTkButton(frame,text='Sign Up',font=('Lexend Regular',16),width=310,height=35,corner_radius=200,fg_color='#8f00ff',hover_color='#c72796',command=connect_database)
login.place(x=100,y=378)

###################################
label1=Label(frame,text='Already have an account?             .',font=('Lexend Light',10),background='#101010',fg='#656565')
label1.place(relx=0.5,y=435,anchor='center')
button2=Button(frame,text='Login here',font=('Lexend Bold',10),bg='#101010',fg='#8f00ff',border=0,cursor='hand2',activebackground='#101010',command=Sign)
button2.place(x=305,y=418.5)

home.mainloop()


