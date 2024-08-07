from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

username=None

def databaseconnection():
    try:
        con=mysql.connector.connect(host='localhost', user='root',password='')
        cursor=con.cursor()
        return con,cursor
    except:
        messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')

def homepage():
    home=Tk()
    home.geometry("1920x1080+0+0")
    home.configure(bg='#101010')
    # home.resizable(False,False)
    home.title("MarkApp")
   

    def loggedin():
        global username
        username=user.get()
        if (user.get()=='Admin' or user.get()=='admin')  and (password.get()=='Admin' or password.get()=='admin'):
            con,cursor=databaseconnection()
            messagebox.showinfo('Success','Login Success')
            home.destroy()
            adminpage()
        if user.get()=='' or user.get()=='Enter Username'  or password.get()=='' or password.get()=='Enter Password':
            messagebox.showerror('Error','All fields required')

        else:
            con,cursor=databaseconnection()
            query=('use userdata')
            cursor.execute(query)
            query=('select * from data where username=%s and password=%s')
            cursor.execute(query,(user.get(),password.get()))
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid Username or password')
            else:
                messagebox.showinfo('Succuess','Login Success')
                con,cursor=databaseconnection()
                query=('use userdata')
                cursor.execute(query)
                query=('select s1,s2,s3,s4 from data where username=%s')
                cursor.execute(query,(user.get(),))
                mark=cursor.fetchone()
                if any(x is None for x in mark):
                    home.destroy()
                    dashboardstudentno()
                else:
                    home.destroy()
                    dashboardstudent()

    def signup():
        home.destroy()
        signuppage()

    img1 = ImageTk.PhotoImage(Image.open("Home TextureH.png"))
    canvas = customtkinter.CTkCanvas(home,bg='#101010',bd=0, highlightthickness=0)
    canvas.create_image(1920, 1080, image=img1)
    canvas.create_text(547, 245, text='Login',font=('Lexend Regular',25),fill='#8f00ff')
    canvas.create_text(665, 275, text='Welcome back! Please log in to access your account',font=('Lexend Light',10),fill='#656565')
    canvas.pack(fill='both', expand=True)
    frame = customtkinter.CTkFrame(master=home, width=500, height=480, fg_color="#101010")
    frame.pack_propagate(0)
    frame.place(x=0,y=0)

    logo=ImageTk.PhotoImage(file="MarkApp Logo.png")
    l2=customtkinter.CTkLabel(master=frame, image=logo, text=" ")

    l2.place(x=100,y=100)

    def on_enter(e):
        user.delete(0, 'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Enter Username')
   
    user=Entry(frame,width=32,fg='#656565',bg='#101010',border=0,font=('Lexend Light',11),insertbackground='#656565')
    user.place(x=100,y=200,)
    user.insert(0,'Enter Username')
    Frame(frame,width=310,height=1,bg='#656565').place(x=95,y=228)
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    def on_enter(e):
        password.delete(0, 'end')
        hide()
    def on_leave(e):
        name=password.get()
        if name=='':
            show()
            password.insert(0,'Enter Password')

    password=Entry(frame,width=32,fg='#656565',bg='#101010',border=0,font=('Lexend Light',11),insertbackground='#656565')
    password.place(x=100,y=280,)
    password.insert(0,'Enter Password')

    def hide():
        openeye.config(file='hidden.png')
        password.config(show='*')
        eyebutton.config(command=show)
    def show():
        openeye.config(file='eye.png')
        password.config(show='')
        eyebutton.config(command=hide)

    openeye=PhotoImage(file='eye.png')
    eyebutton=Button(frame,image=openeye,bd=0,bg='#101010',cursor='hand2',activebackground='#101010',command=hide)
    eyebutton.place(x=377,y=280)
    Frame(frame,width=310,height=1,bg='#656565').place(x=95,y=308)
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)

    login=customtkinter.CTkButton(frame,text='Login',font=('Lexend Regular',16),width=310,height=35,corner_radius=200,fg_color='#8f00ff',hover_color='#4F0260',command=loggedin)
    login.place(x=100,y=370)

    label1=Label(frame,text='Don’t have an account? ',font=('Lexend Light',10),background='#101010',fg='#656565')
    label1.place(x=100,y=420)
    button2=Button(frame,text='Register here',font=('Lexend Bold',10),bg='#101010',fg='#8f00ff',border=0,cursor='hand2',activebackground='#101010',command=signup)
    button2.place(x=249,y=416.75)

    home.mainloop()

