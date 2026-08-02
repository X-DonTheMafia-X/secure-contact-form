from flask_login import login_user
from app.models.user import User
from app.services.audit_service import(
    log_security_event
)
from datetime import datetime, timedelta, UTC
from app.extensions import db
from app.security.constants import(
    MAX_LOGIN_ATTEMPTS,
    LOCKOUT_MINUTES
)

def authenticate_user(username, password, remember=False):
    user = User.query.filter_by(username=username).first()

    now = datetime.now(UTC).replace(tzinfo=None)
    if (
        user is not None
        and user.locked_until
        and user.locked_until > now
    ):
        return False

    if user is None:

        log_security_event(
            event_type="LOGIN_FAILED",
            success=False,
            details=f"Unknown username: {username}"
        )

        return False

    if not user.check_password(password):


        user.failed_login_attempts += 1
        if user.failed_login_attempts >= MAX_LOGIN_ATTEMPTS:

            user.locked_until = (
                now + timedelta(minutes=LOCKOUT_MINUTES)
            )

            log_security_event(
                event_type="ACCOUNT_LOCKED",
                success=True,
                details=(
                    f"Locked until"
                    f"{user.locked_until.isoformat()}"
                )
            )

        db.session.commit()

        log_security_event(
            event_type="LOGIN_FAILED",
            success=False,
            details="Incorrect password"
        )

        return False

    user.failed_login_attempts = 0
    user.locked_until = None
    db.session.commit()

    login_user(
        user,
        remember=remember
        )

    log_security_event(
        event_type="LOGIN_SUCCESS",
        success=True
    )

    

    return True