from flask_mail import Message
from flask import url_for
from app.extensions import mail
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables early


def send_password_reset_email(email, token):
    reset_url = url_for('user_api.reset_password', token=token, _external=True)

    subject = "Password Reset Request"
    sender = os.getenv("MAIL_USERNAME") or "no-reply@example.com"
    recipients = [email]

    text_body = f"""
Hi,

You requested to reset your password. Please click the link below to reset it:

{reset_url}

If you did not request this, please ignore this email.

Thanks,
Your App Team
"""

    html_body = f"""
<html>
  <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
    <h2 style="color: #2c3e50;">Password Reset Request</h2>
    <p>Hi,</p>
    <p>You requested to reset your password. Please click the button below to reset it:</p>
    <p style="text-align: center;">
      <a href="{reset_url}" 
         style="background-color: #3498db; color: white; padding: 12px 20px; text-decoration: none; border-radius: 5px; display: inline-block;">
         Reset Password
      </a>
    </p>
    <p>If the button above doesn’t work, copy and paste this link into your browser:</p>
    <p><a href="{reset_url}" style="color: #3498db;">{reset_url}</a></p>
    <hr style="border:none; border-top:1px solid #eee;">
    <p>If you did not request this, please ignore this email.</p>
    <p>Thanks,<br>Your App Team</p>
  </body>
</html>
"""

    msg = Message(
        subject=subject,
        sender=sender,
        recipients=recipients,
        body=text_body,
        html=html_body
    )
    mail.send(msg)

