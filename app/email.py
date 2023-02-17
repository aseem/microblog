from flask_mail import Message
from app import mail, app
from flask import render_template

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(subject, sender, recipients, html_body):
    message = Mail(
    from_email=sender,
    to_emails=recipients,
    subject=subject,
    html_content=html_body)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))