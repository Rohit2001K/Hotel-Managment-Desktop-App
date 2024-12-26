import tkinter
from tkinter import *
from base import User_actions
from tkinter import ttk

class login:
    def __init__(self,root):
        #basic config
        self.root=root
        self.root.title("R Hotel")
        self.root.geometry("500x400")
        self.login_form()


    def login_form(self):

        self.clear_screen()
        self.welcome_msg=Label(root,text="Welcome",font=("", 25))
        self.welcome_msg.grid(row=0, column=3,padx=10, pady=10)
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
            self.User_create_button.destroy()
            self.book_button=Button(self.root,text='Book Room',command=self.book_rooms)
            self.book_button.grid(row=4, column=3, padx=10, pady=10)
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

    def user_creation_form_clear(self):
        self.fname.destroy()
        self.fname_lable.destroy()

        self.lname_lable.destroy()
        self.lname.destroy()

        self.mobile_lable.destroy()
        self.mobile.destroy()

        self.email_lable.destroy()
        self.email.destroy()

        self.pass1_lable.destroy()
        self.pass1.destroy()

        self.pass2_lable.destroy()
        self.pass2.destroy()



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
            user=User_actions()
            result=user.create_user(fname,lname,mobile,email,password)
            if result:
                self.user_creation_form_clear()
                self.login_msg.config(text=f'Account Created')
                self.back_button=Button(self.root,text='Back To Login',command=self.login_form)
                self.back_button.grid(row=4, column=3, padx=10, pady=10)
                
        else:
            self.login_msg.config(text=f'Please Check Your Passwords')

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()        



    #After login user options

    def book_rooms(self):

        self.welcome_msg.config(text="Select Room")

        self.login_msg.destroy()
        self.book_button.destroy()
        user = User_actions()
        result = user.room_booking()

        columns = ("Room Number", "Beds", "Price")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        self.tree.heading("Room Number", text="Room Number")
        self.tree.heading("Beds", text="Beds")
        self.tree.heading("Price", text="Price")

        self.tree.column("Room Number", width=100, anchor="center")
        self.tree.column("Beds", width=100, anchor="center")
        self.tree.column("Price", width=100, anchor="center")

        for row in result:
            self.tree.insert("", "end", values=row)

        self.tree.grid(row=2, column=1, columnspan=3, padx=10, pady=10)
        self.room_book_button=Button(self.root,text='Book Room',command='')
        self.room_book_button.grid(row=3, column=1, padx=10, pady=10)
   
        
        
    





root=tkinter.Tk()

hotel=login(root)
root.mainloop()