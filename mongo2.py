from pymongo import MongoClient
import random
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import csv
import xlwt
import schedule

"""client=MongoClient()
db=client['test-db']
coll=db.coll
x=random.randint(1,100)
y=random.randint(1,100)

def ins_many():
    marks={'roll no':x,'marks':y}
    res=coll.insert_one(marks)
    print(res)"""
   
def write_csv():
    cursor = coll.find ({},{'roll no':x, 'marks':y})
    cursor=list(cursor)
    print(cursor)
    fields=['roll no','marks']
    with open('database1.csv', 'w',newline='') as outfile:
        csv_output=csv.writer(outfile,delimiter="|")
        csv_output.writerow(fields)
        for data in cursor:
            data1=data['roll no']
            data2=data['marks']
            csv_output.writerow([data1,data2])
   
def mail_csv():
    email_user = 'chaitanyaashtekar21@gmail.com'
    email_password = 'ChVM1234@'
    email_send = 'ptoke01@gmail.com'
    msg = MIMEMultipart()
    subject='Student Marks record'
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject']=subject
    filename='database1.csv'
    attachment  =open('F:\database1.csv','rt')
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)
    msg.attach(part)
    text = msg.as_string()
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('chaitanyaashtekar21@gmail.com','ChVM1234@')
    mail.sendmail('chaitanyaashtekar21@gmail.com','ptoke01@gmail.com',text)

schedule.every(2).seconds.do(ins_many)
time.sleep(1)
schedule.every(6).minutes.do(write_csv)
schedule.every(1).hour.do(mail_csv)

while 1:
    schedule.run_pending()
    time.sleep(1)
write_csv()       


