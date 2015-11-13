#coding:utf8
import smtplib
from email.mime.text import MIMEText

msg =  'this is a test !'
msg =  MIMEText(msg)

msg['Subject'] = 'This is a test'
msg['From'] =  'from@example.com'
msg['To'] =  'to@example.com'

s =  smtplib.SMTP('smtp.example.com')
s.login('username' 'password')
s.sendmail('from@example.com', 'to@example.com', msg.as_string())
s.quit()


