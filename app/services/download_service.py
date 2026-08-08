from pathlib import Path

from flask import (
    abort,
    current_app,
    send_from_directory
)


def download_document(filename):

    upload_directory = (
        current_app.config["UPLOAD_FOLDER"]
        / "documents"
    )

    file_path = upload_directory / filename

    if not file_path.exists():
        abort(404)

    return send_from_directory(
        upload_directory,
        filename,
        as_attachment=True
    )