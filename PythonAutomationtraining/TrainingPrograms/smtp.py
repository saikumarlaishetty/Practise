import smtplib
from email.mime.text import MIMEText
msg = MIMEText("Sample text")
fromaddr = "slaishet@cisco.com"
toaddr   = "slaishet@cisco.com"
msg['Subject'] = 'test mail'
msg['From'] = fromaddr
msg['To'] = toaddr
try:
    s = smtplib.SMTP('mail.cisco.com')
    s.sendmail(fromaddr, [toaddr], msg.as_string())
    s.quit()
except Exception as e1:
    print(e1)
