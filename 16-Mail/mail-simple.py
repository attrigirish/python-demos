#Simple Mail

import smtplib

smtp = smtplib.SMTP('smtp.gmail.com:587')
smtp.ehlo()
smtp.starttls()
smtp.login("niecspi", "*Uncommon##")
msg = "Hello!" 
try:
    smtp.sendmail("niecspi@gmail.com","trainer.gkattri@gmail.com",msg)
    print("Email Sent Successfully")
except:
    print("Coudln't Send Email")
