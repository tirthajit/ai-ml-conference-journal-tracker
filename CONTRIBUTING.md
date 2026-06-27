# Contributing

Contributions are welcome if they improve accuracy, source quality, or coverage.

## Rules for updates

1. Prefer official conference/journal pages.
2. If using a tracker, label the row as `Tracker / historical pattern`.
3. Do not replace an official source with an unofficial one.
4. For tentative deadlines, use a month/window and clearly mark the confidence.
5. Keep venue names normalized:
   - NeurIPS, not NIPS
   - The ACM Web Conference, not WWW only
   - ECML PKDD, not ECML alone
   - IJCAI-ECAI when the year is a joint edition

## Pull request checklist

- [ ] CSV validates with `python scripts/validate_data.py`
- [ ] Source URL added or updated
- [ ] Date is in `YYYY-MM-DD` when exact
- [ ] `deadline_confidence` is correct
- [ ] Notes mention any renamed or joint editions
