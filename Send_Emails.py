import smtplib
import ssl



def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    # Create a password for your email.(gmail or yahoo)
    username = ""
    password = ""
    
    # Add a reciever email.
    receiver = ""
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server :
        server.login(username, password)
        server.sendmail(username, receiver, message)
