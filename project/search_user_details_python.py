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
sql="SELECT * from users where email='"+email+"' and phone_no="+phone_no
cur.execute(sql)
r=cur.fetchone()
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
<div id="dd" id="txt"><h1>User Details</h1></div><br><br>
	""")
print("<br><div id='txt' >User id: %d</div><br>"%r[0])
print("<br><div id='txt' >Name : %s</div><br>"%r[1])
print("<br><div id='txt' >Phone No : %d</div><br>"%r[2])
print("<br><div id='txt' >Email : %s</div><br>"%r[3])
print("<br><div id='txt' >Password : %s</div>"%r[5])
print("""
</center>
</body>
</html>
	""")