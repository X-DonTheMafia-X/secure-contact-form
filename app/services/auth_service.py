from flask_login import login_user
from app.models.user import User
from app.services.audit_service import(
    log_security_event
)

def authenticate_user(username, password, remember=False):
    user = User.query.filter_by(username=username).first()

    if user is None:

        log_security_event(
            event_type="LOGIN_FAILED",
            success=False,
            details=f"Unknown username: {username}"
        )

        return False

    if not user.check_password(password):

        log_security_event(
            event_type="LOGIN_FAILED",
            success=False,
            details="Incorrent password"
        )

        return False

    login_user(
        user,
        remember=remember
        )

    log_security_event(
        event_type="LOGIN_SUCCESS",
        success=True
    )

    

    return True