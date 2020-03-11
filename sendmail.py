import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

RECEIVER_EMAIL = ['<email_address>']

SENDER_EMAIL = "no-reply@domain.com"
SUBJECT = "Let's go for lunch!!!"


def sendmail(subject, body, receiver, sender):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['To'] = ', '.join(receiver)
    msg['From'] = sender

    html_body = MIMEText(body, 'html')
    msg.attach(html_body)
    try:
        server = smtplib.SMTP('<email_server>:<port>')
        server.sendmail(sender, receiver, msg.as_string())
        print("Mail sent")
        server.quit()
    except smtplib.SMTPException:
        print("Error: unable to send mail")

    return "Mail sent"
