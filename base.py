import mysql.connector as ms



my_sql=ms.connect(host='localhost',user='',passwd='',database='test')
if my_sql.is_connected():
    cursor=my_sql.cursor()


class User_actions:
 
    def __init__(self, user=None, password=None):
        self.user = user
        self.password = password

    def login_user(self):
        cursor.execute("SELECT uid FROM users WHERE fname=%s AND password=%s", (self.user, self.password))
        user_auth = cursor.fetchone()
        if user_auth:
            user_name=self.user
            return user_auth,user_name
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

    def room_booking_conform(self, uid, room_no, check_in_date, check_out_date, days):
        try:
            cursor.execute('UPDATE rooms SET available=False WHERE room_no=%s', (room_no,))
            my_sql.commit()
            cursor.execute('INSERT INTO bookings (uid, room_no, check_in, check_out, days) VALUES (%s, %s, %s, %s, %s)',(uid, room_no, check_in_date, check_out_date, days))
            my_sql.commit()
        except :
            print("Error in inserting:")




        
        
