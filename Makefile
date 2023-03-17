lint:
	flake8 app
format:
	isort app && black app
install:
	pip install -r requirements.txt
run:
	flask run
test:
	pytest