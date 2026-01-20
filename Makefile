install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

lint:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format:
	black .

test:
	pytest

build:
	docker build -t wine-quality-api .
