install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black src/*.py
	nbqa black src/*.ipynb 
lint:
	ruff check src/*.py
	nbqa ruff src/*.ipynb
	
test:
	python -m pytest -vv --cov=src.descstats test_descstats.py
	python -m pytest -vv --cov=src.lib test_lib.py
	python -m pytest --nbval src/*.ipynb

all: 
	install format lint test
