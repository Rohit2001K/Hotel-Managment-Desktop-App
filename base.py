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