def dashboardstudent():

    home=Tk()
    home.geometry("926x520+290+120")
    home.configure(bg='#101010')
    home.resizable(False,False)
    home.title("MarkApp")

    def logout():
        home.destroy()
        homepage()

    img1 = ImageTk.PhotoImage(Image.open("DefaultTexture.png"))
    canvas = customtkinter.CTkCanvas(home,bg='#101010',bd=0, highlightthickness=0)
    canvas.create_image(0, 0, image=img1, anchor=NW)
    canvas.pack(fill='both', expand=True)

    logo = ImageTk.PhotoImage(Image.open("MarkApp Logo.png"))
    canvas.create_image(880,474, image=logo, anchor=SE)

    login=customtkinter.CTkButton(canvas,text='LogOut',font=('Lexend Bold',15),width=50,height=35,corner_radius=200,fg_color='#8f00ff',hover_color='#4F0260',command=logout)
    login.place(x=610,y=423)
    canvas.create_text(720,455, text='|', anchor=SE,font=('Lexend Light',15),fill='#fff')
    Hi=Label(canvas,text='Hi,',font=('Lexend Light',30),fg='#656565',bg='#101010')
    Hi.place(x=70,y=70)

    Hi=Label(canvas,text=username,font=('Lexend Regular',30),fg='#8f00ff',bg='#101010')
    Hi.place(x=125,y=70)

    frame = customtkinter.CTkFrame(canvas, corner_radius=30, fg_color='#8f00ff',width=410,height=180,bg_color='#101010',border_width=0)
    frame.place(x=70,y=170)

    con, cursor = databaseconnection()
    cursor.execute('use userdata')
    query = ('SELECT rank FROM (SELECT username, ROW_NUMBER() OVER (ORDER BY (s1 + s2 + s3 + s4) DESC, s1 DESC) as rank FROM data) as rank WHERE username=%s;')
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    rankvar = result[0]

    rank = Label(frame, text=rankvar, font=('Lexend Bold', 50), fg='#fff', bg='#8f00ff')

    yourrank=Label(frame,text='Your Rank',font=('Lexend Medium',30),fg='#fff',bg='#8f00ff',)
    rank.place(x=39,y=54,)
    yourrank.place(x=39,y=15)

    tabview=customtkinter.CTkTabview(canvas,width=520,height=125,corner_radius=30,segmented_button_selected_color='#8f00ff',segmented_button_selected_hover_color='#4F0260')
    tabview.place(x=70,y=350,)

    tabview.add('Subject 1')
    tabview.add('Subject 2')
    tabview.add('Subject 3')
    tabview.add('Subject 4')
    tabview.add('Total')
    tabview._segmented_button.grid(sticky="W")

    def fetchdetails(username):
        con,cursor=databaseconnection()
        cursor.execute('use userdata')
        query=('select s1,s2,s3,s4 from data where username=%s')
        cursor.execute(query,(username,))
        result=cursor.fetchone()
        return result

    result=fetchdetails(username)

    def grade(mark):
        if mark>90:
            return 'A'
        elif mark>80:
            return 'B'
        elif mark>70:
            return 'C'
        elif mark>60:
            return 'D'
        elif mark>=50:
            return 'E'
        elif mark<50:
            return 'Failed'

    def gradetotal(mark):
        if mark>360:
            return 'A'
        elif mark>320:
            return 'B'
        elif mark>280:
            return 'C'
        elif  mark>240:
            return 'D'
        elif mark>=200:
            return 'E'
        elif mark<200:
            return 'Failed'

    pass0=result[0]
    grade0=grade(pass0)

    pass1=result[1]
    grade1=grade(pass1)

    pass2=result[2]
    grade2=grade(pass2)

    pass3=result[3]
    grade3=grade(pass3)

    total=sum(result)
    total_grade=gradetotal(total)

    sub1=customtkinter.CTkLabel(master=tabview.tab('Subject 1'),text=f'Mark : {result[0]}/100 | Grade : {grade0}',font=('Lexend Medium',20))
    sub1.place(x=20,y=-10)

    sub1=customtkinter.CTkLabel(master=tabview.tab('Subject 2'),text=f'Mark : {result[1]}/100 | Grade : {grade1}',font=('Lexend Medium',20))
    sub1.place(x=20,y=-10)

    sub1=customtkinter.CTkLabel(master=tabview.tab('Subject 3'),text=f'Mark : {result[2]}/100 | Grade : {grade2}',font=('Lexend Medium',20))
    sub1.place(x=20,y=-10)

    sub1=customtkinter.CTkLabel(master=tabview.tab('Subject 4'),text=f'Mark : {result[3]}/100 | Grade : {grade3}',font=('Lexend Medium',20))
    sub1.place(x=20,y=-10)

    sub1=customtkinter.CTkLabel(master=tabview.tab('Total'),text=f'Total Marks : {total}/400 | Grade : {total_grade}',font=('Lexend Medium',20))
    sub1.place(x=20,y=-10)

    home.mainloop()

