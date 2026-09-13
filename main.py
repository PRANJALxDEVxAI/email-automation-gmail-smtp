import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")


def send_email(recipient, subject, body , attachments=None, cc=None, bcc=None):
    message = EmailMessage()

    message["From"] = EMAIL_ADDRESS
    message["To"] = recipient
    if cc:
        message["Cc"] = cc
    if bcc:
        message["Bcc"] = bcc
    message["Subject"] = subject


    message.set_content(body)
    if attachments:
        for attachment in attachments:
            with open(attachment, "rb") as f:
                file_data = f.read()
                file_name = os.path.basename(attachment)
                message.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    print("Connecting to Gmail...")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=60) as smtp:
        print("Connected to Gmail.")

        print("Logging in...")
        smtp.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)

        print("Login successful.")

        print("Sending email...")
        smtp.send_message(message)

        print("Email sent successfully!")


recipient = input("Enter recipient email: ")
subject = input("Enter subject: ")
body = input("Enter message: ")
if input("Do you want to add attachments? (y/n): ").lower() == "y":
    attachments = []
    while True:
        attachment_path = input("Enter attachment file path (or 'done' to finish): ")
        if attachment_path.lower() == "done":
            break
        if os.path.isfile(attachment_path):
            attachments.append(attachment_path)
        else:
            print("File does not exist. Please try again.")
else:
    attachments = None

cc = input("Enter CC email addresses (comma-separated, optional): ")
if cc:
    cc = cc.split(",")
else:
    cc = None

bcc = input("Enter BCC email addresses (comma-separated, optional): ")
if bcc:
    bcc = bcc.split(",")
else:
    bcc = None

send_email(recipient, subject, body , attachments=attachments, cc=cc, bcc=bcc)

print("Program finished.")