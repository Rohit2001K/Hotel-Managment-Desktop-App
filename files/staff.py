import tkinter
from tkinter import *
from tkinter import ttk
from base import Staff_action

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

        self.check_out_button = Button(self.root, text='User Check Out', command=self.user_check_out, width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.check_out_button.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.account_updation_button = Button(self.root, text='User Account Updation', command='', width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.account_updation_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")


        self.food_list_button = Button(self.root, text='List New Food Iteam', command='', width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.food_list_button.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        self.food_requst_button = Button(self.root, text='User Food Requests', command='', width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.food_requst_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.booking_histroy_button = Button(self.root, text='Booking History', command=self.booking_histroy, width=20, bg='#4CAF50', fg="white", font=("Arial", 12, "bold"))
        self.booking_histroy_button.grid(row=3, column=0, padx=20, pady=10, sticky="w")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()    

    def user_check_out(self):
        self.clear_screen()
        staff=self.user
        result=staff.current_bookings()

        self.welcome_msg=Label(root,text=f"Current Booking",font=("", 25))
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

        self.welcome_msg=Label(root,text=f"Previous Bookings",font=("", 25))
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






root=tkinter.Tk()
hotel=Staff(root,'motel@stuff.come')
root.mainloop()
