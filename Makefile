VENV := $(HOME)/.venv
PY   := $(VENV)/bin/python
PIP  := $(VENV)/bin/pip
RUFF := $(VENV)/bin/ruff
MYPY := $(VENV)/bin/mypy

.PHONY: install test lint type

install:
	$(PY) -m pip install -e .
	$(PIP) install pytest ruff mypy

test:
	$(PY) -m pytest -q

lint:
	$(RUFF) check src/judge tests

type:
	$(MYPY) src/judge
