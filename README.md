# CITS3403 Project

## Team Members

- @BoboJeager
- @dct0
- @jsun1590

## Project Overview

Sample text.

### Architecture

### Tooling

- black for code formatting
- flake8 for linting
- isort for import sorting
- pytest for unit tests

## Project Setup

1. Copy `.env.example` to `.env` and modify the values.
2. create a virtual environment with `python3 -m venv env`.
3. Source the virtual environment with `source env/bin/activate`.
4. Install the dependencies with `pip install -r requirements.txt`.
5. Run the server with `flask run`.

## Development

On UNIX like systems:

- Linting is done with `make lint`.
- Formatting is done with `make format`.

Otherrwise:

- Linting is done with `flake8 app`.
- Formatting is done with `black app && isort app`.

## Tests

- Run `pytest` to run all unit tests.

## Contributions
