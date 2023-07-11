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


sql="UPDATE plant_type set season='"+season+"' where plant_type_name='"+plant_type_name+"'"
cur.execute(sql)
conn.commit()
sql="SELECT plant_type_id from plant_type where plant_type_name='"+plant_type_name+"'"
cur.execute(sql)
r=cur.fetchone()
plant_type_id=r[0]
conn.commit()
sql="UPDATE water set freq_of_watering="+freq+" where plant_type_id='"+str(plant_type_id)+"'"
cur.execute(sql)
conn.commit()
sql="UPDATE water set water_required="+amt+" where plant_type_id='"+str(plant_type_id)+"'"
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
		<h1>Plant Type Updated</h1>	
		</div>
		<br><br>
		<A href="http://localhost/project/Admin.html"><button id="txt">CONTINUE</button></A>
		</center>	 
	</body>
</html>
''')
