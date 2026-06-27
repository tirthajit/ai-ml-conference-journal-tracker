#!/usr/bin/env python3
"""Validate CSV files for the AI/ML Conference & Journal Tracker."""

from __future__ import annotations

import csv
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

CSV_REQUIREMENTS = {
    "data/conferences_master.csv": [
        "rank_order", "curated_tier", "acronym", "name", "area",
        "full_paper_deadline", "deadline_status", "deadline_confidence",
        "official_or_tracker_url", "last_verified",
    ],
    "data/submission_calendar_current_cycle.csv": [
        "rank_order", "curated_tier", "acronym", "name", "area",
        "full_paper_deadline", "deadline_status", "deadline_confidence",
        "official_or_tracker_url", "last_verified",
    ],
    "data/journals_reputable.csv": [
        "target_priority", "journal", "area", "publisher", "metric_source_url",
        "journal_url", "last_verified",
    ],
    "data/sources.csv": ["source_name", "url", "role"],
}

DATE_COLUMNS = {
    "abstract_deadline", "full_paper_deadline", "last_verified",
    "conference_start", "conference_end", "notification_date", "camera_ready_deadline",
}
URL_COLUMNS = {"official_or_tracker_url", "metric_source_url", "journal_url", "url"}
VALID_TIERS = {"S", "A", "B", "C"}
VALID_STATUSES = {"Passed", "Upcoming", "Not announced", "Rolling"}
VALID_CONFIDENCE_PREFIXES = (
    "Official announced",
    "Tracker /",
    "Tentative",
    "Rolling /",
)
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def check_date(value: str, label: str, errors: list[str]) -> None:
    if not value:
        return
    if not ISO_DATE.fullmatch(value):
        errors.append(f"{label}: expected YYYY-MM-DD, found {value!r}")
        return
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        errors.append(f"{label}: invalid calendar date {value!r}")


def validate_file(relpath: str, required_cols: list[str], errors: list[str]) -> None:
    path = ROOT / relpath
    if not path.exists():
        errors.append(f"Missing file: {relpath}")
        return

    headers, rows = read_csv(path)
    missing = [col for col in required_cols if col not in headers]
    if missing:
        errors.append(f"{relpath}: missing columns: {', '.join(missing)}")
        return

    seen_ids: set[str] = set()
    for idx, row in enumerate(rows, start=2):
        prefix = f"{relpath}:{idx}"

        for col in required_cols:
            if not row.get(col, "").strip():
                errors.append(f"{prefix}: required column {col!r} is blank")

        for col in DATE_COLUMNS.intersection(headers):
            check_date(row.get(col, "").strip(), f"{prefix}:{col}", errors)

        for col in URL_COLUMNS.intersection(headers):
            value = row.get(col, "").strip()
            if value and not valid_url(value):
                errors.append(f"{prefix}:{col}: invalid URL {value!r}")

        tier = row.get("curated_tier") or row.get("target_priority")
        if tier and tier not in VALID_TIERS:
            errors.append(f"{prefix}: invalid tier/priority {tier!r}")

        status = row.get("deadline_status")
        if status and status not in VALID_STATUSES:
            errors.append(f"{prefix}: unexpected deadline_status {status!r}")

        confidence = row.get("deadline_confidence", "")
        if confidence and not confidence.startswith(VALID_CONFIDENCE_PREFIXES):
            errors.append(f"{prefix}: unexpected deadline_confidence {confidence!r}")

        if confidence == "Official announced" and not row.get("official_or_tracker_url", "").strip():
            errors.append(f"{prefix}: official deadline requires official_or_tracker_url")

        key_fields = [row.get("acronym", ""), row.get("current_or_next_edition", ""), row.get("journal", "")]
        key = "|".join(k for k in key_fields if k)
        if key:
            if key in seen_ids:
                errors.append(f"{prefix}: duplicate row key {key!r}")
            seen_ids.add(key)


def main() -> int:
    errors: list[str] = []
    for relpath, required_cols in CSV_REQUIREMENTS.items():
        validate_file(relpath, required_cols, errors)

    if errors:
        print("Validation failed:\n", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("CSV validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
