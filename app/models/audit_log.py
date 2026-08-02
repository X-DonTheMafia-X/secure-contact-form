from datetime import datetime, UTC
from app.extensions import db

class AuditLog(db.Model):

    __tablename__ = "audit_logs"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    timestamp = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC)
    )

    username = db.Column(
        db.String(80),
        nullable=True
    )

    event_type = db.Column(
        db.String(50),
        nullable=False
    )

    success = db.Column(
        db.Boolean,
        nullable=False
    )

    ip_address = db.Column(
        db.String(45),
        nullable=True
    )

    user_agent = db.Column(
        db.String(500),
        nullable=True
    )

    request_path = db.Column(
        db.String(255),
        nullable=True
    )

    details = db.Column(
        db.Text,
        nullable=True
    )