from tkinter import *
from tkinter import ttk
import customtkinter 
from PIL import Image, ImageTk
import mysql.connector
import customtkinter
from tkinter import messagebox

def databaseconnection():
    try:
        con=mysql.connector.connect(host='localhost', user='root',password='')
        cursor=con.cursor()
        return con,cursor
    except:
         messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')   


####WRAP FROM HERE 
def admin():
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("blue")

    home=Tk()
    home.geometry("926x520+50+30")
    home.configure(bg='#101010')
    home.resizable(False,False)
    home.title("MarkApp")
    
    def logout():
        home.destroy()
        

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

    login=customtkinter.CTkButton(canvas,text='LogOut',font=('Lexend Bold',15),width=50,height=35,corner_radius=200,fg_color='#8f00ff',hover_color='#c72796',command=logout)
    login.place(x=610,y=423)
    canvas.create_text(720,455, text='|', anchor=SE,font=('Lexend Bold',15),fill='#fff')
    Hi=Label(canvas,text='Hi,',font=('Lexend Light',30),fg='#656565',bg='#101010')
    Hi.place(x=70,y=70)

    Hi=Label(canvas,text='Admin',font=('Lexend Regular',30),fg='#8f00ff',bg='#101010')
    Hi.place(x=125,y=70)

    frame1 = customtkinter.CTkFrame(canvas, corner_radius=30, fg_color='#2b2b2b',width=430,height=295,bg_color='#101010',border_width=0)
    frame1.place(x=70,y=170)

    addMark = Label(frame1, text='Add Mark', font=('Lexend medium', 15), fg='#fff', bg='#2b2b2b')
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
    selectmark=customtkinter.CTkOptionMenu(frame1,width=260,font=('Lexend medium', 15),corner_radius=25,fg_color='#8f00ff',button_color='#6303ac',values=options,dropdown_font=('Lexend medium',12),variable=selectedoption,)
    selectmark.place(x=30, y=65)
    Go=customtkinter.CTkButton(frame1,width=38,fg_color='#8f00ff',text='GO',font=('Lexend medium', 10),corner_radius=38,hover_color='#c72796',command=call)
    Go.place(x=300, y=65)

    def save():
        update(s1entry.get(),s2entry.get(),s3entry.get(),s4entry.get(),selectedoption.get())
        home.destroy()
        admin()
        
    save=customtkinter.CTkButton(frame1,width=50,fg_color='#8f00ff',text='Save',font=('Lexend medium', 12),corner_radius=25,hover_color='#c72796',command=save)
    save.place(x=30, y=248)

    scrollframe= customtkinter.CTkScrollableFrame(canvas,width=280,height=15,label_text='Rank List',label_font=('Lexend medium', 15),corner_radius=25,label_anchor='w',fg_color='#6303ac',label_fg_color='#8f00ff',scrollbar_button_color='#3b0267')
    scrollframe.place(x=560,y=70)

    con,cursor=databaseconnection()
    cursor.execute('use userdata')
    query=('SELECT ROW_NUMBER() OVER (ORDER BY (s1 + s2 + s3 + s4) DESC, s1 DESC) as rank, username,(s1 + s2 + s3 + s4) AS total_marks FROM data where username <> "Admin";')
    cursor.execute(query)
    rows = cursor.fetchall()

    headings = ['Rank','Name','Total Mark']
    for j in range(len(headings)):
        label = customtkinter.CTkLabel(scrollframe,font=('Lexend Bold', 13), text=headings[j])
        label.grid(row=0, column=j, padx=5, pady=1)  

    values = rows
    for i in range(len(values)):
        for j in range(len(values[i])):
            label = customtkinter.CTkLabel(scrollframe,text=values[i][j])
            label.grid(row=i+1, column=j, padx=(30, 30), pady=(1, 1)) 


    home.mainloop()





