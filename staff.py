import tkinter
from tkinter import *
from tkinter import ttk
from files.base import Staff_action

class Staff:
    def __init__(self, root, email):
        self.root = root
        self.root.title("R Hotel Staff Dashboard")
        self.root.geometry("600x550")
        self.user_email=email
        self.staff_dashboard()

    def staff_dashboard(self):
        self.clear_screen()
        user = Staff_action(self.user_email)
        self.user=user
        result = user.staff_info()
        self.msg = Label(self.root, text=f'Welcome {result} To Staff Dashboard', font=("", 20))
        self.msg.grid(row=0, column=0, columnspan=2, padx=10, pady=10) 

        #user section
        method_lable = Label(self.root, text="User Account",bg='yellow', font=("", 15))
        method_lable.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="n") 

        self.account_updation_button = Button(self.root, text='User Account Updation', command='', width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.account_updation_button.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        password_reset_button=Button(self.root,text="Password Reset Requests",command=self.password_reset,width=20,bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        password_reset_button.grid(row=2, column=1, padx=20, pady=10, sticky="w")
        #booking section
        method_lable1 = Label(self.root, text="User Check Out",bg='yellow', font=("", 15))
        method_lable1.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="n") 

        self.check_out_button = Button(self.root, text='User Check Out', command=self.user_check_out, width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.check_out_button.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        self.booking_histroy_button = Button(self.root, text='Booking History', command=self.booking_histroy, width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.booking_histroy_button.grid(row=4, column=1, padx=20, pady=10, sticky="w")
        
        #food section
        method_lable3 = Label(self.root, text="Food Section",bg='yellow', font=("", 15))
        method_lable3.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="n") 

        self.food_list_button = Button(self.root, text='Food Iteams', command=self.list_food_iteam, width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.food_list_button.grid(row=6, column=0, padx=20, pady=10, sticky="w")

        self.food_requst_button = Button(self.root, text='User Food Requests', command=self.food_request, width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.food_requst_button.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    def user_check_out(self):
        self.clear_screen()
        staff=self.user
        result=staff.current_bookings()

        self.welcome_msg=Label(self.root,text=f"Current Booking",font=("", 25))
        self.welcome_msg.grid(row=0, column=1,pady=10)

        columns = ("Id","Email","RoomNo.", "Check In", "Check Out","Days","Price","Check Out Status")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        self.tree.heading("Id", text="Id")
        self.tree.heading("Email", text="Email")
        self.tree.heading("RoomNo.", text="RoomNo.")
        self.tree.heading("Check In", text="Check In")
        self.tree.heading("Check Out", text="Check Out")
        self.tree.heading("Days", text="Days")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Check Out Status", text="Check Out Status")

        self.tree.column("Id", width=40, anchor="center")
        self.tree.column("Email", width=80, anchor="center")
        self.tree.column("RoomNo.", width=50, anchor="center")
        self.tree.column("Check In", width=80, anchor="center")
        self.tree.column("Check Out", width=80, anchor="center")
        self.tree.column("Days", width=40, anchor="center")
        self.tree.column("Price", width=80, anchor="center")
        self.tree.column("Check Out Status", width=80, anchor="center")

        for row in result:
            self.tree.insert("", "end", values=row)

        self.tree.grid(row=2, column=1, columnspan=3)

        self.check_out_button = Button(self.root, text='Confirm Check Out', command=self.user_check_out_confirm, width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.check_out_button.grid(row=6, column=1,padx=20,pady=20,sticky="w")

        self.back_button=Button(self.root, text='Back', command=self.staff_dashboard, width=15, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.back_button.grid(row=6, column=2,pady=20,sticky="w")

        self.message_lable=Label(self.root,text="Please Verify User Info And Select Room For Check Out",bg='yellow',font=("Arial", 10, "bold"))
        self.message_lable.grid(row=8,column=1,padx=20)

    def user_check_out_confirm(self):
        selected_room = self.tree.selection() 
        if selected_room:
            booking_details=self.tree.item(selected_room, "values")
            id=booking_details[0]
            room_no=booking_details[2]
            result=self.user.check_out(id,room_no)
            if result==True:
                self.message_lable.config(text='Check Out Done Thank You....')
            else:
                self.message_lable.config(text='Error In Checking Out User...',bg='red')
                
                
    def booking_histroy(self):
        self.clear_screen()
        staff=self.user
        result=staff.booking_history()

        self.welcome_msg=Label(self.root,text=f"Previous Bookings",font=("", 25))
        self.welcome_msg.grid(row=0, column=1,pady=10)

        columns = ("Id","Email","RoomNo.", "Check In", "Check Out","Days","Price","Check Out Status")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        self.tree.heading("Id", text="Id")
        self.tree.heading("Email", text="Email")
        self.tree.heading("RoomNo.", text="RoomNo.")
        self.tree.heading("Check In", text="Check In")
        self.tree.heading("Check Out", text="Check Out")
        self.tree.heading("Days", text="Days")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Check Out Status", text="Check Out Status")

        self.tree.column("Id", width=40, anchor="center")
        self.tree.column("Email", width=80, anchor="center")
        self.tree.column("RoomNo.", width=50, anchor="center")
        self.tree.column("Check In", width=80, anchor="center")
        self.tree.column("Check Out", width=80, anchor="center")
        self.tree.column("Days", width=40, anchor="center")
        self.tree.column("Price", width=80, anchor="center")
        self.tree.column("Check Out Status", width=80, anchor="center")

        for row in result:
            self.tree.insert("", "end", values=row)

        self.tree.grid(row=2, column=1, columnspan=3,padx=10)

       

        self.back_button=Button(self.root, text='Back', command=self.staff_dashboard, width=30, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.back_button.grid(row=6, column=1,padx=10,pady=20,sticky="w")


    def list_food_iteam(self):
        self.clear_screen()
        staff=self.user
        result=staff.show_food_items()

        self.welcome_msg=Label(self.root,text=f"Food Items",font=("", 25))
        self.welcome_msg.grid(row=0, column=1,pady=10,padx=10)

        columns = ("Id","Name","Price", "Availability")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        self.tree.heading("Id", text="Id")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Availability", text="Availability")

        self.tree.column("Id", width=40, anchor="center")
        self.tree.column("Name", width=100, anchor="center")
        self.tree.column("Price", width=50, anchor="center")
        self.tree.column("Availability", width=100, anchor="center")

        for row in result:
            self.tree.insert("", "end", values=row)

        self.tree.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

        self.food_item_msg = Label(self.root, text='Add New Item (Fill Below Details)', bg='yellow')
        self.food_item_msg.grid(row=3, column=1, padx=10, pady=10, columnspan=3)

        food_name_label = Label(self.root, text='Food Name: ')
        food_name_label.grid(row=4, column=1, padx=10, pady=5, sticky="e")

        self.food_name = Entry(self.root, width=30)
        self.food_name.grid(row=4, column=2, padx=10, pady=5)

        food_price_label = Label(self.root, text='Price: ')
        food_price_label.grid(row=5, column=1, padx=10, sticky="e")

        self.food_price = Entry(self.root, width=30)
        self.food_price.grid(row=5, column=2, padx=10)

        list_new_item = Button(self.root, text='Add New Item', command=self.add_new_item, width=30, bg='#4CAF50', fg="white", font=("Arial", 10, "bold"))
        list_new_item.grid(row=6, column=1, padx=10, pady=20, sticky="w")

        back_button = Button(self.root, text='Back', command=self.staff_dashboard, width=30, bg='#4CAF50', fg="white", font=("Arial", 10, "bold"))
        back_button.grid(row=6, column=2, padx=10, pady=20, sticky="w")

        self.food_item_msg2 = Label(self.root, text='Want To Change Availability Of Above Item? Select And Click Below Button', bg='yellow')
        self.food_item_msg2.grid(row=7, column=1, padx=10, pady=10, columnspan=3)

        make_available_button = Button(self.root, text='Make Item Available', command=lambda: self.change_item_availability('available'), width=30, bg='#4CAF50', fg="white", font=("Arial", 10, "bold"))
        make_available_button.grid(row=8, column=1, padx=10)

        make_out_of_stock_button = Button(self.root, text='Make Item Out Of Stock', command=lambda: self.change_item_availability('out of stock'), width=30, bg='#4CAF50', fg="white", font=("Arial", 10, "bold"))
        make_out_of_stock_button.grid(row=8, column=2, padx=10)

    def add_new_item(self):
        staff=self.user

        food_name=self.food_name.get()
        food_price=self.food_price.get()

        if not food_name or not food_price:
            self.food_item_msg.config(text='Please Enter Food Name And Price')
        else:
            action=staff.list_new_item(food_name,food_price)
            if action==False:
                self.food_item_msg.config(text='Please Re Check The Name And Price')
            else:
                self.food_item_msg.config(text='New Iteam Listed')


    def change_item_availability(self,status):
        staff=self.user
        selected_item=self.tree.selection() 
        if selected_item:
            selected_item=self.tree.item(selected_item, "values")
            food_name=selected_item[1]
            action=staff.food_item_status(status,food_name)
            if not action:
                self.food_item_msg2.config(text="ERROR Please Contact Admin")
            else:
                self.food_item_msg2.config(text="Food Item Availability Status Updated, Please Go Back And Come Back Again")
        
        else:
            self.food_item_msg2.config(text="Plese Select Food Item Fist Before Changing Availability Status")


    def food_request(self):
        self.clear_screen()
        staff=self.user
        result=staff.food_req()

        self.welcome_msg=Label(self.root,text=f"Order Requests",font=("", 25))
        self.welcome_msg.grid(row=0, column=1,pady=10,padx=10)

        columns = ("OrderId","room_no","food_id","food_name","quantity","Price","status")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        self.tree.heading("OrderId", text="OrderId")
        self.tree.heading("room_no", text="room_no")
        self.tree.heading("food_id", text="food_id")
        self.tree.heading("food_name", text="food_name")
        self.tree.heading("quantity", text="quantity")
        self.tree.heading("Price", text="Price")
        self.tree.heading("status", text="status")

        self.tree.column("OrderId", width=50, anchor="center")
        self.tree.column("room_no", width=50, anchor="center")
        self.tree.column("food_id", width=50, anchor="center")
        self.tree.column("food_name", width=100, anchor="center")
        self.tree.column("quantity", width=50, anchor="center")
        self.tree.column("Price", width=50, anchor="center")
        self.tree.column("status", width=100, anchor="center")

        for row in result:
            self.tree.insert("", "end", values=row)

        self.tree.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

        self.food_item_msg = Label(self.root, text='Select Item,to Change Status', bg='yellow')
        self.food_item_msg.grid(row=3, column=1, padx=10, pady=10, columnspan=3)

        preparing_button = Button(self.root, text='Set Preparing Status', command=lambda: self.food_request_status('preparing'), width=50, bg='#4CAF50', fg="white", font=("Arial", 10, "bold"))
        preparing_button.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        delivered_button = Button(self.root, text='Set Delivered Status', command=lambda: self.food_request_status('delivered'), width=50, bg='#4CAF50', fg="white", font=("Arial", 10, "bold"))
        delivered_button.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        cancelled_button = Button(self.root, text='Cancel Order ', command=lambda: self.food_request_status('cancelled'), width=50, bg='#4CAF50', fg="white", font=("Arial", 10, "bold"))
        cancelled_button.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        back_button = Button(self.root, text='Go Back', command=self.staff_dashboard, width=50,bg='#9E9E9E', fg="white", font=("Arial", 10, "bold"))
        back_button.grid(row=7, column=1, padx=10, pady=5, sticky="w")

    def food_request_status(self,status):
        staff=self.user
        selected_item=self.tree.selection() 
        if selected_item:
            selected_item=self.tree.item(selected_item, "values")
            food_id=selected_item[0]
            action=staff.food_req_status(status,food_id)
            if not action:
                self.food_item_msg.config(text="ERROR Please Contact Admin")
            else:
                self.food_item_msg.config(text="Food Item Status Updated, Please Go Back And Come Back Again")
        
        else:
            self.food_item_msg.config(text="Plese Select Food Item Fist Before Changing Status")

#user password reset request functions
#All pending requests fetch
    def password_reset(self):
        self.clear_screen()
        staff=self.user
        result=staff.password_rest()

        self.welcome_msg=Label(self.root,text="Rest Requests",font=("", 25))
        self.welcome_msg.grid(row=0, column=1,pady=10,padx=10)

        columns = ("Sno.","User Email","Status","Created On")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        self.tree.heading("Sno.", text="Sno.")
        self.tree.heading("User Email", text="User Email")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Created On", text="Created On")

        self.tree.column("Sno.", width=50, anchor="center")
        self.tree.column("User Email", width=80, anchor="center")
        self.tree.column("Status", width=100, anchor="center")
        self.tree.column("Created On", width=150, anchor="center")

        for row in result:
            self.tree.insert("", "end", values=row)

        self.tree.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

        self.rest_msg = Label(self.root, text='Select one of the pending request', bg='yellow')
        self.rest_msg.grid(row=3, column=1, padx=10, pady=10, columnspan=3)

        accept_button = Button(self.root, text='Accept Request And Verify', command=self.verify_request, width=50, bg='#4CAF50', fg="white", font=("Arial", 10, "bold"))
        accept_button.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        cancel_button = Button(self.root, text='Cancel Request', command=self.cancel_user_request, width=50, bg='#4CAF50', fg="white", font=("Arial", 10, "bold"))
        cancel_button.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        back_button = Button(self.root, text='Go Back', command=self.staff_dashboard, width=50,bg='#9E9E9E', fg="white", font=("Arial", 10, "bold"))
        back_button.grid(row=6, column=1, padx=10, pady=5, sticky="w")

#cancelling user password reset request
    def cancel_user_request(self):
        staff=self.user
        selected_item=self.tree.selection() 
        if selected_item:
            selected_item=self.tree.item(selected_item, "values")
            user_email = selected_item[1]
            status="cancelled"
            staff.update_reset_request_status(user_email,self.user_email,status)
            self.rest_msg.config(text="User reset request cancelled..")
        else:
            self.rest_msg.config(text="Please select any user before continue",bg='red')

#after selecting specific user from table ,user account fetch function
    def verify_request(self):
        self.clear_screen_tree()
        staff=self.user
        selected_item=self.tree.selection() 
        if selected_item:
            selected_item=self.tree.item(selected_item, "values")
            user_email = selected_item[1]
            result=staff.user_account_info_fetch(user_email)

            welcome_msg=Label(self.root,text="Reset Requests",font=("", 25))
            welcome_msg.grid(row=0, column=0,pady=10)

            imp_msg=Label(self.root,text="Please verify the user's information and match it with the details below.",bg='yellow')
            imp_msg.grid(row=1,column=0,padx=10, pady=10, sticky='w')
            fname_lable = Label(self.root, text=f'First name:-  {result[0][0]}', font=("", 15))
            fname_lable.grid(row=2, column=0, padx=10, pady=10, sticky='w')

            lname_lable = Label(self.root, text=f'Last name:-  {result[0][1]}', font=("", 15))
            lname_lable.grid(row=3, column=0, padx=10, pady=10, sticky='w')

            mobileno_lable = Label(self.root, text=f'Mobile No:-  {result[0][2]}', font=("", 15))
            mobileno_lable.grid(row=4, column=0, padx=10, pady=10, sticky='w')

            email_lable = Label(self.root, text=f'Email:-  {result[0][3]}', font=("", 15))
            email_lable.grid(row=5, column=0, padx=10, pady=10, sticky='w')

            verify_button=Button(self.root,text='Verify And Set New Password',command=lambda: self.set_password(user_email),width=50, bg='#4CAF50', fg="white", font=("Arial", 10, "bold"))
            verify_button.grid(row=6, column=0, padx=10, pady=5, sticky="w")

            back_button = Button(self.root, text='Back', command=self.password_reset, width=50,bg='#9E9E9E', fg="white", font=("Arial", 10, "bold"))
            back_button.grid(row=7, column=0, padx=10, pady=5, sticky="w")

        else:
            self.password_reset()
            self.rest_msg.config(text="Please select any user before continue",bg='red')

#setting up new password
    def set_password(self,user_email):
        self.clear_screen_tree()
        welcome_msg = Label(self.root, text="Set Password", font=("", 25))
        welcome_msg.grid(row=0, column=0, columnspan=2, pady=20)

        self.msg=Label(self.root,text="Enter a new password",bg='yellow')
        self.msg.grid(row=1,column=0,padx=10)

        passowrd1_label = Label(self.root, text='Password : - ')
        passowrd1_label.grid(row=2, column=0, padx=10, pady=5, sticky="e") 
        self.passowrd1 = Entry(self.root, width=30)
        self.passowrd1.grid(row=2, column=1, padx=10, pady=5)

        passowrd2_label = Label(self.root, text='Confirm Password : - ')
        passowrd2_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")  
        self.passowrd2 = Entry(self.root, width=30)
        self.passowrd2.grid(row=3, column=1, padx=10, pady=5)

        self.verify_button = Button(self.root, text='Set Password', command=lambda: self.set_passwd_confirm(user_email), width=50, bg='#4CAF50', fg="white", font=("Arial", 10, "bold"))
        self.verify_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        back_button = Button(self.root, text='Back', command=self.password_reset, width=50, bg='#9E9E9E', fg="white", font=("Arial", 10, "bold"))
        back_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

#updating password 
    def set_passwd_confirm(self,user_email):
        staff=self.user
        passwd1=self.passowrd1.get()
        passwd2=self.passowrd2.get()

        if not passwd1 or not passwd2:
            self.msg.config(text="Please enter password in both fields",bg='red')
        else:
            if passwd1==passwd2:
                result=staff.user_password_set(user_email,passwd1)
                if result:
                    status="completed"
                    staff.update_reset_request_status(user_email,self.user_email,status)
                    self.msg.config(text="Password Updated",bg='green')
                    self.verify_button.config(state="disabled")
                else:
                    self.msg.config(text="Error in settting new password",bg='red')
            else:
                self.msg.config(text="Please enter same password in both fields",bg='red')

    #screen clearing methods
    def clear_screen_tree(self):
        for widget in self.root.winfo_children():
            widget.grid_forget()         

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()        

#testing
root=tkinter.Tk()
hotel=Staff(root,'motel@stuff.come')
root.mainloop()
