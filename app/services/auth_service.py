from flask_login import login_user
from app.models.user import User

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()

    if user is None:
        return False

    if not user.check_password(password):
        return False

    login_user(user)

    return True