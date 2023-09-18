install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py
	nbqa black *.ipynb 
lint:
	ruff check *.py
	nbqa ruff *.ipynb
	
test:
	python -m pytest -vv --cov=descstats test_descstats.py
	python -m pytest -vv --cov=lib test_lib.py
	python -m pytest --nbval *.ipynb

all: 
	install format lint test
