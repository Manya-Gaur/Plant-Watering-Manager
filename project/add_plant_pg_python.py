#!C:\Users\Manya Gaur\AppData\Local\Programs\Python\Python39/python.exe
import cgi,os

print('content-type:text/html\r\n\r\n')

form=cgi.FieldStorage()

import cx_Oracle

#create connection

conn=cx_Oracle.connect('SYSTEM/manya2002@localhost')

# create cursor

cur=conn.cursor()

sql="SELECT plant_type_id,plant_type_name from plant_type order by plant_type_name"
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
	<body><center>
		<div id="dd" id="txt"><h1>Add Plant</h1></div><br><br>
		<form enctype="multipart/form-data" method="post" action="Add_plant_python.py">
			<label id="txt" for="plant_type_id">Enter Plant Type Id:</label><br>
			<input id="txt" type="number" placeholder="Refer the Below Table" name="plant_type_id"/><br><br>
			<label id="txt" for="last_watering_date">Enter the last date of watering</label><br>
			<input id="txt" type="date" name="last_watering_date"/><br><br>
			<input id="txt" type="submit" name="submit">
		</form>	
		<br><br>
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
for i in r:
    print('  <tr>')
    print('    <td id="txt" align="center">%d</td>'%i[0])
    print('    <td id="txt" align="center">%s</td>'%i[1])
    print('  </tr>')
print('''  
</tbody></table></div><br><br>
<div id="txt">(Scroll Table for More Plant Types!)</div>
	</body></center>
</html>
''')