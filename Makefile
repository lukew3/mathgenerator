FLAKE_FLAGS = --ignore=E501,F401,F403,F405

lint:
	python -m flake8 $(FLAKE_FLAGS)

test:
	python -m pytest --verbose -s tests
