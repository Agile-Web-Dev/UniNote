# CITS3403 Project

- [CITS3403 Project](#cits3403-project)
  - [Team Members](#team-members)
  - [Project Overview](#project-overview)
    - [Architecture](#architecture)
    - [Tooling](#tooling)
      - [Backend](#backend)
  - [Dependencies](#dependencies)
  - [Project Setup](#project-setup)
  - [Development](#development)
  - [Tests](#tests)
  - [Database](#database)
  - [Seeding](#seeding)
  - [Deployment](#deployment)
  - [Contributions](#contributions)

## Team Members

- @BoboJeager (Danish Hillman)
- @dct0 (Dylan To)
- @jsun1590 (Jack Sun)

## Project Overview



### Architecture


This project uses a mix of client-side and server-side rendering via Jinja2 templates. Of course we try to use server-side rendering as much as possible to reduce load times and achieve a faster First Contentful Paint. However, we made some exceptions for the sake of a better development experience. In particular, the chatroom pages are rendered client-side with javascript making API calls to fetch all the message data. This is because the logic to render the messages are written in javascript and it would violate the Don't Repeat Yourself (DRY) principle to rewrite the logic in python.

The backend architecture closely resembles that of Django, where each feature is organised into an app. All apps contain a `routes` folder which makes extensive use of flask blueprints to route everything together. All apps attempt to follow the RESTful API design pattern, with the exception of the `main` app which is used for serving the Jinja2 templates as well as some authentication endpoints which perform redirects that are not RESTful.

Additionally, most apps contain a `tests` folder which contains both end to end and unit tests. The end to end (e2e) tests are written using Selenium and ChromeDriver. Both the unit and end to end tests are run using pytest. The fixtures for both type of tests are also written in pytest.


### Tooling
#### Backend
- alembic for database migrations
- black for code formatting
- flake8 for linting
- isort for import sorting
- pytest for unit tests
- djLint for Django Jinja template linting and formatting

## Dependencies
- 
## Project Setup

1. Copy `.env.example` to `.env` and modify the values.
2. create a virtual environment with `python3 -m venv env`.
3. Source the virtual environment with `source env/bin/activate`
   1. or `.\env\Scripts\activate.bat` on Windows Command Prompt
   2. or `.\env\Scripts\Activate.ps1` on Windows Powershell.
4. Install the dependencies with `pip install -r requirements.txt`.
   1. You may need to install `python-dotenv` outside the virtual environment.
5. Run the server with `flask run`.

## Development

On UNIX like systems:

- Linting is done with `make lint`.
- Formatting is done with `make format`.

Otherwise:

- Linting is done with `flake8 app app.py config.py app/models.py migrations/env.py` and `djlint app`.
- Formatting is done with `isort --profile black app app.py config.py app/models.py migrations/env.py` and `black app app.py config.py app/models.py migrations/env.py`.

## Tests

- For e2e tests, download and add ChromeDriver to your PATH variable per the instructions [here](https://chromedriver.chromium.org/getting-started).
- Run `pytest` to run all unit and end to end (e2e) tests.

## Database

- To generate a migration run `flask db migrate -m "<message>"`.
- Initialize the database using `flask db upgrade`.

## Seeding

- To seed the database run

```sh
python -m scripts.seed_db
```

## Deployment
This project employs a Github Actions CI/CD pipeline to automate the deployment process and maintain the code quality and consistency. The CI pipeline is triggered on every commit and contains steps to:
- Install dependencies
- 

This project is deployed to [Railway](https://railway.app), an alternative to Heroku. It is hosted [here](https://agwp-production.up.railway.app/) The deployment is done automatically via a CD pipeline. The deployment is triggered on every push to the `main` branch. The deployment is done by running a series of scripts that first installs the dependencies, then runs the migrations and seeds the database.

The deplyment uses a Procfile to specify the commands to run during deployment. The production server is run using gunicorn, which servers both the Flask server and static files as well as bootstraps the socket.io worker with gevent-websocket.

## Contributions
