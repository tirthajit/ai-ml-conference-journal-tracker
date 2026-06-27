# Setup and Maintenance Guide

This guide is written for the live repository:

```text
https://github.com/tirthajit/ai-ml-conference-journal-tracker
```

and project webpage:

```text
https://tirthajit.github.io/ai-ml-conference-journal-tracker/
```

## One-time setup checklist

1. Repository is public.
2. GitHub Pages is enabled from `main` branch and `/docs` folder.
3. The repository About panel contains:
   - Description: `Ranked AI/ML conference and journal tracker with submission deadlines, tentative annual windows, source links, and update status.`
   - Website: `https://tirthajit.github.io/ai-ml-conference-journal-tracker/`
   - Topics: `artificial-intelligence`, `machine-learning`, `conferences`, `journals`, `research`, `deadlines`, `academic-publishing`.
4. Issues are enabled.
5. GitHub Actions shows `Validate data`.
6. The root-level folder `workflows/` is absent. Only `.github/workflows/` should exist.

## Web-only update workflow

Use this when making small corrections from the GitHub website.

### Update a conference deadline

1. Open `data/submission_calendar_current_cycle.csv`.
2. Click the pencil icon.
3. Update the row.
4. Update these fields together:

```text
abstract_deadline
full_paper_deadline
timezone
deadline_status
deadline_confidence
official_or_tracker_url
last_verified
notes
```

5. Commit with a specific message, for example:

```text
Update AAAI-27 official deadline
```

6. Open `CHANGELOG.md`.
7. Add a dated entry.
8. Commit.

### Update a general tentative window

Edit `data/conferences_master.csv`, then update:

```text
usual_tentative_window
deadline_confidence
official_or_tracker_url
last_verified
notes
```

### Update a journal row

Edit `data/journals_reputable.csv`, then update:

```text
jcr_quartile_or_rank_note
sjr_quartile_note
metric_source_url
journal_url
last_verified
notes
```

## Local full-maintenance workflow

Use this for larger updates or before a formal release.

```bash
git clone https://github.com/tirthajit/ai-ml-conference-journal-tracker.git
cd ai-ml-conference-journal-tracker
python scripts/validate_data.py
python scripts/build_static_site.py
git status
git add .
git commit -m "Update tracker data and website"
git push
```

## Creating the first GitHub release

1. Open the repository on GitHub.
2. Click **Releases** on the right sidebar, or open:

```text
https://github.com/tirthajit/ai-ml-conference-journal-tracker/releases/new
```

3. Click **Choose a tag**.
4. Type:

```text
v1.0.0
```

5. Select **Create new tag: v1.0.0 on publish**.
6. Release title:

```text
v1.0.0 — Initial public release
```

7. Paste the release notes from `RELEASE_NOTES_v1.0.0.md`.
8. Attach the Excel file from `exports/` if desired.
9. Click **Publish release**.

## Linking from your personal webpage

Add a compact project card to `https://tirthajit.github.io/`:

```markdown
### AI/ML Conference & Journal Tracker

A curated tracker of reputable AI/ML conferences and journals, including rankings, submission deadlines, tentative annual windows, and source links.

[View Repository](https://github.com/tirthajit/ai-ml-conference-journal-tracker) · [Browse Tracker](https://tirthajit.github.io/ai-ml-conference-journal-tracker/)
```

## Data-quality rules

- Do not mark a deadline as `Official announced` without an official source URL.
- Use ISO dates: `YYYY-MM-DD`.
- Keep `AoE` or a clear timezone where known.
- Do not mix tentative and official deadlines without a confidence label.
- Avoid generic CFP aggregators unless no official page is available.
- Keep CSV files as the canonical source; Excel is a convenience export.
