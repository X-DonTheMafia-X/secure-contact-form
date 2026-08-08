from flask import current_app
from flask_mail import Message
from app.extensions import mail

def send_confirmation_email(submission):
    """
    Send a Confirmation email to the customer.
    """

    message = Message(
        subject="We've received your message",
        recipients=[submission.email]
    )

    message.body = (
        f"Hello {submission.name},\n\n"
        "Thank you for contacting us.\n\n"
        "We've successfully received your message"
        " and will respond as soon as possible.\n\n"
        "Regards,\n"
        "YOUR BUSINESS NAME"
    )

    mail.send(message)

def send_admin_notification(submission):
    """
    Notify the admin about new submission.
    """

    message = Message(
        subject="New Submission for YOUR BUSINESS NAME",
        recipients=[
            current_app.config["MAIL_DEFAULT_SENDER"]
            ]
        
    )

    message.body = (
        f"Name: {submission.name}\n"
        f"Email: {submission.email}\n\n"
        f"Message:\n\n{submission.message}"
    )

    mail.send(message)