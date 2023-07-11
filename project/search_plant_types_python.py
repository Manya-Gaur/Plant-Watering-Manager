#!C:\Users\Manya Gaur\AppData\Local\Programs\Python\Python39/python.exe
import cgi,os

print('content-type:text/html\r\n\r\n')

import cx_Oracle

#create connection

conn=cx_Oracle.connect('SYSTEM/manya2002@localhost')

# create cursor
cur=conn.cursor()
sql="SELECT * from plant_type p,water w where p.plant_type_id=w.plant_type_id order by plant_type_name"
cur.execute(sql)
r=cur.fetchall()
conn.commit()

print("""
<html>
<head>
	    <style>
	    .tableFixHead {
        overflow-y: auto;
        height: 475px;
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
<body>
<center>
<div id="dd" id="txt"><h1>Plant Types</h1></div><br><br>
<div class="tableFixHead">
<table style="width:60%" align="center">
<thead>
  <tr>
    <th id="txt">Plant Type Id</th>
    <th id="txt">Plant Type</th>
    <th id="txt">Season</>
    <th id="txt">Freq of Watering</th>
    <th id="txt">Amount of Water</th>
  </tr>
</thead>  
  """)
for i in r:
	print('  <tr>')
	print('    <td  id="txt" align="center">%d</td>'%i[0])
	print('    <td  id="txt" align="center">%s</td>'%i[1])
	print('    <td  id="txt" align="center">%s</td>'%i[2])
	print('    <td  id="txt" align="center">%s</td>'%i[4])
	print('    <td  id="txt" align="center">%d</td>'%i[5])
	print('  </tr>')
print("""
</table>
</div>	
</center>
</body>
</html>
	""")