def signuppage():
    home=Tk()
    home.geometry("926x520+290+120")
    home.configure(bg='#101010')
    home.resizable(False,False)
    home.title("MarkApp")

    def Sign():
        home.destroy()
        homepage()
        
    def user_validation():
        if user.get()==''or user.get()=='Enter Username' or password.get()=='' or password.get()=='Enter Password' or confpassword.get()=='' or confpassword.get()=='Confirm Password':
            messagebox.showerror('Error!','All Fields Required')
        elif password.get()!=confpassword.get():
            messagebox.showerror('Error!','The password and confirmation password should be same')
        else:
            con,cursor=databaseconnection()
            try:
                query='CREATE DATABASE userdata'
                cursor.execute(query)
                query='USE userdata'
                cursor.execute(query)
                query='create table data(username varchar(50) primary key not null,rollno int,password varchar(20),s1 int,s2 int,s3 int,s4 int)'
                cursor.execute(query)
            except:
                query='USE userdata'
                cursor.execute(query)
            
            query = 'SELECT * FROM data WHERE username=%s or rollno=%s'
            cursor.execute(query, (user.get(),rolno.get()))  # Notice the comma after user.get()

            row = cursor.fetchone()
            if row is not None:
                messagebox.showerror('Error', 'The username or roll number you entered already exists')

            else:
                query='insert into data(username,rollno,password) values(%s,%s,%s)'
                cursor.execute(query,(user.get(),rolno.get(),password.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Registration Successful')
                Sign()

    img1 = ImageTk.PhotoImage(Image.open("Home TextureQ.png"))
    canvas = customtkinter.CTkCanvas(home,bg='#101010',bd=0, highlightthickness=0)
    canvas.create_image(0, 0, image=img1, anchor=NW)

    canvas.pack(fill='both', expand=True)
   
    frame = customtkinter.CTkFrame(master=home, width=500, height=480, fg_color="#101010")
    frame.pack_propagate(0)
    frame.place(relx=0.5,rely=0.5,anchor='center')


    logo=ImageTk.PhotoImage(file="MarkApp Logo.png")
    l2=customtkinter.CTkLabel(master=frame, image=logo, text=" ")

    l2.place(relx=0.5,rely=0.16,anchor='center')

    wlo=Label(frame,text='Create Your Account',font=('Lexend Regular',14),fg='#c2c2c2',bg='#101010')
    wlo.place(relx=0.5,rely=0.27,anchor='center')

    def on_enter(e):
        rolno.delete(0, 'end')

    def on_leave(e):
        name = rolno.get()
        if name == '':
            rolno.insert(0, 'Enter Roll Number')

    rolno = Entry(frame, width=32, fg='#656565', bg='#101010', border=0, font=('Lexend Light', 11),
                 insertbackground='#656565')
    rolno.place(x=100, y=160)
    rolno.insert(0, 'Enter Roll Number')
    Frame(frame, width=310, height=1, bg='#656565').place(x=95, y=188)
    rolno.bind('<FocusIn>', on_enter)
    rolno.bind('<FocusOut>', on_leave)

    def on_enter(e):
        user.delete(0, 'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Enter Username')
    user=Entry(frame,width=32,fg='#656565',bg='#101010',border=0,font=('Lexend Light',11),insertbackground='#656565')
    user.place(x=100,y=220)
    user.insert(0,'Enter Username')
    Frame(frame,width=310,height=1,bg='#656565').place(x=95,y=250)
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    def on_enter(e):
        password.delete(0, 'end')
    def on_leave(e):
        name=password.get()
        if name=='':
            password.insert(0,'Enter Password')
    password=Entry(frame,width=32,fg='#656565',bg='#101010',border=0,font=('Lexend Light',11),insertbackground='#656565')
    password.place(x=100,y=280,)
    password.insert(0,'Enter Password')
    Frame(frame,width=310,height=1,bg='#656565').place(x=95,y=308)
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)

    def on_enter(e):
        confpassword.delete(0, 'end')
    def on_leave(e):
        name=confpassword.get()
        if name=='':
            confpassword.insert(0,'Confirm Password')
    confpassword=Entry(frame,width=32,fg='#656565',bg='#101010',border=0,font=('Lexend Light',11),insertbackground='#656565')
    confpassword.place(x=100,y=338,)
    confpassword.insert(0,'Confirm Password')
    Frame(frame,width=310,height=1,bg='#656565').place(x=95,y=366)
    confpassword.bind('<FocusIn>', on_enter)
    confpassword.bind('<FocusOut>', on_leave)

    login=customtkinter.CTkButton(frame,text='Sign Up',font=('Lexend Regular',16),width=310,height=35,corner_radius=200,fg_color='#8f00ff',hover_color='#4F0260',command=user_validation)
    login.place(x=100,y=388)

    label1=Label(frame,text='Already have an account?             .',font=('Lexend Light',10),background='#101010',fg='#656565')
    label1.place(relx=0.5,y=445,anchor='center')
    button2=Button(frame,text='Login here',font=('Lexend Bold',10),bg='#101010',fg='#8f00ff',border=0,cursor='hand2',activebackground='#101010',command=Sign)
    button2.place(x=305,y=428.5)

    home.mainloop()

def adminpage():

    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("blue")

    home=Tk()
    home.geometry("926x520+290+120")
    home.configure(bg='#101010')
    home.resizable(False,False)
    home.title("MarkApp")
    
    def logout():
        home.destroy()
        homepage()
        
    def fetchusername():  
        con,cursor=databaseconnection()
        query=('use userdata')
        cursor.execute(query)
        query=('select username from data where username <> "Admin"') 
        cursor.execute(query)
        results=cursor.fetchall()
        con.close()
        options=[result[0] for result in results]
        print(options)
        return options

    def fetchmarks():
        con,cursor=databaseconnection()
        query=('use userdata')
        cursor.execute(query)
        query = ('select s1,s2,s3,s4 from data where username= %s')
        cursor.execute(query, (selectedoption.get(),))
        mark = cursor.fetchone()
        return mark

    img1 = ImageTk.PhotoImage(Image.open("DefaultTexture.png"))
    canvas = customtkinter.CTkCanvas(home,bg='#101010',bd=0, highlightthickness=0)
    canvas.create_image(0, 0, image=img1, anchor=NW)
    canvas.pack(fill='both', expand=True)

    logo = ImageTk.PhotoImage(Image.open("MarkApp Logo.png"))
    canvas.create_image(880,474, image=logo, anchor=SE)

    login=customtkinter.CTkButton(canvas,text='LogOut',font=('Lexend Bold',15),width=50,height=35,corner_radius=200,fg_color='#8f00ff',hover_color='#4F0260',command=logout)
    login.place(x=610,y=423)
    canvas.create_text(720,455, text='|', anchor=SE,font=('Lexend Bold',15),fill='#fff')
    Hi=Label(canvas,text='Hi,',font=('Lexend Light',30),fg='#656565',bg='#101010')
    Hi.place(x=70,y=70)

    Hi=Label(canvas,text='Admin',font=('Lexend Regular',30),fg='#8f00ff',bg='#101010')
    Hi.place(x=125,y=70)

    frame1 = customtkinter.CTkFrame(canvas, corner_radius=30, fg_color='#2b2b2b',width=380,height=295,bg_color='#101010',border_width=0)
    frame1.place(x=70,y=170)

    addMark = Label(frame1, text='Add Mark (Out of 100)', font=('Lexend medium', 15), fg='#fff', bg='#2b2b2b')
    addMark.place(x=30, y=25)

    s1 = Label(frame1, text='Subject 1 :', font=('Lexend medium', 12), fg='#fff', bg='#2b2b2b')
    s1.place(x=30, y=105)
    s1entry=customtkinter.CTkEntry(frame1,width=220)
    s1entry.place(x=120, y=108)

    s2 = Label(frame1, text='Subject 2 :', font=('Lexend medium', 12), fg='#fff', bg='#2b2b2b')
    s2.place(x=30, y=140)
    s2entry=customtkinter.CTkEntry(frame1,width=220)
    s2entry.place(x=120, y=143)

    s3 = Label(frame1, text='Subject 3 :', font=('Lexend medium', 12), fg='#fff', bg='#2b2b2b')
    s3.place(x=30, y=175)
    s3entry=customtkinter.CTkEntry(frame1,width=220)
    s3entry.place(x=120, y=178)

    s4 = Label(frame1, text='Subject 4 :', font=('Lexend medium', 12), fg='#fff', bg='#2b2b2b')
    s4.place(x=30, y=210)
    s4entry=customtkinter.CTkEntry(frame1,width=220)
    s4entry.place(x=120, y=213)

    def call():
        try:
            marks = fetchmarks()
            entries = [s1entry, s2entry, s3entry, s4entry]
            for i in range(4):
                entries[i].delete(0, END)
                entries[i].insert(0, marks[i])
        except:
            for i in range(4):
                entries[i].delete(0, END)

    def update(s1,s2,s3,s4,username):
        try:
            if username=='Select Student':
                messagebox.showerror('Error','Select Student')
            elif all(0 <= int(mark) <= 100 for mark in [s1, s2, s3, s4]):
                con,cursor=databaseconnection()
                cursor.execute('use userdata')
                cursor.execute('update data set s1=%s,s2=%s,s3=%s,s4=%s where username=%s',(s1,s2,s3,s4,username))
                con.commit()
            else:
                messagebox.showerror('Error','Mark should be 100 or less')
        except:
            messagebox.showerror('Error','Please add all marks')
    options=fetchusername()
    selectedoption=StringVar(home)
    selectedoption.set('Select Student')
    selectmark=customtkinter.CTkOptionMenu(frame1,width=260,font=('Lexend medium', 15),corner_radius=25,fg_color='#8f00ff',button_color='#6303ac',button_hover_color='#4F0260',values=options,dropdown_font=('Lexend medium',12),variable=selectedoption,)
    selectmark.place(x=30, y=65)
    Go=customtkinter.CTkButton(frame1,width=38,fg_color='#8f00ff',text='GO',font=('Lexend medium', 10),corner_radius=38,hover_color='#4F0260',command=call)
    Go.place(x=300, y=65)
      
    def save():
        update(s1entry.get(),s2entry.get(),s3entry.get(),s4entry.get(),selectedoption.get())
        update_rank()
        
    scrollframe= customtkinter.CTkScrollableFrame(canvas,width=340,height=15,label_text='Rank List',label_font=('Lexend medium', 15),corner_radius=25,label_anchor='w',fg_color='#6303ac',label_fg_color='#8f00ff',scrollbar_button_color='#3b0267')
    scrollframe.place(x=500,y=70)
   
    def fetch_rank():
        con,cursor=databaseconnection()
        cursor.execute('use userdata')
        query=('SELECT ROW_NUMBER() OVER (ORDER BY (s1 + s2 + s3 + s4) DESC, s1 DESC) as rank, rollno,username,(s1 + s2 + s3 + s4) AS total_marks FROM data where username <> "Admin" AND s1 IS NOT NULL AND s2 IS NOT NULL AND s3 IS NOT NULL AND s4 IS NOT NULL')
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    def show_rank():
        values = fetch_rank()
        headings = ['Rank','Roll No.','Name','Total']
        for j in range(len(headings)):
            label = customtkinter.CTkLabel(scrollframe,font=('Lexend Bold', 16), text=headings[j])
            label.grid(row=0, column=j, padx=5, pady=1)  
        for i in range(len(values)):
            for j in range(len(values[i])):
                label = customtkinter.CTkLabel(scrollframe,font=('Lexend Light', 13),text=values[i][j])
                label.grid(row=i+1, column=j, padx=(30, 30), pady=(1, 1)) 

    def update_rank():
        values=fetch_rank()
        for widget in scrollframe.winfo_children():
            widget.destroy()
        headings = ['Rank','Roll No.','Name','Total']
        for j in range(len(headings)):
            label = customtkinter.CTkLabel(scrollframe,font=('Lexend Bold', 16), text=headings[j])
            label.grid(row=0, column=j, padx=5, pady=1)  
        for i in range(len(values)):
            for j in range(len(values[i])):
                label = customtkinter.CTkLabel(scrollframe,font=('Lexend Light', 13),text=values[i][j])
                label.grid(row=i+1, column=j, padx=(30, 30), pady=(1, 1)) 
    show_rank()
    save=customtkinter.CTkButton(frame1,width=50,fg_color='#8f00ff',text='Save',font=('Lexend medium', 12),corner_radius=25,hover_color='#4F0260',command=save)
    save.place(x=30, y=248)
    home.mainloop()
  
def dashboardstudentno():
    home=Tk()
    home.geometry("926x520+290+120")
    home.configure(bg='#101010')
    home.resizable(False,False)
    home.title("MarkApp")

    def logout():
        home.destroy()
        homepage()

    img1 = ImageTk.PhotoImage(Image.open("DefaultTexture.png"))
    canvas = customtkinter.CTkCanvas(home,bg='#101010',bd=0, highlightthickness=0)
    canvas.create_image(0, 0, image=img1, anchor=NW)
    canvas.pack(fill='both', expand=True)

    logo = ImageTk.PhotoImage(Image.open("MarkApp Logo.png"))
    canvas.create_image(880,474, image=logo, anchor=SE)

    login=customtkinter.CTkButton(canvas,text='LogOut',font=('Lexend Bold',15),width=50,height=35,corner_radius=200,fg_color='#8f00ff',hover_color='#4F0260',command=logout)
    login.place(x=610,y=423)
    canvas.create_text(720,455, text='|', anchor=SE,font=('Lexend Bold',15),fill='#fff')
    Hi=Label(canvas,text='Hi,',font=('Lexend Light',30),fg='#656565',bg='#101010')
    Hi.place(x=70,y=70)

    Hi=Label(canvas,text=username,font=('Lexend Regular',30),fg='#8f00ff',bg='#101010')
    Hi.place(x=125,y=70)

    frame = customtkinter.CTkFrame(canvas, corner_radius=30, fg_color='#8f00ff',width=410,height=180,bg_color='#101010',border_width=0)
    frame.place(x=70,y=170)

    rank = Label(frame, text='Result', font=('Lexend medium', 20), fg='#fff', bg='#8f00ff')
    yourrank = Label(frame, text='Not yet', font=('Lexend Medium', 20), fg='#fff', bg='#8f00ff',)
    yourrank2 = Label(frame, text='Published', font=('Lexend Medium', 20), fg='#fff', bg='#8f00ff',)

    rank.place(x=39, y=30)
    yourrank.place(x=39, y=65)  
    yourrank2.place(x=39, y=105)  


    tabview=customtkinter.CTkTabview(canvas,width=520,height=125,corner_radius=30,segmented_button_selected_color='#8f00ff',segmented_button_selected_hover_color='#c72796')
    tabview.place(x=70,y=350,)


    tabview.add('NA')
    tabview._segmented_button.grid(sticky="W")

    sub1=customtkinter.CTkLabel(master=tabview.tab('NA'),text='Sit Back and Relax',font=('Lexend Medium',20))
    sub1.place(x=20,y=-10)
    home.mainloop()

if __name__=="__main__":
    homepage()