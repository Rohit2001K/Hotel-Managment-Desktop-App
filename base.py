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
            return self.user
        else:
            return False
        
    def create_user(self,fname,lname,mno,email,password):
        try:
            cursor.execute('INSERT INTO Users (fname, lname, mobile, email, password) VALUES (%s, %s, %s, %s, %s)', (fname, lname, mno, email, password))
            result=my_sql.commit()
            return True
        except:
            return False 
        
        




        
        
