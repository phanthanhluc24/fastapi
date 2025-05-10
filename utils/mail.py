from email.message import EmailMessage
import random
import smtplib
from core.config import settings

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(to_email: str, otp_code: str):
    email_sender = settings.email_sender
    email_password = settings.email_password
    smtp_host = settings.email_smtp_host
    smtp_port = int(settings.email_smtp_port)

    msg = EmailMessage()
    msg['Subject'] = "Mã OTP xác thực đăng ký"
    msg['From'] = email_sender
    msg['To'] = to_email
    msg.set_content(f"Mã OTP của bạn là: {otp_code}")

    with smtplib.SMTP_SSL(smtp_host, smtp_port) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(msg)
