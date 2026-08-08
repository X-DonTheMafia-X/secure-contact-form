import magic
import hashlib

ALLOWED_MIME_TYPES = {
    "application/pdf",
    "image/jpeg",
    "image/png",
    "text/plain",
}

def validate_mime_type(file_storage):

    file_bytes = file_storage.stream.read(2048)

    file_storage.stream.seek(0)

    mime_type = magic.from_buffer(
        file_bytes,
        mime=True
    )

    return mime_type in ALLOWED_MIME_TYPES

def calculate_sha256(file_storage):
    hasher = hashlib.sha256()

    while True:
        chunk = file_storage.stream.read(4096)

        if not chunk:
            break

        hasher.update(chunk)

    file_storage.stream.seek(0)

    return hasher.hexdigest()