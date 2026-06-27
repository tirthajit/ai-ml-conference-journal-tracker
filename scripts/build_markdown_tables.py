#!/usr/bin/env python3
"""Regenerate compact markdown previews from CSV data."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read_csv(rel):
    with (ROOT / rel).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def md_table(rows, cols, max_rows=80):
    rows = rows[:max_rows]
    out = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"]*len(cols)) + " |"]
    for r in rows:
        vals = []
        for c in cols:
            v = str(r.get(c,"")).replace("|","/")
            vals.append(v[:77] + "..." if len(v) > 80 else v)
        out.append("| " + " | ".join(vals) + " |")
    return "\n".join(out)

def main():
    conferences = read_csv("data/conferences_master.csv")
    calendar = read_csv("data/submission_calendar_current_cycle.csv")
    journals = read_csv("data/journals_reputable.csv")

    (ROOT/"docs"/"conferences.md").write_text(
        "---\ntitle: Conference Master List\n---\n\n# Conference Master List\n\n"
        "Full data: [`data/conferences_master.csv`](../data/conferences_master.csv).\n\n"
        + md_table(conferences, ["curated_tier","acronym","name","area","full_paper_deadline","usual_tentative_window","deadline_confidence"], 80)
        + "\n", encoding="utf-8")

    (ROOT/"docs"/"calendar.md").write_text(
        "---\ntitle: Current-Cycle Deadline Calendar\n---\n\n# Current-Cycle Deadline Calendar\n\n"
        "Full data: [`data/submission_calendar_current_cycle.csv`](../data/submission_calendar_current_cycle.csv).\n\n"
        + md_table(calendar, ["curated_tier","acronym","current_or_next_edition","full_paper_deadline","deadline_status","timezone","deadline_confidence"], 100)
        + "\n", encoding="utf-8")

    (ROOT/"docs"/"journals.md").write_text(
        "---\ntitle: Reputable Journals\n---\n\n# Reputable Journals\n\n"
        "Full data: [`data/journals_reputable.csv`](../data/journals_reputable.csv).\n\n"
        + md_table(journals, ["target_priority","journal","area","publisher","jcr_quartile_or_rank_note","sjr_quartile_note"], 100)
        + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
