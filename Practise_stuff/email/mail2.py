from datetime import date
from email.mime.text import MIMEText
from email.MIMEImage import MIMEImage
import smtplib
import time
from email.mime.multipart import MIMEMultipart

f = codecs.open("C:\Users\oskar\Documents\doc_no_backup\python_crap\reports\AA.pdf", encoding="ISO8859-1", mode="rb")
# fp=open("C:\Users\oskar\Documents\doc_no_backup\python_crap\reports\AA.pdf","rb")
# fa = open("C:\Users\oskar\Documents\doc_no_backup\python_crap\reports\finrep.pdf",'r', buffering=-1)
# a=file("C:\Users\oskar\Documents\doc_no_backup\python_crap\reports\finrep.pdf").read()

 
# def emailsend(DATA):
#     SMTP_SERVER = "smtp.live.com"
#     SMTP_PORT = 587
#     SMTP_USERNAME = "oskarolsson_1@hotmail.com"
#     SMTP_PASSWORD = "4818*0h0*Hm"
#     EMAIL_TO = ["o.h.olsson@gmail.com"]
#     EMAIL_FROM = "oskarolsson_1@hotmail.com"
#     EMAIL_SUBJECT = "Trading update"
#     DATE_FORMAT = "%d/%m/%Y"
#     EMAIL_SPACE = ", "
# #     msg = MIMEText(DATA)
#     msg = MIMEMultipart()
#     msg = MIMEMultipart()
#     msg.attach(MIMEText(file("C:\Users\oskar\Documents\doc_no_backup\python_crap\reports\finrep.pdf",'r').read()))     
#     msg['Subject'] = 'oo'
#     msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
#     msg['From'] = EMAIL_FROM
#       
# #     msg.preamble = 'oo'   
#     #attach text-----------------------------------
# #     filename = "Nt.txt"
# #     f = file(filename) 
# #     attachment = MIMEText(f.read())
# #     attachment.add_header('Content-Disposition', 'attachment', filename=filename)           
# #     msg.attach(attachment)
#       
#     mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#     mail.starttls()
#     mail.login(SMTP_USERNAME, SMTP_PASSWORD)
#     mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
#     time.sleep(2)
#     mail.quit()
#        
# emailsend('holla')