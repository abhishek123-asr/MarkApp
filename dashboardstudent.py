from tkinter import *
import customtkinter 
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

home=Tk()
home.geometry("926x520+50+30")
home.configure(bg='#101010')
home.resizable(False,False)
home.title("MarkApp")

def logout():
    home.destroy()
    import login

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

Hi=Label(canvas,text='Username',font=('Lexend Regular',30),fg='#8f00ff',bg='#101010')
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