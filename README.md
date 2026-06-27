# AI/ML Conference & Journal Tracker

[![Data validation](https://github.com/tirthajit/ai-ml-conference-journal-tracker/actions/workflows/validate-data.yml/badge.svg)](https://github.com/tirthajit/ai-ml-conference-journal-tracker/actions/workflows/validate-data.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC--BY--4.0-green.svg)](LICENSE)
[![Last verified](https://img.shields.io/badge/last_verified-2026-06-27-informational)](data/sources.csv)

A curated, ranked, source-backed tracker for reputable AI/ML conferences and journals. It is intended for researchers who need to identify target venues, monitor submission windows, and verify official sources before submitting manuscripts.

> Deadlines move often. Treat this tracker as a planning aid and always verify the official CFP or journal page before submission.

## Quick links

| Resource | Link |
|---|---|
| Public webpage | [https://tirthajit.github.io/ai-ml-conference-journal-tracker/](https://tirthajit.github.io/ai-ml-conference-journal-tracker/) |
| Current-cycle deadlines | [`data/submission_calendar_current_cycle.csv`](data/submission_calendar_current_cycle.csv) |
| Conference master list | [`data/conferences_master.csv`](data/conferences_master.csv) |
| Journal list | [`data/journals_reputable.csv`](data/journals_reputable.csv) |
| Source registry | [`data/sources.csv`](data/sources.csv) |
| Excel export | [`exports/ai_ml_conference_journal_tracker_v2.xlsx`](exports/ai_ml_conference_journal_tracker_v2.xlsx) |
| Methodology | [https://tirthajit.github.io/ai-ml-conference-journal-tracker/methodology.html](https://tirthajit.github.io/ai-ml-conference-journal-tracker/methodology.html) |

## Snapshot

| Item | Count |
|---|---:|
| Conferences tracked | 117 |
| Current-cycle deadline rows | 117 |
| Journal targets tracked | 50 |
| Source entries | 39 |
| Last verified snapshot | 2026-06-27 |

## What is included

| File/folder | Purpose |
|---|---|
| `data/` | Canonical CSV files. Update these first. |
| `docs/` | Static GitHub Pages website with searchable tables. |
| `exports/` | Convenience Excel snapshot for offline use. |
| `scripts/validate_data.py` | Checks required columns, dates, tiers, URLs, and confidence labels. |
| `scripts/build_static_site.py` | Regenerates static site metadata and sanity-checks web assets. |
| `schemas/` | Machine-readable descriptions of expected data fields. |
| `.github/ISSUE_TEMPLATE/` | Structured update request form. |
| `.github/workflows/` | GitHub Actions validation workflow. |

## Tier convention

This project uses a practical target tier in addition to any available external ranking information.

| Tier | Meaning |
|---|---|
| `S` | Global flagship or field-defining venue. |
| `A` | Major reputable archival venue. |
| `B` | Solid specialist, regional, or focused venue. |
| `C` | Niche venue; verify fit, indexing, and reputation carefully. |

The `core_rank_prefill` field is included only as a convenience field. External rankings should be verified from their original sources.

## Deadline confidence labels

| Label family | Meaning |
|---|---|
| `Official announced` | Verified from an official venue page or CFP. |
| `Tracker / ...` | Sourced from a reputable deadline tracker or official pattern, but not treated as the final authority. |
| `Tentative ...` | Estimated from historical cycles or common annual windows. |
| `Rolling ...` | Multiple or rolling deadlines; check the official page before planning. |

## Recommended maintenance rule

When updating a row, update these fields together:

```text
full_paper_deadline
abstract_deadline, if applicable
timezone
deadline_status
deadline_confidence
official_or_tracker_url
last_verified
notes
```

Then add a short note to [`CHANGELOG.md`](CHANGELOG.md).

## Contributing corrections

Use the issue form: [https://github.com/tirthajit/ai-ml-conference-journal-tracker/issues/new/choose](https://github.com/tirthajit/ai-ml-conference-journal-tracker/issues/new/choose)

Please include an official CFP, conference website, publisher page, ranking source, or other verifiable source. Unsourced changes may not be accepted.

## Citation

Use the repository citation metadata in [`CITATION.cff`](CITATION.cff). After the first public release, consider archiving the release with Zenodo and adding a DOI.

## License

This dataset and documentation are released under the [Creative Commons Attribution 4.0 International License](LICENSE), unless otherwise stated. Source websites retain their respective copyrights.
