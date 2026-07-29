from app.extensions import db
from app.models.submission import Submission
from app.services.email_service import(
    send_admin_notification,
    send_confirmation_email
)

def create_submission(name, email, message):
    """
    Create and save a contact from submission.
    """

    submission = Submission(
        name=name,
        email=email,
        message=message
    )
    try:
        db.session.add(submission)
        db.session.commit()
        send_confirmation_email(submission)
        send_admin_notification(submission)
    except Exception:
        db.session.rollback()
        raise

    return submission