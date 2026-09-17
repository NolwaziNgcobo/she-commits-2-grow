"""
app.py

Main Flask app. Run with:  python backend/app.py
Then open: http://localhost:5000

Flow:
  1. GET  /            -> shows the capture form
  2. POST /submit      -> handles the form, runs the checks,
                           generates the PDF, shows a result page
  3. GET  /download/<f> -> lets the user download the generated PDF
"""

import os
import sys

# allow "from backend.x import y" style imports to work whether this
# is run as `python backend/app.py` or `python -m backend.app`
sys.path.append(os.path.dirname(__file__))

from flask import Flask, render_template, request, send_from_directory, redirect, url_for

from metadata_check import check_image
from routing_logic import get_guidance, list_incident_types
from report_generator import generate_report, OUTPUT_DIR

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "..", "frontend", "templates")
STATIC_DIR = os.path.join(os.path.dirname(__file__), "..", "frontend", "static")
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "..", "sample_output", "uploads")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB upload limit

os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html", incident_types=list_incident_types())


@app.route("/submit", methods=["POST"])
def submit():
    reporter_name = request.form.get("reporter_name", "").strip()
    platform = request.form.get("platform", "").strip()
    incident_date = request.form.get("incident_date", "").strip()
    incident_type = request.form.get("incident_type", "").strip()
    description = request.form.get("description", "").strip()
    screenshot = request.files.get("screenshot")

    guidance = get_guidance(incident_type)

    # Save uploaded screenshot (if provided) and run the metadata check
    image_check = {"filename": "-", "dimensions": None, "has_exif": False, "warnings": []}
    if screenshot and screenshot.filename:
        safe_name = screenshot.filename.replace(" ", "_")
        upload_path = os.path.join(UPLOAD_DIR, safe_name)
        screenshot.save(upload_path)
        image_check = check_image(upload_path)
    else:
        image_check["warnings"].append("No screenshot was uploaded.")

    case = {
        "reporter_name": reporter_name,
        "platform": platform,
        "incident_date": incident_date,
        "incident_type_label": guidance.get("label", incident_type),
        "description": description,
    }

    pdf_path = generate_report(case, image_check, guidance)
    pdf_filename = os.path.basename(pdf_path)

    return render_template(
        "result.html",
        case=case,
        guidance=guidance,
        image_check=image_check,
        pdf_filename=pdf_filename,
    )


@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
