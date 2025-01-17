import tkinter
from tkinter import *
from files.base import User_actions,Staff_action
from tkinter import ttk
import datetime
from staff import Staff

class Hotel:
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
        self.login_msg=Label(root,text="Please Enter Your Email And Password Below")
        self.login_msg.grid(row=1, column=3, padx=10, pady=10)

        #userid and password
        self.user_email_lable=Label(self.root,text="Email : ",font=("Arial", 10, "bold"))
        self.user_email_lable.grid(row=2, column=2, padx=10, pady=0)
        self.user_email=Entry(self.root,width=30,bg='#E3F2FD')
        self.user_email.grid(row=2, column=3, padx=10, pady=10)

        self.password_lable=Label(self.root,text="Password : ",font=("Arial", 10, "bold"))
        self.password_lable.grid(row=3, column=2, padx=10, pady=0)
        self.password=Entry(self.root,width=30,bg='#E3F2FD')
        self.password.grid(row=3, column=3, padx=10, pady=10)

        self.login_button=Button(self.root,text='Login',command=self.loginuser,width=30,bg='#ADD8E6')
        self.login_button.grid(row=4, column=3, padx=10, pady=10)

        self.User_create_button=Button(self.root,text='Create account',command=self.user_creation_form,width=30,bg='#ADD8E6')
        self.User_create_button.grid(row=5, column=3, padx=10, pady=10)

        self.user_forget_passwd=Button(self.root,text="Forgot Password?",command=self.user_passwd_rest_request,width=30,bg='#ADD8E6')
        self.user_forget_passwd.grid(row=6, column=3, padx=10, pady=10)

    #main user login function
    def loginuser(self):
        self.email = self.user_email.get()  
        passwd = self.password.get()  
        #self.email = 'test6'
        #passwd = 'test6'
        
        if not self.email or not passwd:
            self.login_msg.config(text=f'Enter Info')
        else:
            self.auth_login = User_actions(self.email, passwd)  
            result = self.auth_login.login_user() 
            if result==False:
                self.login_msg.config(text=f'Invalid username or password')
                self.user_email.delete(0, END) 
                self.password.delete(0, END)

            elif result[0][4]==True: 
                self.show_staff_dashboard()

            else: 
                self.user_name = result[0][1]  
                self.user_email = self.email  
                self.user_method_screen()  
            
                

    #if user is staff member then show this
    def show_staff_dashboard(self):
        self.user_email.delete(0, END)
        self.password.delete(0, END)
        staff_window = Toplevel(self.root)
        staff_app = Staff(staff_window, self.email) 
        staff_window.mainloop()

    


    #clearing login screen
    def login_screen_clear(self):
        self.user_email.destroy()
        self.user_email_lable.destroy()
        self.password_lable.destroy()
        self.password.destroy()
        self.login_button.destroy()
        self.User_create_button.destroy()
        self.user_forget_passwd.destroy()

    #forgot password method
    def user_passwd_rest_request(self):
        self.clear_screen()
        
        welcome_msg = Label(self.root, text="Forgot Password?", font=("", 25))
        welcome_msg.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        rest_passwd_msg = Label(self.root, 
                                text="If you wish to reset your password due to forgetfulness, "
                                    "you can request a reset here. We will forward your request to a staff member "
                                    "for verification. Please approach a staff member for further assistance.",
                                bg='yellow', 
                                justify=LEFT, wraplength=400)
        rest_passwd_msg.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        user_email_label = Label(self.root, text="Email : ")
        user_email_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.user_email_filed = Entry(self.root, width=30)
        self.user_email_filed.grid(row=2, column=1, padx=10, pady=10)

        request_button = Button(self.root, text="Submit", width=40,bg='#4CAF50')
        request_button.grid(row=3, column=0, columnspan=4, pady=20)

    #after login,user option menu
    def user_method_screen(self):
        self.clear_screen()
        result = self.auth_login.login_user()
        user_name = self.user_name

        # Welcome message
        self.welcome_msg = Label(self.root, text=f"Welcome {user_name}", font=("", 25))
        self.welcome_msg.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        # Account Section
        self.method_lable = Label(self.root, text="Account",bg='yellow', font=("", 15))
        self.method_lable.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="n") 

        self.account_button = Button(self.root, text='My Account', command=self.see_account, width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.account_button.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        self.account_updation_button = Button(self.root, text='Account Updation', command=self.account_updation, width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.account_updation_button.grid(row=2, column=3, columnspan=2, padx=10, pady=10)

        # Booking Section
        self.method_lable2 = Label(self.root, text="Booking",bg='yellow', font=("", 15))
        self.method_lable2.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="n")

        self.book_button = Button(self.root, text='Book Room', command=self.book_rooms, width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.book_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

        self.booking_hisotry_button = Button(self.root, text='Booking History', command=self.booking_history, width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.booking_hisotry_button.grid(row=4, column=3, padx=10, pady=10)

        # Food Section
        self.method_lable3 = Label(self.root, text="Food",bg='yellow', font=("", 15))
        self.method_lable3.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="n")  

        self.order_food_button = Button(self.root, text='Order Food', command=self.food_order, width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.order_food_button.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

        self.order_status_button = Button(self.root, text='Order Status', command=self.order_status, width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.order_status_button.grid(row=6, column=3, padx=10, pady=10)



    #User option menu clear
    def user_method_screen_clear(self):
        self.book_button.destroy()
        self.account_updation_button.destroy()
        self.account_button.destroy()
        self.order_food_button.destroy()
        self.welcome_msg.destroy()
        self.booking_hisotry_button.destroy()
        self.order_status_button.destroy()
        self.method_lable.destroy()
        self.method_lable2.destroy()
        self.method_lable3.destroy()

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
        self.fname_lable=Label(self.root,text="First Name :",font=("Arial", 10, "bold"))
        self.fname_lable.grid(row=2, column=2, padx=10, pady=0)
        self.fname=Entry(self.root,width=30,bg='#E3F2FD')
        self.fname.grid(row=2, column=3, padx=10, pady=10)

        self.lname_lable=Label(self.root,text="Last Name :",font=("Arial", 10, "bold"))
        self.lname_lable.grid(row=3, column=2, padx=10, pady=0)
        self.lname=Entry(self.root,width=30,bg='#E3F2FD')
        self.lname.grid(row=3, column=3, padx=10, pady=10)

        self.mobile_lable=Label(self.root,text="Mobile Number :",font=("Arial", 10, "bold"))
        self.mobile_lable.grid(row=4, column=2, padx=10, pady=0)
        self.mobile=Entry(self.root,width=30,bg='#E3F2FD')
        self.mobile.grid(row=4, column=3, padx=10, pady=10)

        self.email_lable=Label(self.root,text="Email :",font=("Arial", 10, "bold"))
        self.email_lable.grid(row=5, column=2, padx=10, pady=0)
        self.email=Entry(self.root,width=30,bg='#E3F2FD')
        self.email.grid(row=5, column=3, padx=10, pady=10)

        self.pass1_lable=Label(self.root,text="Password :",font=("Arial", 10, "bold"))
        self.pass1_lable.grid(row=6, column=2, padx=10, pady=0)
        self.pass1=Entry(self.root,width=30,bg='#E3F2FD')
        self.pass1.grid(row=6, column=3, padx=10, pady=10)

        self.pass2_lable=Label(self.root,text="Confirm Password :",font=("Arial", 10, "bold"))
        self.pass2_lable.grid(row=7, column=2, padx=10, pady=0)
        self.pass2=Entry(self.root,width=30,bg='#E3F2FD')
        self.pass2.grid(row=7, column=3, padx=10, pady=10)

        self.create_button=Button(self.root,text='Submit',command=self.submit_user_creation,width=30,bg='#4CAF50')
        self.create_button.grid(row=8, column=3, padx=10, pady=10)

        self.back_button=Button(self.root,text='Back',command=self.login_form,width=30,bg='#9E9E9E')
        self.back_button.grid(row=9, column=3, padx=10, pady=10)

    #creating new user function
    def submit_user_creation(self):
        fname=self.fname.get()
        lname=self.lname.get()
        mobile=self.mobile.get()
        email=self.email.get()
        pass1=self.pass1.get()
        pass2=self.pass2.get()
        if not fname or not lname or not mobile or not email or not pass1 or not pass2:
            self.login_msg.config(text='Please fill in all the details.')
        else:
            if pass1==pass2:
                password=self.pass1.get()
                user=User_actions()
                result=user.create_user(fname,lname,mobile,email,password)
                if result:
                    self.user_creation_form_clear()
                    self.back_button.destroy()
                    self.login_msg.config(text=f'Account Created')
                    self.back_button=Button(self.root,text='Back To Login',command=self.login_form,bg='#4CAF50')
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



        self.room_book_button=Button(self.root,text='Book Room',width=20,bg='#4CAF50',fg="white", command=self.room_booking)
        self.room_book_button.grid(row=7, column=2,padx=10,pady=10)

        self.error_lable=Label(self.root,text='',bg='red')
        self.error_lable.grid(row=8, column=2,padx=10,pady=10)
        
        self.back_button2=Button(self.root,text='Back',command=self.user_method_screen,width=20,bg='#9E9E9E')
        self.back_button2.grid(row=7, column=3)


    def room_booking(self):
        selected_room = self.tree.selection() 
        user = User_actions()
        if selected_room:
            check_out_date = self.date.get()
            check_out_month = self.month.get()
            check_out_year = self.year.get() 
            if not check_out_date or not check_out_month or not check_out_year:
                self.error_lable.config(text='Please Enter Check Out Date')
            else:
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
                            self.error_lable.config(text='Please Enter Correct Date')
                        else:
                            room_no = room[0]
                            price=user.price_fetch(room_no)
                            days=day_count.days
                            price_total=(days*price)
                            email=self.user_email
                            self.auth_login.room_booking_conform(email,room_no,date,check_out,days,price_total)
                            self.error_lable.config(text=f'Booking Done Thank You, Total Price= {price_total}',bg='yellow')
                        
                    except:
                        self.error_lable.config(text='Error In Date (Please Contact Manager)')
        else:
            self.error_lable.config(text='Please Select Room')

    def see_account(self):
        self.user_method_screen_clear()
        self.welcome_msg = Label(self.root, text="My Account", font=("", 25))
        self.welcome_msg.grid(row=0, column=0,padx=20, pady=20)
        user=User_actions()
        result=user.user_account(self.user_email)
        total_spend=user.user_spends(self.user_email)

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

        self.back_button=Button(self.root,text='Back',command=self.user_method_screen,width=30,bg='#9E9E9E')
        self.back_button.grid(row=7, column=0, padx=10, pady=10, sticky='w')


    def booking_history(self):
        self.user_method_screen_clear()
        user=User_actions()
        result=user.user_booking_history(self.user_email)

        self.welcome_msg=Label(root,text=f"Booking History",font=("", 25))
        self.welcome_msg.grid(row=0, column=1,pady=10)

        columns = ("RoomNo.", "Check In", "Check Out","Days","Price")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        self.tree.heading("RoomNo.", text="RoomNo.")
        self.tree.heading("Check In", text="Check In")
        self.tree.heading("Check Out", text="Check Out")
        self.tree.heading("Days", text="Days")
        self.tree.heading("Price", text="Price")

        self.tree.column("RoomNo.", width=80, anchor="center")
        self.tree.column("Check In", width=100, anchor="center")
        self.tree.column("Check Out", width=100, anchor="center")
        self.tree.column("Days", width=80, anchor="center")
        self.tree.column("Price", width=100, anchor="center")

        for row in result:
            self.tree.insert("", "end", values=row)


        self.tree.grid(row=2, column=1, columnspan=3,padx=10)
        self.back_button=Button(self.root,text='Back',command=self.user_method_screen,width=65,bg='#9E9E9E')
        self.back_button.grid(row=5,column=1,padx=10,pady=15, sticky='w')


    def food_order(self):
        self.user_method_screen_clear()
        user=User_actions()
        result=user.food_items_fetch()

        self.welcome_msg=Label(root,text=f"Order Food",font=("", 25))
        self.welcome_msg.grid(row=0, column=1,pady=10)

        columns = ("tem_id","Name", "Price")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        self.tree.heading("tem_id", text="tem_id")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")

        self.tree.column("tem_id", width=80, anchor="center")
        self.tree.column("Name", width=100, anchor="center")
        self.tree.column("Price", width=100, anchor="center")

        for row in result:
            self.tree.insert("", "end", values=row)

        self.tree.grid(row=2, column=1, columnspan=3,padx=10)

        self.food_item_msg = Label(self.root, text='Select Your Food Item From Above', bg='yellow')
        self.food_item_msg.grid(row=3, column=1, padx=10, pady=10, columnspan=3)

        self.food_item_msg2 = Label(self.root, text='Enter Quantity :')
        self.food_item_msg2.grid(row=4, column=1, padx=10, pady=10)

        self.food_quantity = Entry(self.root, width=30)
        self.food_quantity.grid(row=4, column=2, padx=10, pady=5)

        confirm_order=Button(self.root, text='Place Order', command=self.place_order, width=30, bg='#4CAF50', fg="white", font=("Arial", 10, "bold"))
        confirm_order.grid(row=5, column=1, padx=10, pady=20, sticky="w")

        back_button=Button(self.root,text='Back',command=self.user_method_screen,width=30,bg='#9E9E9E')
        back_button.grid(row=5,column=2,padx=10,pady=20, sticky='w')

    def place_order(self):
        user = User_actions()
        selected_item = self.tree.selection()
        if selected_item:
            selected_item = self.tree.item(selected_item[0])
            values = selected_item["values"]
            food_id = values[0] 
            food_name = values[1] 
            food_price=values[2]
            float_price=float(food_price)
            int_price=int(float_price)
            quantity = self.food_quantity.get()
            if not quantity:
                self.food_item_msg.config(text="Please Enter No Of Quantity", bg='yellow')
            else:
                email = self.user_email
                total_quantity=int(quantity)
                total_price=float_price*total_quantity
                place_order = user.food_order(email, food_id, food_name,total_price, quantity)
                if place_order:
                    self.food_item_msg.config(text="Order Placed Successfully, Thank you", bg='green')
                else:
                    self.food_item_msg.config(text="You don't have any active room booking", bg='red')
                
    def order_status(self):
        self.clear_screen()
        user = User_actions()
        result=user.order_status_check(self.user_email)
        self.welcome_msg=Label(root,text=f"Order History",font=("", 25))
        self.welcome_msg.grid(row=0, column=1,pady=10)

        columns = ("order_id","room_no","food_name","quantity", "price","status")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        self.tree.heading("order_id", text="Order_id")
        self.tree.heading("room_no", text="Room_no")
        self.tree.heading("food_name", text="Food_name")
        self.tree.heading("quantity", text="Quantity")
        self.tree.heading("price", text="Price")
        self.tree.heading("status", text="status")

        self.tree.column("order_id", width=80, anchor="center")
        self.tree.column("room_no", width=50, anchor="center")
        self.tree.column("food_name", width=100, anchor="center")
        self.tree.column("quantity", width=50, anchor="center")
        self.tree.column("price", width=100, anchor="center")
        self.tree.column("status", width=100, anchor="center")

        for row in result:
            self.tree.insert("", "end", values=row)

        self.tree.grid(row=2, column=1, columnspan=3,padx=10)

        back_button=Button(self.root,text='Back',command=self.user_method_screen,width=65,bg='#9E9E9E')
        back_button.grid(row=4,column=1,padx=15,pady=20, sticky='w')     

    def account_updation(self):
        self.clear_screen()
        user = User_actions()
        result=user.account_info_fetch(self.user_email)
        fname=result[0][0]
        lname=result[0][1]
        mob_no=result[0][2]
        email=result[0][3]

        self.welcome_msg=Label(root,text=f"Account Info",font=("", 25))
        self.welcome_msg.grid(row=0, column=1,pady=10,padx=20)

        #first name
        fname_lable=Label(self.root,text='Fist name : ', font=("Arial", 15, "bold"))
        fname_lable.grid(row=2,column=1,pady=10)
        self.fname_entry=Entry(self.root,width=30, font=("Arial", 10))
        self.fname_entry.grid(row=2,column=2,pady=10)
        self.fname_entry.insert(0,fname)

        #last name
        lname_lable=Label(self.root,text='Last name : ', font=("Arial", 15, "bold"))
        lname_lable.grid(row=3,column=1,pady=10)
        self.lname_entry=Entry(self.root,width=30, font=("Arial", 10))
        self.lname_entry.grid(row=3,column=2,pady=10)
        self.lname_entry.insert(0,lname)

        #mobile no
        mob_no_lable=Label(self.root,text='Mobile No. : ', font=("Arial", 15, "bold"))
        mob_no_lable.grid(row=4,column=1,pady=10)
        self.mob_no_entry=Entry(self.root,width=30, font=("Arial", 10))
        self.mob_no_entry.grid(row=4,column=2,pady=10)
        self.mob_no_entry.insert(0,mob_no)

        #message
        self.UC_messge_lable=Label(self.root,text="Leave blank if you don't want to change password",bg='yellow')
        self.UC_messge_lable.grid(row=6,column=1,sticky='n')
        
        #password1
        passwd_lable=Label(self.root,text='New Password : ', font=("Arial", 15, "bold"))
        passwd_lable.grid(row=8,column=1,pady=10)
        self.passwd_entry=Entry(self.root,width=30, font=("Arial", 10))
        self.passwd_entry.grid(row=8,column=2,pady=10)

        #password2
        passwd_lable2=Label(self.root,text='Confirm Password : ', font=("Arial", 15, "bold"))
        passwd_lable2.grid(row=9,column=1,pady=10)
        self.passwd2_entry=Entry(self.root,width=30, font=("Arial", 10))
        self.passwd2_entry.grid(row=9,column=2,pady=10)

        #buttons
        confirm_button=Button(self.root,text='Update Info',width=30,command=self.account_updation_confirm,bg='#4CAF50')
        confirm_button.grid(row=11,column=1)
        back_button=Button(self.root,text='Back',command=self.user_method_screen,width=30,bg='#9E9E9E')
        back_button.grid(row=11,column=2 ,sticky='w')

    #updating info without entring password
    def account_updation_without_pass(self):
        user = User_actions()
        email=self.user_email
        fname=self.fname_entry.get()
        lname=self.lname_entry.get()
        mobile=self.mob_no_entry.get()
        result=user.user_acc_update(email,fname,lname,mobile)
        if not result:
                self.UC_messge_lable.config(text='ERROR IN UPDATING USER INFO',bg='red')
        else:
            self.UC_messge_lable.config(text='User Information Updated',bg='green')  

    #updating user info with password and other info
    def account_updation_confirm(self):
        user = User_actions()
        email=self.user_email
        passwd1=self.passwd_entry.get()
        passwd2=self.passwd2_entry.get()
        if not passwd1 or not passwd2:
            self.account_updation_without_pass()    
        else:
            if passwd1==passwd2:
                result=user.user_acc_password_update(email,passwd1)
                self.account_updation_without_pass() 
                if result:
                    self.UC_messge_lable.config(text='User Info Updated',bg='green') 
                else:
                    self.UC_messge_lable.config(text='ERROR IN UPDATING PASS',bg='red')



root=tkinter.Tk()
hotel=Hotel(root)
root.mainloop()