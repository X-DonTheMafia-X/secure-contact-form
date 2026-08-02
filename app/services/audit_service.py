from flask import request
from flask_login import current_user

from app.extensions import db
from app.models.audit_log import AuditLog

def log_security_event(
        event_type,
        success,
        details=None
):
    username = "anonymous"

    if current_user.is_authenticated:
        username = current_user.username

    log = AuditLog(
        username=username,
        event_type=event_type,
        success=success,
        ip_address=request.remote_addr,
        user_agent=request.user_agent.string,
        request_path=request.path,
        details=details
    )

    try:
        db.session.add(log)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
        
