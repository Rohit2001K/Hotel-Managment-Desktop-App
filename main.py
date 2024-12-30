import tkinter
from tkinter import *
from base import User_actions
from tkinter import ttk
import datetime


class login:
    def __init__(self,root):
        #basic config
        self.root=root
        self.root.title("R Hotel")
        self.root.geometry("500x550")
        self.login_form()


#login form which take user inputs
    def login_form(self):

        #clearning previous screen
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

    #main user login function
    def loginuser(self):
        username=self.user.get()
        passwd=self.password.get()
        self.auth_login=User_actions(username,passwd)
        result=self.auth_login.login_user()
        self.user_id=result[0]
        if result:
            self.user_method_screen()

        else:
            self.login_msg.config(text=f'Invalid username or password')
            self.user.delete(0, END)
            self.password.delete(0, END)

    #clearing login screen
    def login_screen_clear(self):
        self.user.destroy()
        self.user_lable.destroy()
        self.password_lable.destroy()
        self.password.destroy()
        self.login_button.destroy()
        self.User_create_button.destroy()

    #after login,user option menu
    def user_method_screen(self):
        self.clear_screen()
        result=self.auth_login.login_user()
        self.user_id=result[0] 

        self.welcome_msg=Label(root,text=f"Welcome {result[1]}",font=("", 25))
        self.welcome_msg.grid(row=0, column=3,padx=10,pady=20)

        self.book_button=Button(self.root,text='Book Room',command=self.book_rooms,width=15)
        self.book_button.grid(row=4, column=3,padx=50)

        self.account_button=Button(self.root,text='My Account ',command=self.see_account,width=15)
        self.account_button.grid(row=4, column=4)

        self.order_food_button=Button(self.root,text='Order Food',command='',width=15)
        self.order_food_button.grid(row=6, column=3,padx=50,pady=50)

        self.booking_hisotry_button=Button(self.root,text='Booking History',command='',width=15)
        self.booking_hisotry_button.grid(row=6, column=4)

    #User option menu clear
    def user_method_screen_clear(self):
        self.book_button.destroy()
        self.account_button.destroy()
        self.order_food_button.destroy()
        self.welcome_msg.destroy()
        self.booking_hisotry_button.destroy()

    #sign up form clear
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


    #User sign up form
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

    #creating new user function
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

    #clear everything function
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()        



    #Abooking options
    def book_rooms(self):
        self.user_method_screen_clear()

        self.welcome_msg=Label(root,text=f"Select Room",font=("", 25))
        self.welcome_msg.grid(row=0, column=2,pady=10)

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

        self.tree.grid(row=2, column=1, columnspan=3)

        self.booking_msg=Label(self.root,text="Enter Check Out Date ")
        self.booking_msg.grid(row=3, column=2,padx=10,pady=10)

        self.date_lable=Label(self.root,text="Date : ")
        self.date_lable.grid(row=4, column=1,padx=10,pady=10)

        self.date=Entry(self.root,width=20)
        self.date.grid(row=4, column=2)

        self.month_lable=Label(self.root,text="Month : ")
        self.month_lable.grid(row=5, column=1,padx=10,pady=10)

        self.month=Entry(self.root,width=20)
        self.month.grid(row=5, column=2)

        self.year_lable=Label(self.root,text="Year : ")
        self.year_lable.grid(row=6, column=1,padx=10,pady=10)

        self.year=Entry(self.root,width=20)
        self.year.grid(row=6, column=2)



        self.room_book_button=Button(self.root,text='Book Room', command=self.room_booking)
        self.room_book_button.grid(row=7, column=2,padx=10,pady=10)

        self.error_lable=Label(self.root,text='',bg='red')
        self.error_lable.grid(row=8, column=2,padx=10,pady=10)
        
        self.back_button2=Button(self.root,text='Back',command=self.user_method_screen,width=10)
        self.back_button2.grid(row=7, column=3)


    def room_booking(self):
        selected_room = self.tree.selection() 
        user = User_actions()
        if selected_room:
            check_out_date = self.date.get()
            check_out_month = self.month.get()
            check_out_year = self.year.get() 
            if selected_room:
                room=self.tree.item(selected_room, "values")
                try:
                    check_out_date=int(check_out_date)
                    check_out_month=int(check_out_month)
                    check_out_year=int(check_out_year)
                    date=datetime.date.today()
                    check_out=datetime.date(check_out_year, check_out_month, check_out_date)
                    day_count=check_out-date
                    days=day_count.days
                    if days<0:
                        self.error_lable.config(text='Please Type Correct Date')
                    else:
                        room_no = room[0]
                        price=user.price_fetch(room_no)
                        days=day_count.days
                        price_total=(days*price)
                        uid=self.user_id
                        uid=uid[0]
                        self.auth_login.room_booking_conform(uid,room_no,date,check_out,days,price_total)
                        self.error_lable.config(text=f'Booking Done Thank You, Total Price= {price_total}',bg='yellow')
                        
                except:
                    self.error_lable.config(text='Error In Date (Please Contact Manager)')
        else:
            self.error_lable.config(text='Please Select Room')

    def see_account(self):
        self.user_method_screen_clear()
        user = User_actions()

        self.welcome_msg = Label(self.root, text="My Account", font=("", 25))
        self.welcome_msg.grid(row=0, column=0,padx=20, pady=20)

        uid = self.user_id
        uid = uid[0]
        result = user.user_account(uid)
        total_spend=user.user_spends(uid)

        self.fname_lable = Label(self.root, text=f'First name:-  {result[0][1]}', font=("", 15))
        self.fname_lable.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.lname_lable = Label(self.root, text=f'Last name:-  {result[0][2]}', font=("", 15))
        self.lname_lable.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        self.mobileno_lable = Label(self.root, text=f'Mobile No:-  {result[0][3]}', font=("", 15))
        self.mobileno_lable.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        self.email_lable = Label(self.root, text=f'Email:-  {result[0][5]}', font=("", 15))
        self.email_lable.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        self.total_spend_lable = Label(self.root, text=f'Totel Spends :-  Rs.{total_spend}', font=("", 15))
        self.total_spend_lable.grid(row=5, column=0, padx=10, pady=10, sticky='w')

        self.msg_lable=Label(self.root,text='Please Contact Stuff Member To Update Your Info ',bg='yellow')
        self.msg_lable.grid(row=6, column=0, padx=10, pady=10, sticky='w')

        self.back_button=Button(self.root,text='Back',command=self.user_method_screen,width=30,bg='green')
        self.back_button.grid(row=7, column=0, padx=10, pady=10, sticky='w')






root=tkinter.Tk()

hotel=login(root)
root.mainloop()