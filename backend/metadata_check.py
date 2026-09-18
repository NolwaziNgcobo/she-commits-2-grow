"""
metadata_check.py

Basic checks on an uploaded screenshot/image to flag obvious issues
before it gets included in a report. This is intentionally simple for
the hackathon demo - it's meant to visibly show *something* checking
the evidence, not to be forensic-grade software.

If there's time left after the core flow works, good next steps:
- Compare EXIF DateTimeOriginal (if present) against the date the user
  entered in the form, and flag a mismatch.
- Check for common signs of re-encoding/editing (e.g. missing EXIF on
  a file that claims to be a direct-from-camera photo).
"""

import os
import hashlib
from PIL import Image
from PIL.ExifTags import TAGS

def calculate_sha256(file_path: str) -> str:
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def check_image(file_path: str) -> dict:
    """
    Returns a dict:
      {
        "filename": str,
        "size_bytes": int,
        "dimensions": (width, height) or None,
        "has_exif": bool,
        "warnings": [str, ...]
      }
    """
    warnings = []
    result = {
        "filename": os.path.basename(file_path),
        "size_bytes": os.path.getsize(file_path),
        "dimensions": None,
        "has_exif": False,
        "warnings": warnings,
    }

    if result["size_bytes"] == 0:
        warnings.append("File is empty - upload may have failed.")
        return result

    try:
        with Image.open(file_path) as img:
            result["dimensions"] = img.size

            exif_data = img.getexif()
            if exif_data and len(exif_data) > 0:
                result["has_exif"] = True
            else:
                # Most phone screenshots strip EXIF by default - this is
                # normal, not suspicious, but worth surfacing to the user.
                warnings.append(
                    "No EXIF metadata found. This is common for screenshots, "
                    "but means the image alone can't confirm when it was taken - "
                    "the timestamp you entered in the form is what matters most."
                )
    except Exception as e:
        warnings.append(f"Could not read image file: {e}")

    return result
