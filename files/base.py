import mysql.connector as ms

my_sql=ms.connect(host='localhost',user='',passwd='',database='test')
if my_sql.is_connected():
    cursor=my_sql.cursor()


class User_actions:
 
    def __init__(self, user=None, password=None):
        self.user = user
        self.password = password

    def login_user(self):
        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (self.user, self.password))
        user_auth = cursor.fetchall()
        if user_auth:
            return user_auth
        else:
            return False


        
    def create_user(self,fname,lname,mno,email,password):
        try:
            cursor.execute('INSERT INTO Users (fname, lname, mobile, email, password) VALUES (%s, %s, %s, %s, %s)', (fname, lname, mno, email, password))
            result=my_sql.commit()
            return True
        except:
            return False 
        

    def room_booking(self):
        cursor.execute('select room_no,beds,price from Rooms where available=True')
        result=cursor.fetchall()
        return result    

    def price_fetch(self,room_no):
        cursor.execute('select price from rooms where room_no=%s',(room_no,))
        result=cursor.fetchall()
        result=result[0][0]
        return result

    def room_booking_conform(self,email, room_no, check_in_date, check_out_date, days,price):
        try:
            cursor.execute('UPDATE rooms SET available=False WHERE room_no=%s', (room_no,))
            my_sql.commit()
            cursor.execute('INSERT INTO bookings (email, room_no, check_in, check_out, days,price) VALUES (%s, %s, %s, %s, %s,%s)',(email, room_no, check_in_date, check_out_date, days,price))
            my_sql.commit()
        except :
            print("Error in inserting:")



    def user_account(self,email):
        cursor.execute('select * from users where email=%s',(email,))
        result=cursor.fetchall()
        return result
        
    def user_spends(self,email):
        #room booking total 
        cursor.execute('select price from bookings where email=%s',(email,))   
        room_booking_price=cursor.fetchall()
        total_room_price=0
        for i in room_booking_price:
            for j in i:
                total_room_price+=int(j)

        #food total


        return total_room_price   
    
    def user_booking_history(self,email):
        cursor.execute('select room_no,check_in,check_out,days,price from bookings where email=%s',(email,))
        result=cursor.fetchall()
        return result


#staff dashboard
class Staff_action:
    def __init__(self,email):
        self.email=email

    def staff_info(self):
        cursor.execute('SELECT fname FROM users where email=%s',(self.email,))
        result=cursor.fetchone()
        return result[0]

    def current_bookings(self):
        cursor.execute('SELECT * FROM bookings where check_out_status!="Completed"')
        result = cursor.fetchall()
        return result

    def booking_history(self):
        cursor.execute('SELECT * FROM bookings where check_out_status="Completed"')
        result = cursor.fetchall()
        return result

    def check_out(self,id,room_no):
        try:
            cursor.execute('update bookings set check_out_status="Completed" where booking_id=%s',(id,))
            cursor.execute('update rooms set available=True where room_no=%s',(room_no,))
            my_sql.commit()
            return True
        except Exception as e:
            my_sql.rollback()  # Rollback the transaction in case of an error
            print(f"Error occurred: {e}")
            return False


    def show_food_items(self):
        cursor.execute('select * from food_items')
        result=cursor.fetchall()
        return result
    
    def list_new_item(self,name,price):
        try:
            cursor.execute('insert into food_items (name,price) values (%s,%s)',(name,price,))
            my_sql.commit()
            return True
        except:
            return False
    
    def food_item_status(self,status,name):
        try:
            cursor.execute('UPDATE food_items SET availability = %s WHERE name = %s', (status, name))
            my_sql.commit()
            return True
        except:
            return False

