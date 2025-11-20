PYTHON ?= python
VENV := .venv
PIP := $(VENV)/Scripts/python -m pip
PY := $(VENV)/Scripts/python

.PHONY: venv install test clean

venv:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip setuptools wheel

install: venv
	$(PIP) install -e . pytest

test:
	$(PY) -m pytest -q

clean:
	# Remove build artifacts and editable installs
	-@powershell -NoProfile -Command "Remove-Item -Recurse -Force build,dist,*.egg-info -ErrorAction SilentlyContinue"
