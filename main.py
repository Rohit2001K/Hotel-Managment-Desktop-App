import tkinter
from tkinter import *


#config
root=tkinter.Tk()
root.title("XYZ Motel")
root.geometry("800x400")

frame=tkinter.Frame(root)
frame.pack(pady=10)


#welcome
welcome_msg=Label(root,text="Welcome",font=("", 25)).pack(pady=10)
login_msg=Label(root,text="Please Enter Your UserID And Password Below").pack(pady=10)



#login
user_id_text=Label(root,text="Enter UserID :").pack()
user_id=Entry(root,width=50).pack()


password_text=Label(root,text="Enter Password :").pack()
password=Entry(root,width=50).pack()

login_button=Button(root,text="Login").pack()




















root.mainloop()