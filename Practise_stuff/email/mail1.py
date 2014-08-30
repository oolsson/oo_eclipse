'''
Created on Jun 9, 2012

@author: oo
'''
from datetime import date
from email.mime.text import MIMEText
import smtplib
import time
from email.mime.multipart import MIMEMultipart



 
def emailsend(DATA):
    SMTP_SERVER = "smtp.live.com"
    SMTP_PORT = 587
    SMTP_USERNAME = "oskarolsson_1@hotmail.com"
    SMTP_PASSWORD = "4818*0h0*Hm"
    EMAIL_TO = ["o.h.olsson@gmail.com"]
    EMAIL_FROM = "oskarolsson_1@hotmail.com"
    EMAIL_SUBJECT = "Trading update"
    DATE_FORMAT = "%d/%m/%Y"
    EMAIL_SPACE = ", "
#     msg = MIMEText(DATA)
    msg = MIMEMultipart()
    msg['Subject'] = 'oo'
    msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
    msg['From'] = EMAIL_FROM
    
    msg.preamble = 'oo'
    filename = "Nt.txt"
    f = file(filename)
    
    attachment = MIMEText(f.read())
    attachment.add_header('Content-Disposition', 'attachment', filename=filename)           
    msg.attach(attachment)
    
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    time.sleep(2)
    mail.quit()
     
emailsend('holla')