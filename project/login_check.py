#!C:\Users\Manya Gaur\AppData\Local\Programs\Python\Python39/python.exe
import cgi,os

print('content-type:text/html\r\n\r\n')

form=cgi.FieldStorage()
email=str(form.getvalue("email"))
password=str(form.getvalue("password"))

import cx_Oracle

#create connection

conn=cx_Oracle.connect('SYSTEM/manya2002@localhost')

# create cursor

cur=conn.cursor()

sql="SELECT user_id,password,type from USERS where email= :e"
cur.execute(sql,{'e':email})
r=cur.fetchone()
user_id=r[0]
user_type=r[2]
pass_from_db=r[1]
sql="SELECT max(s_no) from current_user"
cur.execute(sql)
r=cur.fetchone()
s_no=r[0]+1
if((password==pass_from_db) and (user_type=='USER')):
    sql="insert into current_user values("+str(user_id)+","+str(s_no)+")"
    cur.execute(sql)

conn.commit()

if(password==pass_from_db):
	print("""<html><head>
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
</head><body><center>""")
	print('<div id="dd" id="txt"><h2>Successfully Logged In</h2></div><br><br>')
	if(user_type=='USER'):
	    print('<A href="http://localhost/project/Customer.html"><button id="txt">Continue</button></A>')
	else:
	    print('<A href="http://localhost/project/Admin.html"><button id="txt">Continue</button></A>')   
	print('</center></body></html>')
else:
	print("""<html><head>
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
</head><body><center>""")
	print('<div id="dd" id="txt"><h2>Login Failed</h2></div><br><br>')
	print('<button id="txt"><A href="http://localhost/project/Login.html">Try Again</A></button>')
	print('</center></body></html>')
