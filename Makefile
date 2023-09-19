install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black scripts/*.py
	nbqa black scripts/*.ipynb 
lint:
	ruff check scripts/*.py
	nbqa ruff scripts/*.ipynb
	
test:
	python -m pytest -vv --cov=scripts.descstats test_descstats.py
	python -m pytest -vv --cov=scripts.lib test_lib.py
	python -m pytest --nbval scripts/*.ipynb

all: 
	install format lint test
