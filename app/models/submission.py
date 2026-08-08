from app.extensions import db
from datetime import datetime, timezone
# Create a new database model
class Submission(db.Model):
    # Tells SQLAlchemy what the database table should be called
    __tablename__ = "submissions"

    # Date and Tme
    created_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    # ID
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Name
    name = db.Column(
        db.String(100),
        nullable=False
    )

    # Email
    email = db.Column(
        db.String(255),
        nullable=False
    )

    # Message
    message = db.Column(
        db.Text(1000),
        nullable=False
    )
    # Attachments
    attachment = db.Column(
        db.String(255),
        nullable=True
    )

    attachment_sha256 = db.Column(
        db.String(64),
        nullable=True,
        unique=False
    )

    attachment_mime_type = db.Column(
        db.String(100),
        nullable = True
    )


    