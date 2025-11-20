# hello-python-playground

A minimal Python "Hello World" development playground scaffold. Use this repository to experiment with Python packages, testing, linting, and CI.

Quick start

1. Create a virtual environment

   python -m venv .venv
   . .venv\Scripts\Activate.ps1

2. Install dev dependencies

   pip install -r requirements.txt

3. Run tests

   pytest -q

Files of interest

- `src/playground` - main package
- `tests` - pytest test suite
- `.github/workflows/ci.yml` - GitHub Actions workflow for tests
- `pyproject.toml` - build and tool config

## Development setup (exact commands I ran)

Prefer PowerShell on Windows. From the project root run:

```powershell
# Create and activate a virtual environment
python -m venv .venv
. .venv\Scripts\Activate.ps1

# Upgrade packaging tools and install editable package + test runner
python -m pip install --upgrade pip setuptools wheel
# hello-python-playground

[![CI](https://github.com/gatorMiner/hello-python-playground/actions/workflows/ci.yml/badge.svg)](https://github.com/gatorMiner/hello-python-playground/actions)

A minimal Python "Hello World" development playground scaffold. Use this repository to experiment with Python packages, testing, linting, and CI.

Quick start

1. Create a virtual environment

   python -m venv .venv
   . .venv\Scripts\Activate.ps1

2. Install dev dependencies

   pip install -r requirements.txt

3. Run tests

   pytest -q

Files of interest

- `src/playground` - main package
- `tests` - pytest test suite
- `.github/workflows/ci.yml` - GitHub Actions workflow for tests
- `pyproject.toml` - build and tool config

## Development setup (exact commands I ran)

Prefer PowerShell on Windows. From the project root run:

```powershell
# Create and activate a virtual environment
python -m venv .venv
. .venv\Scripts\Activate.ps1

# Upgrade packaging tools and install editable package + test runner
python -m pip install --upgrade pip setuptools wheel
python -m pip install -e . pytest

# Run the test suite
pytest -q
```

Makefile (cross-platform convenience)

You can also use the provided `Makefile` targets. On Windows with GNU Make installed, run:

```powershell
make venv     # creates venv and upgrades pip/setuptools/wheel
make install  # installs editable package and pytest into the venv
make test     # runs pytest using the venv's python
make clean    # remove build artifacts
```

Notes

- When using PowerShell, prefix activation with a dot and a space: `. .venv\Scripts\Activate.ps1`.
- If `python` points to the Microsoft Store stub, install CPython from https://www.python.org/ and choose “Add Python to PATH”.
- The project is installed in editable mode so changes in `src/playground` are reflected immediately when running tests.

## Contributing

Thanks for wanting to contribute — this is a small learning playground so we keep things simple.

- Run the Makefile targets locally to prepare and test changes:
   - `make venv` — create `.venv` and upgrade packaging tools
   - `make install` — install the package in editable mode and `pytest`
   - `make test` — run the test suite
- Create a feature branch locally, e.g. `git checkout -b feat/my-change`.
- Make small, focused commits and run `make test` before pushing.
- Push the branch and open a Pull Request on GitHub. Use the web UI or `gh`:

```powershell
# push new branch and open a PR
git push -u origin feat/my-change
gh pr create --fill
```

- Keep PRs small. When your tests pass and at least one reviewer approves, merge into `main`.

We intentionally avoid heavy admin rules here — the CI will run tests on push and PRs, but merging is lightweight so you can iterate quickly.

## Creating and pushing a new GitHub repo (PowerShell script)

This repository includes a helper PowerShell script `create_and_push_with_gh.ps1` to create a GitHub repository from the current folder and push the code, intended to be run from Windows PowerShell when the folder is a standalone project root.

Prerequisites

- `git` installed and available on PATH
- GitHub CLI `gh` installed and authenticated (the script will prompt to run `gh auth login` if needed)
- PowerShell (Windows PowerShell or PowerShell Core)

Basic usage

Run from the project root (the script defaults the repository name to the current folder name):

```powershell
# Run interactively; defaults to public repo and current folder name
.\create_and_push_with_gh.ps1 -GitHubUser your-github-username
```

Options

- `-RepoName <name>` : explicitly set the repo name (default: current folder name)
- `-Visibility public|private` : set repo visibility (default: public)
- `-Force` : allow creating a nested git repo inside an existing parent repo (not recommended)

Notes

- If your folder is inside another git repository, the script will abort unless you pass `-Force`.
- The script tries to use `winget` to install `gh` if missing, otherwise it instructs you to install `gh` manually.
- The script will attempt an initial commit if none exists.

