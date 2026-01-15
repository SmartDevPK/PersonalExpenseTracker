import os
import uuid
from flask import url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "app/static/uploads/receipts"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "pdf"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


def save_receipt_file(file):
    if not file or file.filename == "":
        return None

    if not allowed_file(file.filename):
        raise ValueError("Invalid receipt file type")

    ext = file.filename.rsplit(".", 1)[1].lower()
    filename = f"{uuid.uuid4().hex}.{ext}"

    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    return url_for(
        "static",
        filename=f"uploads/receipts/{filename}",
        _external=True
    )
