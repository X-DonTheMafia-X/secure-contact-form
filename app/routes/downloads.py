from flask import (
    Blueprint,
    abort
)

from flask_login import (
    current_user,
    login_required
)

from app.models.submission import Submission
from app.services.download_service import download_document
from app.services.audit_service import log_security_event

downloads = Blueprint(
    "downloads",
    __name__,
    url_prefix="/downloads"
)

@downloads.route("/<int:submission_id>")
@login_required
def download(submission_id):

    submission = Submission.query.get_or_404(submission_id)

    if current_user.role != "admin":

        log_security_event(
            event_type="FILE_DOWNLOAD_DENIED",
            success=False,
            details=f"Submission #{submission.id}"
        )

        abort(403)

    if not submission.attachment:
        abort(404)

    log_security_event(
        event_type="FILE_DOWNLOAD",
        success=True,
        details=f"Submission #{submission.id}"
    )

    return download_document(
        submission.attachment
    )