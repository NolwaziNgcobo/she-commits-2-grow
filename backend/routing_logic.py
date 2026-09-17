"""
routing_logic.py

Takes an incident type and returns the guidance steps + urgency level
from data/routing_rules.json.

This is deliberately simple for the hackathon build: a lookup, not a
classifier. If there's time left, this is the easiest place to add
more intelligence (e.g. keyword-based auto-suggestion of incident type
from the free-text description).
"""

import json
import os

RULES_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "routing_rules.json")


def load_rules():
    with open(RULES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_guidance(incident_type: str) -> dict:
    """
    Returns a dict with 'label', 'urgency', and 'steps' for the given
    incident_type key. Falls back to a generic response if the type
    isn't recognised, so the app never crashes on unexpected input.
    """
    rules = load_rules()
    return rules.get(incident_type, {
        "label": "General online abuse",
        "urgency": "medium",
        "steps": [
            "Screenshot everything with dates and account handles visible.",
            "Report to the platform where it happened.",
            "If you feel unsafe, contact SAPS or a trusted support organisation."
        ]
    })


def list_incident_types() -> dict:
    """Returns {key: label} for populating the form dropdown."""
    rules = load_rules()
    return {key: value["label"] for key, value in rules.items()}
