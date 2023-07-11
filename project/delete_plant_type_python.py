#!C:\Users\Manya Gaur\AppData\Local\Programs\Python\Python39/python.exe
import cgi,os

print('content-type:text/html\r\n\r\n')

form=cgi.FieldStorage()
string=str(form.getvalue("plant")).split(" ")
plant_type_id=string[0]

import cx_Oracle

#create connection

conn=cx_Oracle.connect('SYSTEM/manya2002@localhost')

# create cursor
cur=conn.cursor()

sql="DELETE from water where plant_type_id="+plant_type_id
cur.execute(sql)
conn.commit()

sql="delete from plant where plant_type_id="+plant_type_id
cur.execute(sql)
conn.commit()
sql="delete from plant_type where plant_type_id="+plant_type_id
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
<div id="dd" id="txt"><h1>Deleted Successfully!</h1></div><br><br>
<A href="http://localhost/project/Delete.html"><button id="txt">Continue</button></A>
</center>
</body>
</html>
	""")
