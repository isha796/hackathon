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

	cursor.execute("select * from emp where substring(dob,6,5)= '%s';" % (date))

	data = cursor.fetchall()
	dict=[]
	for e in data:
		ins={}
		ins['emp_id']=int(e[0])
		ins['name']=str(e[1])
		ins['dob']=str(e[3])
		dict.append(ins)

	cursor.execute("select * from emp where substring(dob,6,5)= '%s';" % (nxt))

	data = cursor.fetchall()
	dic=[]
	for e in data:
		ins={}
		ins['emp_id']=int(e[0])
		ins['name']=str(e[1])
		ins['dob']=str(e[3])
		dic.append(ins)

	db.close()

	me = 'sharanahuja8@gmail.com'
	you = ['ishanki.kansal796@gmail.com','sahil.070197@gmail.com','nishantvarshney28@gmail.com']

	for i in you:
		msg = MIMEMultipart('alternative')
		msg['Subject'] = "Link"
		msg['From'] = me
		msg['To'] = i

		# Create the body of the message (a plain-text and an HTML version).
		text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
		html = """\
		<html>
		  <head></head>
		  <body>
		    <p>Hi!<br>
		       <h1>How</h1> are you?<br>
		       Here is the <a href="http://www.python.org">link</a> you wanted.
		    </p>
		  </body>
		</html>
		"""

		# Record the MIME types of both parts - text/plain and text/html.
		part1 = MIMEText(text, 'plain')
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
		s.login('sharanahuja8@gmail.com','hiiamsharan')
		# sendmail function takes 3 arguments: sender's address, recipient's address
		# and message to send - here it is sent as one string.
		s.sendmail(me, i, msg.as_string())
		#s.quit()

	return json.dumps(dict)

if __name__ == '__main__':
      app.run(host='0.0.0.0')
