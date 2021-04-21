from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib
# email package > sub package mime (define email format)>
# # HTML & PLain Text Content
#
template = Template(Path('template.html').read_text()) #look for template.html in the code
template.substitute()
message = MIMEMultipart()
message["from"] = 'Unkown User'
message['to'] = ''
message['subject'] = 'This is a test'
body = template.substitute({"name": "John"})
message.attach(MIMEText(body, 'html'))
message.attach(MIMEImage(Path('logo.jpg').read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('userid', 'password')
    smtp.send(message)
