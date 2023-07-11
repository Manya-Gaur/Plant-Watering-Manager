#!C:\Users\Manya Gaur\AppData\Local\Programs\Python\Python39/python.exe
import cgi,os

print('content-type:text/html\r\n\r\n')

form=cgi.FieldStorage()
string=str(form.getvalue("plant")).split(" ")
plant_id=string[0]
plant_type_id=str(form.getvalue("plant_type_id"))
date=str(form.getvalue("last_watering_date"))

import cx_Oracle

#create connection

conn=cx_Oracle.connect('SYSTEM/manya2002@localhost')

# create cursor
cur=conn.cursor()
sql="SELECT user_id from current_user where s_no=(select max(s_no) from current_user)"
cur.execute(sql)
r=cur.fetchone()
user_id=r[0]
sql="UPDATE plant set plant_type_id="+plant_type_id+",last_watering_date=TO_DATE('"+str(date)+"','YYYY-MM-DD') where user_id="+str(user_id)+" and plant_id="+plant_id
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
			#txt1{
				width:25px;
				height:25px;
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
<div id="dd" id="txt"><h1>Edited Successfully!</h1></div><br><br>
<A href="http://localhost/project/Customer.html"><button id="txt">Continue</button></A>
</center>
</body>
</html>
	''')
