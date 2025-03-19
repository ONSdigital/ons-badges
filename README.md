
![Logo](logo.png)

# ons-badges

A way to create ONS themed badges for use in GitHub repositories.

## Prerequisites

- Python 3.13
- Poetry

### Installing Python 3.13:

If you don't have Python 3.13 installed, you can install it using pyenv. Follow the instructions below to install pyenv and Python 3.13:

```bash
brew install pyenv
pyenv install 3.13.0
```

### Install Poetry:
   - This project uses Poetry for dependency management. Ensure Poetry is installed on your system.
   - If Poetry is not installed, you can install it using:
```bash
brew install pipx
pipx install poetry
```
- Use the official Poetry installation guide for other installation methods: https://python-poetry.org/docs/#installation
- Verify the installation by using the following command:
```bash
poetry --version
```


## Running the service

```bash
poetry run dev
```

## Linting

```bash
ruff lint
```
## Example use

`http://127.0.0.1:5005/api/badge/standard?left_text=hello&right_text=world`
