#!C:\Users\Manya Gaur\AppData\Local\Programs\Python\Python39/python.exe
import cgi,os

print('content-type:text/html\r\n\r\n')

form=cgi.FieldStorage()
fname=str(form.getvalue("fname"))
lname=str(form.getvalue("lname"))
phone_no=str(form.getvalue("phone_no"))
email=str(form.getvalue("email"))
password=str(form.getvalue("password"))
name=fname+" "+lname

import cx_Oracle

#create connection

conn=cx_Oracle.connect('SYSTEM/manya2002@localhost')

# create cursor

cur=conn.cursor()

sql="SELECT max(user_id) from USERS where type='ADMIN'"
cur.execute(sql)
r=cur.fetchone()
user_id=r[0]+1

sql="insert into users values("+str(user_id)+",'"+name+"',"+phone_no+",'"+email+"','ADMIN',"+"'"+password+"')"
cur.execute(sql)


conn.commit()

print('''
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
		<div id="dd" id="txt">
		<h1>Admin Added Successfully</h1>	
		</div>
		<br><br>
		<A href="http://localhost/project/Admin.html"><button id="txt">CONTINUE</button></A>
		</center>	 
	</body>
</html>
''')
