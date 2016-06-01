import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of email is here")

msg['Subject'] = "An Email Alert"
msg['From'] = "ryan@pythonscraping.com"
msg['To'] = "webmaster@pyhtonscraping.com"

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
