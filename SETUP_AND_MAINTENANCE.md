# Setup and Maintenance Guide

This guide assumes the maintainer is using the GitHub username `tirthajit` and wants the project site at:

```text
https://tirthajit.github.io/ai-ml-conference-journal-tracker/
```

## One-time setup from GitHub web

1. Create a new public repository named `ai-ml-conference-journal-tracker`.
2. Do not initialize it with a README, license, or `.gitignore` if you are uploading this package, because those files are already included.
3. Extract this ZIP file.
4. Upload the **contents inside** the `ai-ml-conference-journal-tracker/` folder to the repository root.
5. Commit with: `Initial release: AI/ML conference and journal tracker`.
6. Go to **Settings → Pages**.
7. Under **Build and deployment**, choose **Deploy from a branch**.
8. Select branch `main` and folder `/docs`.
9. Save.
10. After deployment, the website should be available at `https://tirthajit.github.io/ai-ml-conference-journal-tracker/`.

## Repository metadata

Use this description:

```text
Ranked AI/ML conference and journal tracker with submission deadlines, tentative annual windows, source links, and update status.
```

Use these topics:

```text
artificial-intelligence, machine-learning, conferences, journals, research, deadlines, academic-publishing, computer-vision, nlp, data-mining, medical-imaging, robotics
```

## Web-only update workflow

For most updates, edit files directly on GitHub.

### Updating a conference deadline

1. Open `data/submission_calendar_current_cycle.csv`.
2. Click the edit pencil.
3. Update the relevant row.
4. Update at least these fields: `full_paper_deadline`, `timezone`, `deadline_confidence`, `source_url`, `last_verified`, and `notes`.
5. Commit with a specific message, e.g. `Update AAAI-27 deadline source`.
6. Update `CHANGELOG.md` with one short bullet.

### Updating the general conference list

Edit `data/conferences_master.csv` when the venue itself changes: rank, name, area, usual deadline window, or source.

### Updating journals

Edit `data/journals_reputable.csv` when adding a journal or updating metrics/ranking source notes.

## Local update workflow

Use this when making many edits.

```bash
git clone https://github.com/tirthajit/ai-ml-conference-journal-tracker.git
cd ai-ml-conference-journal-tracker
python scripts/validate_data.py
python scripts/build_markdown_tables.py
git add .
git commit -m "Update conference deadlines"
git push
```

For later updates:

```bash
cd ai-ml-conference-journal-tracker
git pull
# edit CSV/Markdown files
python scripts/validate_data.py
python scripts/build_markdown_tables.py
git add .
git commit -m "Update current-cycle deadlines"
git push
```

## Maintenance rules

- Keep CSV files as the source of truth.
- Use ISO dates: `YYYY-MM-DD`.
- Use `AoE` when the conference uses Anywhere on Earth time.
- Do not mix official and guessed deadlines without labeling them.
- Prefer official CFP/conference pages for deadlines.
- Update `last_verified` whenever a row is checked.
- Add a `CHANGELOG.md` entry for visible updates.
