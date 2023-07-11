#!C:\Users\Manya Gaur\AppData\Local\Programs\Python\Python39/python.exe
import cgi,os

print('content-type:text/html\r\n\r\n')

form=cgi.FieldStorage()
plant_type_name=str(form.getvalue("plant_type_name"))
season=str(form.getvalue("season"))
freq=str(form.getvalue("freq"))
amt=str(form.getvalue("amt"))

import cx_Oracle

#create connection

conn=cx_Oracle.connect('SYSTEM/manya2002@localhost')

# create cursor

cur=conn.cursor()

sql="SELECT max(plant_type_id) from plant_type"
cur.execute(sql)
r=cur.fetchone()
plant_type_id=r[0]+1

sql="insert into plant_type values("+str(plant_type_id)+",'"+plant_type_name+"','"+season+"')"
cur.execute(sql)
conn.commit()
sql="insert into water values("+str(plant_type_id)+","+freq+","+amt+")"
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
		<h1>Plant Type Added</h1>	
		</div>
		<br><br>
		<A href="http://localhost/project/Admin.html"><button id="txt">CONTINUE</button></A>
		</center>	 
	</body>
</html>
''')
