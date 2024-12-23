import tkinter
from tkinter import *


class login:
    def __init__(self,root):


        #basic config
        self.root=root
        self.root.title("XYZ")
        self.root.geometry("800x400")

        #messages
        self.welcome_msg=Label(root,text="Welcome",font=("", 25)).pack(pady=10)
        self.login_msg=Label(root,text="Please Enter Your UserID And Password Below").pack(pady=10)

        #userid and password
        self.user=Entry(self.root,width=30).pack()
        self.password=Entry(self.root,width=30).pack()
        self.login_button=Button(self.root,text='Login').pack()







root=tkinter.Tk()

hotel=login(root)
root.mainloop()