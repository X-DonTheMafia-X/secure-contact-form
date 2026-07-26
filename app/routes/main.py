from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for
)

# Import forms
from app.forms.contact_form import ContactForm

# Import models
from app.models.submission import Submission

# Import extensions
from app.extensions import db

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():

    form = ContactForm()

    if form.validate_on_submit():
        submission = Submission(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )
        try:
            db.session.add(submission)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

        return redirect(url_for("main.home"))

    return render_template(
        "pages/home.html",
        form=form
        )