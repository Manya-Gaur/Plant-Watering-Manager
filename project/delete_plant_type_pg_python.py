#!C:\Users\Manya Gaur\AppData\Local\Programs\Python\Python39/python.exe
import cgi,os

print('content-type:text/html\r\n\r\n')



import cx_Oracle

#create connection

conn=cx_Oracle.connect('SYSTEM/manya2002@localhost')

# create cursor
cur=conn.cursor()


sql="SELECT plant_type_id,Plant_type_name from plant_type order by plant_type_name"
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
	<div id="dd" id="txt"><h1>Delete Plant Type</h1></div><br><br>
		<form enctype="multipart/form-data" method="post" action="delete_plant_type_python.py">
		''')
for i in r:
	print('		<input id="txt1" type="radio" id="%d" name="plant" value="%d %s">'%(i[0],i[0],i[1]))
	print('       <label id="txt" for="%d">%d %s</label><br>'%(i[0],i[0],i[1]))

print('''            <br><input id="txt" type="submit" name="delete" value="Delete Plant Type"/>
		</form>	
	</center>
</body>
</html>
	''')