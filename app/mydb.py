#coding=utf-8
import MySQLdb
from _mysql import result
from werkzeug.security import generate_password_hash,check_password_hash



class mydb():
    def __init__(self,host='69.164.202.55',user='test',passwd='test',db='test',port=3306):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
    
    def mysqlconnect(self):
        return MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=self.port)
    

    
    def checklogin(self,mail,password):
        self.mail = mail
        self.password = password
        conn=self.mysqlconnect()
        cur=conn.cursor()
        if cur.execute('select * from users where mail ="%s" and password ="%s"' %(self.mail,self.password)):
            return 1
    
    def checkmail(self,mail):
        self.mail = mail
        conn=self.mysqlconnect()
        cur=conn.cursor()
        if cur.execute('select * from users where mail ="%s"' %self.mail):
            return 1 
    
    def checkusername(self,username):
        self.username = username
        conn=self.mysqlconnect()
        cur=conn.cursor()
        if cur.execute('select * from users where username ="%s"' % self.username):
            return 1             
        
    
    def saveuser(self,username,password,mail): 
        createtableusers = """CREATE TABLE users (

         username  CHAR(20) not null unique,
         password CHAR(20) not null,

         mail char(60) unique,
         dt timestamp not null default now(),
         primary key(username)
         )"""        
    
        conn=self.mysqlconnect()
        cur=conn.cursor()
        if cur.execute('show tables like "users"') == 0:
            cur.execute(createtableusers)
    #            cur.execute('drop table if exists message')
#        try:
    #            cur.execute(self.createteble)
        self.username = username
        self.mail = mail    
        self.passwd = password

        cur.execute('insert into users(username,password,mail) values("%s","%s","%s")'%(self.username,self.passwd,self.mail))

        result = cur.fetchall()



        result = cur.fetchall()

        cur.close()
        conn.commit()
        conn.close()

#        except:
#            conn.rollback()
            
if __name__ == '__main__':
    host='69.164.202.55'
    user='test'
    passwd='test'
    db='test'
    port=3306
    mydb = mydb()
#    print mydb.checklogin("eree2323232144", '34333122344')
    print mydb.checkmail("223231233433")
#    mydb.saveuser('eree2323232144r', '34333122344', '223231233433')
    
    