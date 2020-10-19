IGNORE_ERRORS = E501,F401,F403,F405
PKG = mathgenerator

format:
	python -m autopep8 --ignore=$(IGNORE_ERRORS) -i $(PKG)/*

lint:
	python -m flake8 --ignore=$(IGNORE_ERRORS) $(PKG)

test:
	python -m pytest --verbose -s tests
