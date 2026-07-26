from flask import (
    Blueprint,
    render_template
)

from app.forms.contact_form import ContactForm

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():

    form = ContactForm()

    if form.validate_on_submit():
        print("Form validated successfully!")

    return render_template(
        "pages/home.html",
        form=form
        )