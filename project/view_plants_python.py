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
sql="create view view1 as SELECT plant_id,plant.plant_type_id,Plant_type_name,last_watering_date,season from plant,plant_type where user_id="+str(user_id)+" and plant.plant_type_id=plant_type.plant_type_id"
cur.execute(sql)
conn.commit()
sql="SELECT plant_id,Plant_type_name,TO_CHAR(last_watering_date,'DD-MM-YYYY') last_water_date,season,freq_of_watering,water_required from view1,water where view1.plant_type_id=water.plant_type_id order by plant_id"
cur.execute(sql)
r=cur.fetchall()
sql="drop view view1"
cur.execute(sql)
conn.commit()

print('''
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
	<body><center>
		<div id="dd" id="txt"><h1>My Plants</h1></div><br><br></center>
<div class="tableFixHead">		
<table style="width:60%" align="center">
<thead>
  <tr>
    <th id="txt">Plant Id</th>
    <th id="txt">Plant Type</th>
    <th id="txt">Last Watering Date</th>
    <th id="txt">Season</>
    <th id="txt">Freq of Watering (days) </th>
    <th id="txt">Amount of Water (ml) </th>
  </tr>
 </thead> 
  ''')
for i in r:
    print('  <tr>')
    print('    <td id="txt" align="center">%d</td>'%i[0])
    print('    <td id="txt" align="center">%s</td>'%i[1])
    print('    <td id="txt" align="center">%s</td>'%i[2])
    print('    <td id="txt" align="center">%s</td>'%i[3])
    print('    <td id="txt" id="txt" align="center">%d</td>'%i[4])
    print('    <td id="txt" align="center">%d</td>'%i[5])
    print('  </tr>')
print('''  
</table></div>
	</body></center>
</html>
''')
