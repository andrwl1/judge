.PHONY: test install
install:
	python -m pip install -e .
	pip install pytest
test:
	python -m pytest -q
