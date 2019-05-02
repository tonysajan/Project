#!C:\Python27/python.exe
import cgi
import mysql.connector as conn
def htmlTop():
    print("""Content-type:text/html\n\n
             <!DOCTYPE html>
             <html lang="en">
                <head>
                    <meta charset ="utf-8"/>
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
    username=formData.getvalue("username")
    password=formData.getvalue("password")
    people.append([username,password])
    return people

def checklogin(db,cursor,people):
    for each in people:
        sql="select usertype from register where Username='{0}' and Password='{1}'".format(each[0],each[1])
        cursor.execute(sql)
        people=cursor.fetchall()
        for r in people:
            if(r[0]=="disabled"):
                print("<script>location.href='../Video/Disabled/index.html';</script>")
            elif(r[0]=="non"):
                 print("<script>location.href='../Video/NonDisabled/index.html';</script>")
            

#main program
if __name__ == "__main__":
    try:
        htmlTop()
        db,cursor=connectDB()
        people=createInputRecord()
        checklogin(db,cursor,people)
        print("<script>alert('Invalid login credentials');</script>")
        print("<script>location.href='../Public/Login.html';</script>")
        htmlTail()

    except:
        cgi.print_exception
