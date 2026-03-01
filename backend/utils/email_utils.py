import smtplib
from email.mime.text import MIMEText
from flask import current_app

def send_email(to, subject, html_content):

    msg = MIMEText(html_content, "html")
    msg["Subject"] = subject
    msg["From"] = current_app.config["MAIL_DEFAULT_SENDER"]
    msg["To"] = to

    with smtplib.SMTP(
        current_app.config["MAIL_SERVER"],
        current_app.config["MAIL_PORT"]
    ) as server:
        server.send_message(msg)