import mysql.connector
from mysql.connector import Error
try:
   mySQLconnection = mysql.connector.connect(host='localhost',
                             database='test',
                             user='shiv',
                             password='tarun')
   sql_select_Query = "select * from vision"
   cursor = mySQLconnection .cursor()
   cursor.execute(sql_select_Query)
   records = cursor.fetchall()
   print("Total number of rows in python_developers is - ", cursor.rowcount)
   f= open("vision.md","w")
   heads=cursor.description
   for row in records:
       i=0
       for head in heads:
          h="#"+str(head[0])+"\n"
          r=str(row[i])+"\n"
          f.write(h)
          f.write(r)
          i=i+1
   cursor.close()
   
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(mySQLconnection .is_connected()):
        mySQLconnection.close()
        f.close()
        print("MySQL connection is closed")
