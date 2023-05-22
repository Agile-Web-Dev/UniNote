# CITS3403 Project

- [CITS3403 Project](#cits3403-project)
  - [Team Members](#team-members)
  - [Project Overview](#project-overview)
    - [Architecture](#architecture)
    - [Tooling](#tooling)
    - [Frontend](#frontend)
      - [Backend](#backend)
  - [Dependencies](#dependencies)
    - [Frontend](#frontend-1)
    - [Backend](#backend-1)
  - [Project Setup](#project-setup)
  - [Development](#development)
  - [Tests](#tests)
  - [Database](#database)
  - [Deployment](#deployment)
  - [Contributions](#contributions)

## Team Members

- @BoboJeager (Danish Hillman)
- @dct0 (Dylan To)
- @jsun1590 (Jack Sun)

## Project Overview

UniNote is a chatroom that connects students, tutors and lecturers in a shared working space.
This application hopes to encourage collaboration between students through chatrooms and shared notes.
Additionally students are able to accelerate their learning by asking questions and discuss class topics with an integrated GPT bot. The bot is able to answer questions and provide summarised solutions based on the shared notes forum. This is packaged in an all-in-one platform that provides quick and easy access to everything a student needs in one place.

### Architecture

This project uses a mix of client-side and server-side rendering via Jinja2 templates. Of course we try to use server-side rendering as much as possible to reduce load times and achieve a faster First Contentful Paint. However, we made some exceptions for the sake of a better development experience. In particular, the chatroom pages are rendered client-side with javascript making API calls to fetch all the message data. This is because the logic to render the messages are written in javascript and it would violate the Don't Repeat Yourself (DRY) principle to rewrite the logic in python.

The backend architecture closely resembles that of Django, where each feature is organised into an app. The motivation behind this design choice is to improve the modularity of the codebase and to make it easier to maintain and extend. It allows tests to be written for each feature in a more isolated fashion and again, improved modularity.

All apps contain a `routes` folder which makes extensive use of flask blueprints to route everything together. All apps attempt to follow the RESTful API design pattern, with the exception of the `main` app which is used for serving the Jinja2 templates as well as some authentication endpoints which perform redirects that are not RESTful.

Additionally, most apps contain a `tests` folder which contains both end to end and unit tests. The end to end (e2e) tests are written using Selenium and ChromeDriver. Both the unit and end to end tests are run using pytest. The fixtures for both type of tests are also written in pytest.

### Tooling

### Frontend

- Prettier (as a VSCode extension) for code formatting
- djLint for Django Jinja template linting and formatting

#### Backend

- alembic for database migrations
- black for code formatting
- flake8 for linting
- isort for import sorting
- pytest for unit tests

## Dependencies

### Frontend

The project uses the following javascript libraries:

- [Popper.js](https://popper.js.org/) for Bootstrap
- [Socket.io](https://socket.io/) for real-time messaging
- [Emoji Mart](https://github.com/missive/emoji-mart) for emoji picker keyboard

Additionally, the following CSS libraries are used:

- [Reset CSS](https://meyerweb.com/eric/tools/css/reset/) for resetting default browser styles to a consistent baseline
- [Bootstrap](https://getbootstrap.com/) for styling
- [Bootstrap Icons](https://icons.getbootstrap.com/) for icons

### Backend

The project has been tested on Python >3.10.10. The dependencies are listed in `requirements.txt`.

## Project Setup

1. Copy `.env.example` to `.env` and modify the values accordingly.
2. create a virtual environment with `python -m venv env`.
3. Source the virtual environment with `source env/bin/activate`
   1. or `.\env\Scripts\activate.bat` on Windows Command Prompt
   2. or `.\env\Scripts\Activate.ps1` on Windows Powershell.
4. Install the dependencies with `pip install -r requirements.txt`.
5. Initialise the database with `flask db upgrade`.
6. Run the server with `flask run`.

## Development

This project unconventionally uses `make` to store common set up and development scripts inside a Makefile to improve the developer experience. This is very similar to how npm scripts works but as we do not have a `package.json` file, we use `make` as a substitute instead. `make` is only available on UNIX like systems by default. The following commands are available:

- `make lint`
- `make format`
- `make install`
- `make run`
- `make test`
- `make seed`

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
- To initialise and apply migrations to the database run `flask db upgrade`.
- To seed the database run `python -m scripts.seed_db`

## Deployment

This project employs a Github Actions CI/CD pipeline to automate the deployment process and maintain the code quality and consistency. The CI pipeline is triggered on every commit and contains steps to:

- Set up a Python environment
- Install chrome and chromedriver for e2e tests
- Install dependencies
- Run linter
- Run migrations
- Run unit and e2e tests
- Output a test coverage report

This project is deployed to [Railway](https://railway.app), an alternative to Heroku. It is hosted [here](https://agwp-production.up.railway.app/) The deployment is done automatically via a CD pipeline. The deployment is triggered on every push to the `main` branch. The deployment is done by running a series of scripts that first installs the dependencies, then runs the migrations and seeds the database.

The deplyment uses a Procfile to specify the commands to run during deployment. The production server is run using gunicorn, which servers both the Flask server and static files as well as bootstraps the socket.io worker with gevent-websocket.

## Contributions
