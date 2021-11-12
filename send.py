import ssl, smtplib
from email.message import EmailMessage
from time import sleep
from getpass import getpass


def send(choices, username, sender, smtp_server):
    msg_string = """\n
    Hi {0}!\n
    You have been chosen as {1}'s Secret Santa.
    """

    with smtplib.SMTP(smtp_server) as smtp:
        cntxt = ssl.create_default_context()
        smtp.starttls(context=cntxt)
        try:
            smtp.login(user=username, password=getpass("password:"))
        except smtplib.SMTPAuthenticationError:
            print("Username and password not accepted or access blocked (e.g. Google blocking third party apps.). Aborting.")
            return
        for (name, mail, nameto) in choices:
            msg = EmailMessage()
            msg['From'] = sender
            msg['Subject'] = f"Secret Santa pick for {nameto}"
            msg['To'] = mail
            msg.set_content(msg_string.format(nameto, name))
            smtp.send_message(msg)
            sleep(0.5)

def pre_send():
    address = input("Write the address from which the emails will be sent: ")
    username, server = address.split('@')
    smtp_server = "smtp." + server
    return username, address, smtp_server


def work(choices):
    username, address, smtp_server = pre_send()
    send(choices, username, address, smtp_server)
