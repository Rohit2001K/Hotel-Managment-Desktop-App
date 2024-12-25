import tkinter
from tkinter import *
from base import User_actions

class login:
    def __init__(self,root):


        #basic config
        self.root=root
        self.root.title("R Hotel")
        self.root.geometry("500x400")

        #messages
        self.welcome_msg=Label(root,text="Welcome",font=("", 25))
        self.welcome_msg.grid(row=0, column=3)

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

        self.User_create_button=Button(self.root,text='Create account',command=self.user_creation_form)
        self.User_create_button.grid(row=5, column=3, padx=10, pady=10)


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

    def login_screen_clear(self):
        self.user.destroy()
        self.user_lable.destroy()
        self.password_lable.destroy()
        self.password.destroy()
        self.login_button.destroy()
        self.User_create_button.destroy()



    def user_creation_form(self):
        self.login_screen_clear()
        self.login_msg.config(text=f'Please enter you infomation')
        self.welcome_msg.config(text='Account Creation')
        #lables and entries
        self.fname_lable=Label(self.root,text="First Name :")
        self.fname_lable.grid(row=2, column=2, padx=10, pady=0)
        self.fname=Entry(self.root,width=30)
        self.fname.grid(row=2, column=3, padx=10, pady=10)

        self.lname_lable=Label(self.root,text="Last Name :")
        self.lname_lable.grid(row=3, column=2, padx=10, pady=0)
        self.lname=Entry(self.root,width=30)
        self.lname.grid(row=3, column=3, padx=10, pady=10)

        self.mobile_lable=Label(self.root,text="Mobile Number :")
        self.mobile_lable.grid(row=4, column=2, padx=10, pady=0)
        self.mobile=Entry(self.root,width=30)
        self.mobile.grid(row=4, column=3, padx=10, pady=10)

        self.email_lable=Label(self.root,text="Email :")
        self.email_lable.grid(row=5, column=2, padx=10, pady=0)
        self.email=Entry(self.root,width=30)
        self.email.grid(row=5, column=3, padx=10, pady=10)

        self.pass1_lable=Label(self.root,text="Password :")
        self.pass1_lable.grid(row=6, column=2, padx=10, pady=0)
        self.pass1=Entry(self.root,width=30)
        self.pass1.grid(row=6, column=3, padx=10, pady=10)

        self.pass2_lable=Label(self.root,text="Confirm Password :")
        self.pass2_lable.grid(row=7, column=2, padx=10, pady=0)
        self.pass2=Entry(self.root,width=30)
        self.pass2.grid(row=7, column=3, padx=10, pady=10)

        self.create_button=Button(self.root,text='Submit',command=self.submit_user_creation)
        self.create_button.grid(row=8, column=3, padx=10, pady=10)

    def submit_user_creation(self):
        fname=self.fname.get()
        lname=self.lname.get()
        mobile=self.mobile.get()
        email=self.email.get()
        if self.pass1.get()==self.pass2.get():
            password=self.pass1.get()
            return password
        else:
            self.login_msg.config(text=f'Please Check Your Passwords')

        

root=tkinter.Tk()

hotel=login(root)
root.mainloop()