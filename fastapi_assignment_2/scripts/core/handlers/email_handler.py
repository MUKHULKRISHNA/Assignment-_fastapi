from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from scripts.core.handlers.fast_api_handler import aggregation_func

load_dotenv()


def send_email(email: str, subject: str):
    # Set up the email details
    sender_email = os.environ.get('sender_email')
    sender_password = os.environ.get('sender_password')

    receiver_email = email

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add the body to the email

    dat = aggregation_func()  # Assuming you have a function that returns the data

    total_fees = dat.get("total fees")  # Extract the value of the "total fees" key

    body = str(total_fees)

    message.attach(MIMEText(f"Total amount :{body}", "plain"))

    try:
        return extract_code(sender_email, sender_password, message)
    except Exception as e:
        return {"message": str(e)}


def extract_code(sender_email, sender_password, message):
    # Create a secure connection to the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Login to the sender's email account
    server.login(sender_email, sender_password)

    # Send the email
    server.send_message(message)

    # Close the connection
    server.quit()

    return {"message": "Email sent successfully"}
