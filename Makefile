lint:
	flake8 app app.py config.py models.py migration/env.py
format:
	isort app app.py config.py models.py migration/env.py && black app app.py config.py models.py migration/env.py
install:
	pip install -r requirements.txt
run:
	flask run
test:
	pytest