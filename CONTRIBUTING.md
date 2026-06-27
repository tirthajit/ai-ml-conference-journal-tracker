# Contributing

Contributions are welcome if they improve accuracy, source quality, or usability.

## What to submit

Good update requests include:

- Official CFP or conference page.
- Journal publisher page.
- Ranking or metric source page.
- Clear old value and new value.
- Deadline timezone, if applicable.
- Date on which the source was checked.

## Preferred source hierarchy

1. Official conference or journal website.
2. Publisher, society, or association page.
3. Recognized ranking or indexing database.
4. Reputable deadline tracker.
5. Historical inference, marked clearly as tentative.

## Pull request checklist

Before opening a pull request:

- Run `python scripts/validate_data.py`.
- Use ISO dates: `YYYY-MM-DD`.
- Include a source URL for every official deadline.
- Update `CHANGELOG.md`.
- Keep tables and CSV rows sorted where appropriate.

## Style rules

- Use concise notes.
- Do not add predatory, generic, or unverifiable venues.
- Do not overstate journal metrics; metrics change annually.
- Mark historical estimates as tentative.
