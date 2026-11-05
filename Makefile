.PHONY: setup check lint validate spell test

PY ?= python3

setup:
	$(PY) -m pip install -r requirements-dev.txt

check: lint validate spell test
	@echo "make check: OK"

lint:
	ruff check scripts tests

validate:
	$(PY) scripts/validate_schemas.py

spell:
	@if command -v codespell >/dev/null 2>&1; then \
		codespell --ignore-words=.codespell-ignore MASTER_PROMPT.md HANDOFF.md README.md CONTRIBUTING.md NOTICE docs prompts schemas examples; \
	else echo "codespell not installed; skipping (run 'make setup'). CI runs it."; fi

test:
	$(PY) -m pytest -q tests
