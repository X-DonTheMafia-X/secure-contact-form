from app.extensions import db
from app.models.submission import Submission

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
    except Exception:
        db.session.rollback()
        raise

    return submission