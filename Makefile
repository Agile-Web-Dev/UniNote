lint:
	flake8 app app.py config.py app/models.py migrations/env.py
format:
	isort app app.py config.py app/models.py migrations/env.py && black app app.py config.py app/models.py migrations/env.py
install:
	pip install -r requirements.txt
run:
	flask run
test:
	pytest