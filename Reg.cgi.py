#!C:\Python27\python.exe

import cgi
import mysql.connector as conn

def htmlTop():
   print("""Content-type:text/html\n\n
             <!DOCTYPE html>
             <html lang="en">
                 <head>
                     <meta charset="utf-8"/>
                     <title>My Server Side Template</title>
                 </head>
                 <body>""")
def htmlTail():
    print("""</body>
        </html>""")
def connectDB():
    db=conn.connect(host="localhost",user="root",passwd="",db="project")
    cursor=db.cursor()
    return db,cursor
def createInputRecord():
    people=[]
    formData=cgi.FieldStorage()
    Username=formData.getvalue("username")
    Password=formData.getvalue("Password")
    UserType=formData.getvalue("type")
    people.append([Username,Password,UserType])
    return people

def insertRegRecord(db,cursor,people):
   for each in people:
      sql="insert into register(Username,Password,UserType) values('{0}','{1}','{2}')".format(each[0],each[1],each[2])
      cursor.execute(sql)
   db.commit()

#main program
if __name__=="__main__":
    try:
        htmlTop()
        db,cursor=connectDB()
        people=createInputRecord()
        insertRegRecord(db,cursor,people)
        print("<script>location.href='../Video/index.html';</script>")
        htmlTail()
        
    except:
        cgi.print_exception
