from flask import (
    Blueprint,
    render_template
)

from flask_login import login_required

from app.extensions import limiter

from app.security.authorization import(
    admin_required
)

admin = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)

@admin.route("/")
@login_required
@limiter.limit(
    "30 per minute"
)
@admin_required
def dashboard():

    return render_template(
        "pages/admin_dashboard.html"
    )
