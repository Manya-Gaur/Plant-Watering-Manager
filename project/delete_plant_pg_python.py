#!C:\Users\Manya Gaur\AppData\Local\Programs\Python\Python39/python.exe
import cgi,os

print('content-type:text/html\r\n\r\n')

form=cgi.FieldStorage()

import cx_Oracle

#create connection

conn=cx_Oracle.connect('SYSTEM/manya2002@localhost')

# create cursor

cur=conn.cursor()
sql="SELECT user_id from current_user where s_no=(select max(s_no) from current_user)"
cur.execute(sql)
r=cur.fetchone()
user_id=r[0]

sql="SELECT plant_id,Plant_type_name from plant,plant_type where user_id="+str(user_id)+" and plant.plant_type_id=plant_type.plant_type_id"
cur.execute(sql)
r=cur.fetchall()
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
	<div id="dd" id="txt"><h1>Delete Plant</h1></div><br><br>
		<form enctype="multipart/form-data" method="post" action="delete_plant_python.py">
		''')
for i in r:
	print('		<input id="txt1" type="radio" id="%d" name="plant" value="%d %s">'%(i[0],i[0],i[1]))
	print('       <label id="txt" for="%d">%d %s</label><br>'%(i[0],i[0],i[1]))

print('''            <br><input id="txt" type="submit" name="delete" value="Delete Plant"/>
		</form>	
	</center>
</body>
</html>
	''')