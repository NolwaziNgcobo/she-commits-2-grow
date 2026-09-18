# SheCommits2Grow
**She Builds Tomorrow — Track 2 (Cyber Safe & Secure) **


## The Problem

Online gender-based violence is rising, and most cases never get investigated —
not because the abuse isn't real, but because the evidence isn't usable. Screenshots
get cropped, timestamps go missing, accounts get deleted before anyone documents
them properly.

## The Solution

A guided evidence-capture and reporting tool. A woman documents an incident once,
the tool checks the evidence, and generates a clean, structured report — plus
tells her exactly where it needs to go (platform report, SAPS, or both).

This is applied digital forensics, not an awareness campaign.

## How to Run It

```bash
# from the project root
python -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate
pip install -r requirements.txt
python backend/app.py
```

Then open **http://localhost:5000** in your browser.

## Project Structure

```
she-commits-2-grow/
├── README.md
├── requirements.txt
├── backend/
│   ├── app.py               # Flask app, routes, form handling
│   ├── metadata_check.py    # checks uploaded screenshots
│   ├── report_generator.py  # builds the PDF report
│   └── routing_logic.py     # incident type -> guidance steps
├── frontend/
│   ├── templates/
│   │   ├── index.html       # the capture form
│   │   └── result.html      # guidance + download page
│   └── static/
│       └── style.css
├── data/
│   └── routing_rules.json   # editable guidance content per incident type
└── sample_output/           # generated PDFs land here (gitignored contents)
```

## Demo Plan

1. Open the form live.
2. Fill it in with a sample incident + screenshot.
3. Submit — show the generated PDF and the guidance steps.
 

## If Time Allows (Stretch Goals — Do Not Start Until Core Flow Works)

- Keyword-based auto-suggestion of incident type from the free-text description
- Multiple-incident case building for stalking patterns (log over time, not one-off)
- Basic auth so a user can come back and add to an existing case
# SheCommits2Grow
**She Builds Tomorrow — Track 2 (Cyber Safe & Secure) **


## The Problem

Online gender-based violence is rising, and most cases never get investigated —
not because the abuse isn't real, but because the evidence isn't usable. Screenshots
get cropped, timestamps go missing, accounts get deleted before anyone documents
them properly.

## The Solution

A guided evidence-capture and reporting tool. A woman documents an incident once,
the tool checks the evidence, and generates a clean, structured report — plus
tells her exactly where it needs to go (platform report, SAPS, or both).

This is applied digital forensics, not an awareness campaign.

## How to Run It

```bash
# from the project root
python -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate
pip install -r requirements.txt
python backend/app.py
```

Then open **http://localhost:5000** in your browser.

## Project Structure

```
she-commits-2-grow/
├── README.md
├── requirements.txt
├── backend/
│   ├── app.py               # Flask app, routes, form handling
│   ├── metadata_check.py    # checks uploaded screenshots
│   ├── report_generator.py  # builds the PDF report
│   └── routing_logic.py     # incident type -> guidance steps
├── frontend/
│   ├── templates/
│   │   ├── index.html       # the capture form
│   │   └── result.html      # guidance + download page
│   └── static/
│       └── style.css
├── data/
│   └── routing_rules.json   # editable guidance content per incident type
└── sample_output/           # generated PDFs land here (gitignored contents)
```

## Demo Plan

1. Open the form live.
2. Fill it in with a sample incident + screenshot.
3. Submit — show the generated PDF and the guidance steps.
 

## If Time Allows (Stretch Goals — Do Not Start Until Core Flow Works)

- Keyword-based auto-suggestion of incident type from the free-text description
- Multiple-incident case building for stalking patterns (log over time, not one-off)
- Basic auth so a user can come back and add to an existing case


            "Every other programme teaches women to protect themselves.
   We built the system that makes sure that when they try, it actually works."


            "Every other programme teaches women to protect themselves.
   We built the system that makes sure that when they try, it actually works."
