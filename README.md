# AI/ML Conference & Journal Tracker

[![Data validation](https://img.shields.io/badge/data-validation_ready-blue)](#data-quality)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC--BY--4.0-green.svg)](LICENSE)
[![Last verified](https://img.shields.io/badge/last_verified-2026-06-27-informational)](data/sources.csv)

A curated, ranked, source-backed tracker for reputable AI/ML conferences and journals.

This repository is designed for researchers who need a fast way to decide **where to submit**, **when to prepare**, and **which sources to verify** before final submission.

> Maintainer note: conference deadlines move often. Always verify the official CFP before submission.

## What is included

| File | Purpose |
|---|---|
| `data/conferences_master.csv` | General ranked AI/ML conference list with tentative windows and source URLs |
| `data/submission_calendar_current_cycle.csv` | Date-sorted current/next-cycle tracker |
| `data/journals_reputable.csv` | Reputable AI/ML/vision/medical-imaging journals with target tiers |
| `data/sources.csv` | Source registry used by the tracker |
| `docs/` | GitHub Pages-ready public website |
| `scripts/validate_data.py` | Lightweight CSV validation |
| `schemas/` | Machine-readable column schemas |

## Rank/tier convention

This project uses a practical target tier in addition to any available CORE rank.

| Tier | Meaning |
|---|---|
| **S** | Global flagship / most selective field-defining venue |
| **A** | Major reputable archival venue |
| **B** | Solid specialist/regional venue |
| **C** | Niche venue; verify fit and indexing carefully |

`core_rank_prefill` is included only as a convenience field. Treat CORE as a separate source to verify, not as the sole decision criterion.

## Upcoming deadlines from this snapshot

| curated_tier | acronym | current_or_next_edition | full_paper_deadline | timezone | deadline_confidence |
| --- | --- | --- | --- | --- | --- |
| B | ICONIP | ICONIP 2026 | 2026-06-30 | AoE | Tentative window |
| A | ACCV | ACCV 2026 | 2026-07-05 | AoE | Tentative window |
| A | SIGMOD | SIGMOD 2027 | 2026-07-10 | AoE | Tentative / multi-round |
| A | AIES | AIES 2026 | 2026-07-10 | AoE | Tracker / historical pattern |
| B | INLG | INLG 2026 | 2026-07-10 | AoE | Tracker / historical pattern |
| A | ICDE | ICDE 2027 | 2026-07-15 | AoE | Tentative / multi-cycle |
| A | CSCW | CSCW 2027 | 2026-07-15 | AoE | Rolling / multiple cycles |
| B | GROUP | GROUP 2027 | 2026-07-15 | AoE | Tentative window |
| S | AAAI | AAAI-27 | 2026-07-28 | AoE | Official announced |
| A | NDSS | NDSS 2027 | 2026-07-30 | AoE | Tentative / cycles |
| A | HPCA | HPCA 2027 | 2026-08-01 | AoE | Tentative window |
| A | WSDM | WSDM 2027 | 2026-08-10 | AoE | Tentative window |
| A | 3DV | 3DV 2027 | 2026-08-15 | AoE | Tentative window |
| B | IEEE BIBM | BIBM 2026 | 2026-08-15 | AoE | Tentative window |

## S-tier conference preview

| acronym | name | area | current_or_next_edition | full_paper_deadline | usual_tentative_window |
| --- | --- | --- | --- | --- | --- |
| CVPR | IEEE/CVF Conference on Computer Vision and Pattern Recognition | Computer Vision | CVPR 2026 | 2025-11-13 | Nov |
| ECCV | European Conference on Computer Vision | Computer Vision | ECCV 2026 | 2026-03-05 | Mar |
| ICCV | IEEE/CVF International Conference on Computer Vision | Computer Vision | ICCV 2027 | 2027-03-07 | Mar |
| ICML | International Conference on Machine Learning | Core ML | ICML 2026 | 2026-01-28 | Jan |
| NeurIPS | Conference on Neural Information Processing Systems | Core ML / AI | NeurIPS 2026 | 2026-05-06 | May |
| ICLR | International Conference on Learning Representations | Core ML / Deep Learning | ICLR 2026 | 2025-09-24 | Sep |
| KDD | ACM SIGKDD Conference on Knowledge Discovery and Data Mining | Data Mining | KDD 2026 | 2026-02-08 | Aug & Feb cycles |
| AAAI | AAAI Conference on Artificial Intelligence | General AI | AAAI-27 | 2026-07-28 | Jul-Aug |
| IJCAI | International Joint Conference on Artificial Intelligence | General AI | IJCAI-ECAI 2026 | 2026-01-19 | Jan |
| SIGGRAPH | ACM SIGGRAPH | Graphics / Vision Adjacent | SIGGRAPH 2027 | 2027-01-20 | Jan |
| CHI | ACM CHI Conference on Human Factors in Computing Systems | HCI / Human-centered AI | CHI 2027 | 2026-09-10 | Sep |
| SIGIR | ACM SIGIR Conference on Research and Development in Information Retrieval | Information Retrieval | SIGIR 2026 | 2026-01-22 | Jan |
| MICCAI | International Conference on Medical Image Computing and Computer Assisted Int... | Medical Imaging | MICCAI 2026 | 2026-02-26 | Feb |
| ACM MM | ACM Multimedia | Multimedia / Vision / Audio | ACM MM 2026 | 2026-04-01 | Mar-Apr |
| ACL | Annual Meeting of the Association for Computational Linguistics | NLP | ACL 2026 | 2026-01-05 | Jan / ARR cycles |
| EMNLP | Conference on Empirical Methods in Natural Language Processing | NLP | EMNLP 2026 | 2026-05-25 | May / ARR cycles |
| ICRA | IEEE International Conference on Robotics and Automation | Robotics | ICRA 2027 | 2026-09-15 | Sep |
| RSS | Robotics: Science and Systems | Robotics | RSS 2026 | 2026-01-30 | Jan |
| TheWebConf | The ACM Web Conference | Web / Data Mining | WWW/TheWebConf 2027 | 2026-10-10 | Oct |

## Recommended GitHub Pages setup

1. Create a public repository, suggested name: `ai-ml-conference-journal-tracker`.
2. Upload this repository structure.
3. Go to **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select branch `main` and folder `/docs`.
6. Save. Your site will be published as a GitHub Pages website.

## Updating workflow

1. Edit the relevant CSV in `data/`.
2. Add or update the source URL in `data/sources.csv`.
3. Run:

```bash
python scripts/validate_data.py
python scripts/build_markdown_tables.py
```

4. Commit with a clear message:

```bash
git add data docs
git commit -m "Update AAAI-27 and WACV 2027 deadlines"
git push
```

## Data quality

Each deadline row has a `deadline_confidence` value:

- `Official announced` — official conference site or CFP found.
- `Tracker / historical pattern` — credible deadline tracker or past-year pattern.
- `Tentative window` — estimated from normal annual cadence; verify before relying on it.
- `Rolling / multiple cycles` — venue has multiple or rolling deadlines.

## Scope

Included: reputable archival conferences, major field venues, and selected adjacent venues where AI/ML papers are common.

Excluded by default: local low-selectivity conferences, generic commercial AI events, workshops without proceedings, and predatory venues.

## Citation

Use `CITATION.cff` or cite the repository URL once published.
