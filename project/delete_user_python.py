#!C:\Users\Manya Gaur\AppData\Local\Programs\Python\Python39/python.exe
import cgi,os

print('content-type:text/html\r\n\r\n')

form=cgi.FieldStorage()
email=str(form.getvalue("email"))
phone_no=str(form.getvalue("phone_no"))


import cx_Oracle

#create connection

conn=cx_Oracle.connect('SYSTEM/manya2002@localhost')

# create cursor

cur=conn.cursor()
sql="SELECT user_id from users where email='"+email+"' and phone_no="+phone_no
cur.execute(sql)
r=cur.fetchone()
user_id=r[0]
sql="DELETE from plant where user_id="+str(user_id)
cur.execute(sql)
conn.commit()
sql="DELETE from users where user_id="+str(user_id)
cur.execute(sql)
conn.commit()

print("""
<html>
<head>
	    <style>    
	        body{
				background-image: url("bg4.jpeg");
			}
			#txt{
				width:737px;
				height:50px;
				font-size:25px;
			}
			#dd{
				color:white;
				background-color:black;
				padding-top:10px;
				height:75px;
			}
		</style>
</head>
<body>
<center>
<div id="dd" id="txt"><h1>User succcessfully Deleted!</h1></div><br><br>
<A href='http://localhost/project/Admin.html'><button id="txt">Continue</button></A>
</center>
</body>
</html>
	""")