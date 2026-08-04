from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    url_for
)
from app.extensions import limiter
from app.forms.login_form import LoginForm
from app.services.auth_service import authenticate_user

from flask_login import(
    login_required,
    logout_user
)

from app.services.audit_service import(
    log_security_event
)

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
@limiter.limit(
    "5 per minute"
)
def login():

    form = LoginForm()

    if form.validate_on_submit():

        success = authenticate_user(
            form.username.data,
            form.password.data,
            form.remember.data
        )

        if success:

            flash(
                f"Welcome back, {form.username.data}",
                "success"
            )

            return redirect(
                url_for("main.home")
            )
        flash(
            "Invalid username or password.",
            "danger"

        )
    return render_template(
        "pages/login.html",
        form=form
    )
@auth.route("/logout")
@login_required
def logout():

    log_security_event(
        event_type="LOGOUT",
        success=True
    )

    logout_user()

    flash(
        "You have been logged out.",
        "success"
    )

    return redirect(
        url_for("auth.login")
    )