#!/usr/bin/env python3
import csv
import re
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "data/conferences_master.csv": ["curated_tier","acronym","name","area","full_paper_deadline","deadline_confidence","official_or_tracker_url"],
    "data/submission_calendar_current_cycle.csv": ["curated_tier","acronym","name","area","full_paper_deadline","deadline_confidence","official_or_tracker_url"],
    "data/journals_reputable.csv": ["target_priority","journal","area","metric_source_url","journal_url"],
    "data/sources.csv": ["source_name","url","role"],
}

DATE_COLS = {"full_paper_deadline", "abstract_deadline", "last_verified"}

def check_date(value, path, rownum, col, errors):
    if not value:
        return
    if col == "last_verified" or re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            errors.append(f"{path}:{rownum}: invalid date in {col}: {value}")
    else:
        errors.append(f"{path}:{rownum}: exact dates must use YYYY-MM-DD in {col}: {value}")

def main():
    errors = []
    for rel, cols in REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing file: {rel}")
            continue
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            missing = [c for c in cols if c not in reader.fieldnames]
            if missing:
                errors.append(f"{rel}: missing columns {missing}")
                continue
            for i, row in enumerate(reader, start=2):
                for col in cols:
                    if col in ("full_paper_deadline", "abstract_deadline"):
                        continue
                    if not row.get(col, "").strip():
                        errors.append(f"{rel}:{i}: blank required field {col}")
                for col in DATE_COLS & set(row.keys()):
                    check_date(row.get(col, "").strip(), rel, i, col, errors)
                for col in ("official_or_tracker_url","metric_source_url","journal_url","url"):
                    if col in row and row[col] and not row[col].startswith(("http://","https://")):
                        errors.append(f"{rel}:{i}: URL field {col} is not http(s): {row[col]}")
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print("CSV validation passed.")

if __name__ == "__main__":
    main()
