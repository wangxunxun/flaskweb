#coding=utf-8
import MySQLdb
from _mysql import result



class mydb():
    def __init__(self,host,user,passwd,db,port):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
    def mysqlconnect(self):
        return MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=self.port)
    
    def saveuser(self,username1,password1,mail1): 
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

        print 1
        cur.execute('insert into users(username,password,mail) values("%s","%s","%s")'%(username1,password1,mail1))

        result = cur.fetchall()

        print(result)

        result = cur.fetchall()
        print 1
        print(result)
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
    mydb1 = mydb(host,user,passwd,db,port)
    mydb1.saveuser('ereer', '3434', '2323')
    
    