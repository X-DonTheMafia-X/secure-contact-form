from app.extensions import db
from app.models.submission import Submission
from app.logging_config import logger
from app.services.email_service import(
    send_admin_notification,
    send_confirmation_email
)
from app.services.upload_service import(
    save_uploaded_file
)

def create_submission(name, email, message, attachment=None):
    """
    Create and save a contact from submission.
    """
    attachment_name = save_uploaded_file(attachment)
    submission = Submission(
        name=name,
        email=email,
        message=message,
        attachment=attachment_name
        
    )
    try:
        db.session.add(submission)
        db.session.commit()
        logger.info(
            "Submission created for email=%s",
            submission.email
        )

    except Exception:
        db.session.rollback()
        raise

    # Send email delivery after database success.
    # after transaction has committed.
    send_confirmation_email(submission)
    send_admin_notification(submission)

    return submission