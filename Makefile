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

add_commit_push:
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add denirohist.png report.md; \
		git commit -m "Add generated plot image"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi

update_readme:
	cat report.md >> README.md
	git add README.md
	git commit -m "merge readmes"
	git push  

all: 
	install format lint test
