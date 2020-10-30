from config import rules

import smtplib
import requests
from email.mime.text import MIMEText


def send_smtp_email(subject, body):
    """
    send the email by smtp service
    :param subject: subject of email
    :param body: body of email
    :return: none
    """
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "z.jamshidi1378@gmail.com"
    msg['To'] = rules['email']['receiver']

    with smtplib.SMTP('smtp.mailtrap.io', 2525) as mail_server:
        mail_server.login("4f68dbf8fe2f8c", "d7f97e9207f180")
        mail_server.sendmail(msg['From'], msg['To'], msg.as_string())
