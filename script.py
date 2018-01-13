from flask import Flask
import MySQLdb
from flask import request
import json
import datetime
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)


@app.route('/')

def index():
	db = MySQLdb.connect('',"root","greyscale","info" )

	cursor = db.cursor()

	dt=datetime.datetime.now()
	nxtdt=str(datetime.datetime.now() + datetime.timedelta(days=7))
	nxt=nxtdt[5:10]

	mnth=dt.month
	if mnth<10:
		mnth='0' + str(mnth)

	day=dt.day
	if day<10:
		day='0' + str(day)

	date=str(mnth) + '-' + str(day)
	print('%s' %(date))
	print('%s' %(nxt))

	cursor.execute("select email from db where substring(dob,6,5) <> '%s' ;" %(date)) 
	data = cursor.fetchall()
	cursor.execute("select * from db where substring(dob,6,5)= '%s';" % (date))
	data1 = list(cursor)
	dict=[]
	for e in data1:
	ins={}
	ins['emp_id']=int(e[0])
	ins['name']=str(e[1])
	dict.append(ins)
	#for row in data1
		
	for you in data:
		me = "sharanahuja8@gmail.com"

		# Create message container - the correct MIME type is multipart/alternative.
		msg = MIMEMultipart('alternative')
		msg['Subject'] = "Link"
		msg['From'] = me
		msg['To'] = str(you)

		# Create the body of the message (a plain-text and an HTML version).
		text = "Send a birthday wish to " 
		html = """\
		<html>
		  <head></head>
		  <body>
		    <p>Hi!<br>
		   
		  </body>
		</html>
		"""

		# Record the MIME types of both parts - text/plain and text/html.
		part1 = MIMEText(text, 'text')
		part2 = MIMEText(html, 'html')

		# Attach parts into message container.
		# According to RFC 2046, the last part of a multipart message, in this case
		# the HTML message, is best and preferred.
		msg.attach(part1)
		msg.attach(part2)

		# Send the message via local SMTP server.
		s = smtplib.SMTP('smtp.gmail.com',587)

		s.ehlo()

		s.starttls()

		s.login('sharanahuja8@gmail.com', 'hiiamsharan')
		# sendmail function takes 3 arguments: sender's address, recipient's address
		# and message to send - here it is sent as one string.
		s.sendmail(me, you, msg.as_string())

			#s.quit()
	# dict=[]
	# for e in data:
	# 	ins={}
	# 	ins['emp_id']=int(e[0])
	# 	ins['name']=str(e[1])
	# 	ins['dob']=str(e[3])
	# 	dict.append(ins)

	cursor.execute("select * from emp where substring(dob,6,5)= '%s';" % (nxt))

	data2 = cursor.fetchall()
	# dic=[]
	# for e in data:
	# 	ins={}
	# 	ins['emp_id']=int(e[0])
	# 	ins['name']=str(e[1])
	# 	ins['dob']=str(e[3])

	cursor.execute("select email from db where substring(dob,6,5) <> '%s' ;" %(date)) 
	
	for you in cursor:
		me = "sharanahuja8@gmail.com"

		# Create message container - the correct MIME type is multipart/alternative.
		msg = MIMEMultipart('alternative')
		msg['Subject'] = "Link"
		msg['From'] = me
		msg['To'] = str(you)

		# Create the body of the message (a plain-text and an HTML version).
		text = "%s" %(data1)
		html = """\
		<html>
		  <head></head>
		  <body>
		    <p>Send a birthday wish to<br>
		       
		    </p>
		  </body>
		</html>
		"""

		# Record the MIME types of both parts - text/plain and text/html.
		part1 = MIMEText(text, 'plain')
		part2 = MIMEText(html, 'html')

		# Attach parts into message container.
		# According to RFC 2046, the last part of a multipart message, in this case
		# the HTML message, is best andn preferred.
		msg.attach(part1)
		msg.attach(part2)

		# Send the message via local SMTP server.
		s = smtplib.SMTP('smtp.gmail.com',587)

		s.ehlo()

		s.starttls()

		s.login('sharanahuja8@gmail.com', 'hiiamsharan')
		# sendmail function takes 3 arguments: sender's address, recipient's address
		# and message to send - here it is sent as one string.
		s.sendmail(me, you, msg.as_string())

		#s.quit()

	return "hello"

@app.route('/update')

def upd():
	iden= request.args.get('id')
	name= request.args.get('name')
	dob= request.args.get('dob')
	phone= request.args.get('phone')
	email= request.args.get('email')
	designation= request.args.get('designation')
	address= request.args.get('address')
	hobby= request.args.get('hobby')
	db = MySQLdb.connect('',"root","greyscale","info" )

	cursor = db.cursor()

	

	cursor.execute("update db set name='%s', dob='%s', phone='%s', email='%s', designation='%s' address='%s', hobby='%s' where emp_id='%s';" % (name,dob,phone,email,designation,address,hobby,iden))

	db.close()

if __name__ == '__main__':
      app.run(host='0.0.0.0')
