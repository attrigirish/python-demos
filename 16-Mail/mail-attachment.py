import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "niecspi@gmail.com"
toaddr = "trainer.gkattri@mail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Email From Python"
 
body = "Hello From Girish"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "sample.txt"
attachment = open(filename, "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(fromaddr, "*Uncommon##")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
