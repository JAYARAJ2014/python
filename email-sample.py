from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
# email package > sub package mime (define email format)>
# # HTML & PLain Text Content
#

message = MIMEMultipart()
message["from"] = 'Unkown User'
message['to'] = ''
message['subject'] = 'This is a test'
message.attach(MIMEText("Body"))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('', '')
    smtp.send(message)
