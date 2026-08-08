from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)


# Import forms
from app.forms.contact_form import ContactForm

# Import Services
from app.services.submission_service import create_submission

# Import models
from app.models.submission import Submission

# Import extensions
from app.extensions import db
from app.extensions import limiter

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
@limiter.limit(
    "10 per minute"
)

def home():

    return render_template(
        "pages/home.html",
        )

@main.route("/contact", methods=["GET", "POST"])
@limiter.limit(
    "10 per minute"
)
def contact():

    form = ContactForm()

    if form.validate_on_submit():

        create_submission(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data,
            attachment=form.attachment.data
        )

        flash(
            "Your message has been sent successfully!",
            "success"
        )

        return redirect(url_for("main.contact"))

    return render_template(
        "pages/contact.html",
        form=form
        )
@main.route("/menu", methods=["GET", "POST"])
@limiter.limit(
    "10 per minute"
)

def menu():

    return render_template(
        "pages/menu.html",
        )
