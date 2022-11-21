VENV = Finance_API3.9
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip3
SHELL := /bin/bash

all: venv


run:
	clear
	uvicorn app:app --reload



$(VENV)/bin/activate: requirements.txt
	clear
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt


venv: $(VENV)/bin/activate


clean:
	clear
	rm -rf __pycache__
	rm -rf $(VENV)


version:
	$(PYTHON) --version

.PHONY: all run clean version