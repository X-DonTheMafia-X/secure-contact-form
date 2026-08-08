from flask import (
    Blueprint,
    render_template
)
from app.models.submission import Submission

from flask_login import login_required

from app.extensions import limiter

from app.security.authorization import(
    admin_required
)
from zoneinfo import ZoneInfo
from datetime import timezone

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

    submissions = Submission.query.all()
    local_timezone = ZoneInfo("America/Toronto")

    for submission in submissions:
        utc_created_at = submission.created_at.replace(tzinfo=timezone.utc)

        submission.local_created_at = utc_created_at.astimezone(local_timezone)

    return render_template(
        "pages/admin_dashboard.html",
        submissions=submissions,
    )
