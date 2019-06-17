import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

 
fromaddr = "niecspi@gmail.com"
toaddr = "trainer.gkattri@gmail.com"

#Message Creation
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Email From Python"

#Body Attachment
body = "Hello From Girish"
msg.attach(MIMEText(body, 'plain'))

#File Attachment
filename = "banner-1.jpg"
attachment = open(filename, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

#Server Connection and Mail Send
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(fromaddr, "*Uncommon##")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
