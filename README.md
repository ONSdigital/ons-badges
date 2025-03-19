# sdx-fastapi-boilerplate
A boilerplate for creating fastapi services

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

## Generate `.env`

To use environment variables, you need to create a `.env` file in the root directory of the project. You can copy the `.env.example` file and rename it to `.env`:

```bash
cp .env.example .env
```

## Running the service

```bash
poetry run dev
```

## Linting

```bash
ruff lint
```

## Installed by default

### Config class

The config class in `config.py` is used to store static and environment variables and use these values throughout the application using the `SETTINGS` object. E.g ...

```python
from app.config import SETTINGS

print(f"Project ID is {SETTINGS.project_id}")
```

### Loggy

Loggy is a logging utility class that is in `app/facades/loggy.py`. It has been set up in `main.py` so to use it throughout the application you can import it and use any of the various static methods to log messages. E.g ...

```python

from app.facades.loggy import Loggy

Loggy.info("Hello world", logger="uvicorn") # Use the uvicorn logger
Loggy.info("This is an info message")       # Use the default logger
Loggy.warning("Warning message")            # Log a warning message
Loggy.error("Error message")                # Log an error message
Loggy.log_table_info(
        "New Table",
        ["Header 1", "Header 2"],
        [
            ["Row 1", "Row 2"],
            ["Row 3", "Row 4"],
        ]
    )

"""
New Table
=========
+------------+------------+
| Header 1   | Header 2   |
+============+============+
| Row 1      | Row 2      |
+------------+------------+
| Row 3      | Row 4      |
+------------+------------+

"""
```

### Singleton meta

The `SingletonMeta` class in `app/meta/singleton_meta.py` is a metaclass that can be used to ensure that only one instance of a class is created. To use it, you can inherit from the `SingletonMeta` class in your class definition. E.g ...

```python

from app.meta.singleton_meta import SingletonMeta

class MyClass(metaclass=SingletonMeta):
    def __init__(self):
        pass
```
