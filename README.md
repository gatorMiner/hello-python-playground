# hello-python-playground

A minimal Python "Hello World" development playground scaffold. Use this repository to experiment with Python packages, testing, linting, and CI.

Quick start

1. Create a virtual environment

   python -m venv .venv
   .venv\Scripts\Activate.ps1

2. Install dev dependencies

   pip install -r requirements.txt

3. Run tests

   pytest -q

Files of interest

- `src/playground` - main package
- `tests` - pytest test suite
- `.github/workflows/ci.yml` - GitHub Actions workflow for tests
- `pyproject.toml` - build and tool config
