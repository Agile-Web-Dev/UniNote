# CITS3403 Project

- [CITS3403 Project](#cits3403-project)
  - [Team Members](#team-members)
  - [Project Overview](#project-overview)
    - [Architecture](#architecture)
    - [Tooling](#tooling)
  - [Project Setup](#project-setup)
  - [Development](#development)
  - [Tests](#tests)
  - [Database](#database)
  - [Contributions](#contributions)

## Team Members

- @BoboJeager
- @dct0
- @jsun1590

## Project Overview

Sample text.

### Architecture

### Tooling

- alembic for database migrations
- black for code formatting
- flake8 for linting
- isort for import sorting
- pytest for unit tests

## Project Setup

1. Copy `.env.example` to `.env` and modify the values.
2. create a virtual environment with `python3 -m venv env`.
3. Source the virtual environment with `source env/bin/activate`
   1. or `.\env\Scripts\activate.bat`) on Windows Command Prompt
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
- Formatting is done with `isort app app.py config.py app/models.py migrations/env.py` and `black app app.py config.py app/models.py migrations/env.py`.

## Tests

- For e2e tests, download and add ChromeDriver to your PATH variable per the instructions [here](https://chromedriver.chromium.org/getting-started).
- Run `pytest` to run all unit and end to end (e2e) tests.

## Database

- To generate a migration run `flask db migrate -m "<message>"`.
- Initialize the database using `flask db upgrade`.

todo:

- [ ] create strings for visual representation of data

## Contributions
