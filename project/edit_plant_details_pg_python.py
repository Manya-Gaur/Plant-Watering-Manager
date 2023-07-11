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
	    .tableFixHead {
        overflow-y: auto;
        height: 106px;
      }
      .tableFixHead thead th {
        position: sticky;
        top: 0;
      }
      table {
        border-collapse: collapse;
        width: 100%;
      }
      th,
      td {
        padding: 8px 16px;
        border: 1px solid #ccc;
      }
      th {
        background: #eee;
      }     
	        body{
				background-image: url("bg4.jpeg");
			}
			#txt{
				width:737px;
				height:50px;
				font-size:20px;
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
	<center><div id="dd" id="txt"><h1>Select Plant To Edit</h1></div><br><br></center>
		<form enctype="multipart/form-data" method="post" action="edit_plant_details_python.py">
		''')
for i in r:
	print('		<input id="txt1" type="radio" id="%d" name="plant" value="%d %s">'%(i[0],i[0],i[1]))
	print('       <label id="txt" for="%d">%d %s</label><br>'%(i[0],i[0],i[1]))

print('''            
	        <br><label id="txt" for="plant_type_id">Enter New Plant Type Id:</label><br>
			<input id="txt" type="number" placeholder="Refer the Below Table" name="plant_type_id"/><br><br>
			<label id="txt" for="last_watering_date">Enter the New last date of watering</label><br>
			<input id="txt" type="date" name="last_watering_date"/><br><br>
	        <input id="txt" type="submit" name="edit" value="Edit Plant"/>
		</form>	
		<br><br><br>
<div class="tableFixHead">		
<table style="width:60%" align="center">
<thead>
  <tr>
    <th id="txt">Plant Type Id</th>
    <th id="txt">Plant Type</th>
  </tr>
</thead>
<tbody>  
  ''')
sql="SELECT plant_type_id,plant_type_name from plant_type order by plant_type_name"
cur.execute(sql)
r=cur.fetchall()
conn.commit()
for i in r:
    print('  <tr>')
    print('    <td id="txt" align="center">%d</td>'%i[0])
    print('    <td id="txt" align="center">%s</td>'%i[1])
    print('  </tr>')
print('''  
</tbody></table></div><br><br>
<div id="txt">(Scroll Table for More Plant Types!)</div>
	</center>
</body>
</html>
	''')