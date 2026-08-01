from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    url_for
)

from app.forms.login_form import LoginForm
from app.services.auth_service import authenticate_user

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        success = authenticate_user(
            form.username.data,
            form.password.data
        )

        if success:

            flash(
                f"Welcome back, {form.username.data}"
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