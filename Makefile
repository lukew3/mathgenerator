IGNORE_ERRORS = E501,F401,F403,F405
PKG = mathgenerator
PYTHON ?= python3

deps:
	$(PYTHON) -m pip install --user -r dev-requirements.txt

format:
	$(PYTHON) -m autopep8 --ignore=$(IGNORE_ERRORS) -ir $(PKG)/*

lint:
	$(PYTHON) -m flake8 --ignore=$(IGNORE_ERRORS) $(PKG)

test:
	$(PYTHON) -m pytest --verbose -s tests
