FLAKE_FLAGS = --ignore=E501,F401,F403,F405

lint:
	python3 -m flake8 $(FLAKE_FLAGS)

test:
	python3 -m pytest --verbose -s tests
