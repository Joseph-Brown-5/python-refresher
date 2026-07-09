# Python Refresher

Following along with a Python course to refresh my knowledge.

## Layout

- `lessons/` — one file per topic/section as you follow the course (e.g. `01_variables.py`, `02_loops.py`). Throwaway, just for following along.
- `exercises/` — practice problems, kept separate from lesson code so they don't get overwritten when you re-run a lesson file.
- `projects/` — any bigger mini-projects the course has you build, each in its own subfolder (e.g. `projects/calculator/`).
- `notes.md` — quick personal notes / cheatsheet as you learn things worth remembering.
- `.venv/` — virtual environment (not committed, machine-specific).
- `requirements.txt` — any third-party packages the course has you install.

## Setup (first time)

```
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Day to day

1. Activate the venv: `.venv\Scripts\activate` (do this every new terminal session)
2. Create/open a file under `lessons/` for whatever topic you're on.
3. Run it: `python lessons/01_variables.py`
4. If the course gives you a package to install, add it to `requirements.txt` and `pip install -r requirements.txt`.
