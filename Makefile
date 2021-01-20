VENV_NAME?=.venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=$(if $(CI), /usr/bin/env python3 ,$(VENV_NAME)/bin/python3)

all: init

clean: clean-venv

clean-venv:
	@rm -rf .venv

init: venv

venv: .git $(VENV_ACTIVATE)

$(VENV_ACTIVATE):
	test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
	$(PYTHON) -m pip install -qU pip
	$(PYTHON) -m pip install -qr requirements.txt
	$(PYTHON) -m pre_commit install
.git:
	git init

test: $(if $(CI), ,init)
	$(PYTHON) -m pytest -vv tests

lint: $(if $(CI), ,init)
	$(PYTHON) -m flake8 --statistics --count

run: $(if $(CI), ,init)
	$(PYTHON) eva_api/eva_api.py

.PHONY: clean clean-venv
