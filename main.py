import tkinter
from tkinter import *
from base import User_actions

class login:
    def __init__(self,root):


        #basic config
        self.root=root
        self.root.title("R Hotel")
        self.root.geometry("400x400")

        #messages
        self.welcome_msg=Label(root,text="Welcome",font=("", 25)).grid(row=0, column=3)
        self.login_msg=Label(root,text="Please Enter Your UserID And Password Below")
        self.login_msg.grid(row=1, column=3, padx=10, pady=10)

        #userid and password
        self.user_lable=Label(self.root,text="UserName")
        self.user_lable.grid(row=2, column=2, padx=10, pady=0)
        self.user=Entry(self.root,width=30)
        self.user.grid(row=2, column=3, padx=10, pady=10)

        self.password_lable=Label(self.root,text="Password")
        self.password_lable.grid(row=3, column=2, padx=10, pady=0)
        self.password=Entry(self.root,width=30)
        self.password.grid(row=3, column=3, padx=10, pady=10)

        self.login_button=Button(self.root,text='Login',command=self.loginuser)
        self.login_button.grid(row=4, column=3, padx=10, pady=10)

    def loginuser(self):
        username=self.user.get()
        passwd=self.password.get()
        auth_login=User_actions(username,passwd)
        result=auth_login.login_user()
        if result:
            self.login_msg.config(text=f'Welcome {result} ')
            self.user.destroy()
            self.user_lable.destroy()
            self.password_lable.destroy()
            self.password.destroy()
            self.login_button.destroy()
            
        else:
            self.login_msg.config(text=f'Invalid username or password')
            self.user.delete(0, END)
            self.password.delete(0, END)
        





root=tkinter.Tk()

hotel=login(root)
root.mainloop()