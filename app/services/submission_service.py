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
    attachment_filename = None
    attachment_sha256 = None
    attachment_mime_type = None

    if attachment:
        attachment_info = save_uploaded_file(attachment)

        existing = Submission.query.filter_by(
            attachment_sha256=attachment_info["sha256"]
    ).first()


    if existing:
        attachment_filename = existing.attachment
        attachment_sha256 = existing.attachment_sha256
        attachment_mime_type = existing.attachment_mime_type

    else:
        attachment_filename = attachment_info["filename"]
        attachment_sha256 = attachment_info["sha256"]
        attachment_mime_type = attachment_info["mime_type"]

    submission = Submission(
        name=name,
        email=email,
        message=message,
        attachment=attachment_filename,
        attachment_sha256=attachment_sha256,
        attachment_mime_type=attachment_mime_type
        
    )
    try:
        db.session.add(submission)
        db.session.commit()
        logger.info(
            "Submission created for email= %s",
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