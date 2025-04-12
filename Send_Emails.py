import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv("mail.env")

def send_email(message):
    host = "smtp.gmail.com"
    port = 587  # Try 587 if 465 doesn't work

    username = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(host, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(username, password)
            server.sendmail(username, receiver, message)
    except Exception as e:
        print(f"Error sending email: {e}")