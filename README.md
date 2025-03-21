
![Logo](logo.png)

# ons-badges

![Version](https://ons-badges-290227325370.europe-west2.run.app/api/badge/repo/version?url=https://github.com/ONSdigital/ons-badges) ![Python](https://ons-badges-290227325370.europe-west2.run.app/api/badge/repo/python-version?url=https://github.com/ONSdigital/ons-badges) 

A very simple fastapi service to generate badges for use in GitHub repositories.

## Playground

Visit the playground to generate badges online ...

[https://ons-badges-290227325370.europe-west2.run.app/](https://ons-badges-290227325370.europe-west2.run.app/)

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

### Building the frontend (optional)

To build the optional homepage frontend, run the following command:

```bash
cd frontend
npm install
npm run build
```

### Running the service

```bash
poetry run dev
```

## Working with the frontend

If you wish to develop and work on the frontend, you can run the following command to start the frontend in development mode:

```bash
cd frontend
npm install
npm run dev
```

## Run with Docker

The Dockerfile will build the frontend and backend and run the service on port 5005.

### Build the image

```bash
docker build -t ons-badges .
```

### Run the container

```bash
docker run -p 5005:5005 ons-badges
```

## Formatter

```bash
ruff format
```
## Example use

### Custom Badge

This badge will display two pieces of text, one on the left and one on the right.

`http://127.0.0.1:5005/api/badge/custom?left=hello&right=world`

### Version Badge

This badge will dynamically fetch the version from the `pypoetry.toml` file in a specified repository.

`http://127.0.0.1:5005/api/badge/repo/version?url=https://github.com/ONSdigital/sdx-transformer`

## Configure allowed owners

Currently the repository routes are configured to only allow repositories that are owned by the ONS. To change this, the list of allowed owners in `app/repo.py`. Or modify the code to use Environment Variables which is probably a better idea.

## Add badges to your README

To add a badge to your README, use the following markdown:

```markdown
![Badge](https:YOUR_INSTANCE_URL/api/badge/custom?left=hello&right=world)
```
