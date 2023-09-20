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
	python -m pytest -vv --cov=scripts scripts/test_*.py
	python -m pytest --nbval scripts/*.ipynb

report:

all: 
	install format lint test
