from pathlib import Path
from uuid import uuid4

from flask import current_app
from werkzeug.utils import secure_filename


def save_uploaded_file(file_storage):
    """
    Validate and save an uploaded file.
    
    Returns the generated filename, or None if no file was uploaded.
    """

    if not file_storage or not file_storage.filename:
        return None

    original_name = secure_filename(file_storage.filename)

    if not original_name:
        return None

    extension = Path(original_name).suffix.lower()

    allowed_extensions = current_app.config.get(
        "ALLOWED_UPLOAD_EXTENSIONS",
        set()
    )

    if extension not in allowed_extensions:
        raise ValueError("File type is not allowed.")

    filename = f"{uuid4().hex}{extension}"

    upload_directory = (
        Path(current_app.config["UPLOAD_FOLDER"])
        / "documents"
    )

    upload_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    upload_path = upload_directory / filename

    file_storage.save(upload_path)

    return filename