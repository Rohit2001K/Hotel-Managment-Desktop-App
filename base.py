import mysql.connector as ms



my_sql=ms.connect(host='localhost',user='',passwd='',database='')
if my_sql.is_connected():
    cursor=my_sql.cursor()


class User_actions:
    def __init__(self,user,password):
        self.user=user
        self.password=password
    
    def login_user(self):
        cursor.execute(f"select uid from users where fname='{self.user}' and password='{self.password}'")
        user_auth=cursor.fetchone()
        if user_auth:
            return self.user
            
        else:
            return False
        
        



        
        
