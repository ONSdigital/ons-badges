import requests
import toml
from urllib.parse import urlparse
from app.exceptions import RepositoryException


def fetch_raw_content(url: str, file_path: str) -> str:
    """
    Fetch raw content from a specific file in a GitHub repository.

    :param url: The URL of the repository (GitHub).
    :param file_path: The path of the file to fetch within the repository (e.g., 'pyproject.toml').
    :return: The raw content of the file as a string.
    """
    # Parse the repository owner and name from the URL
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip("/").split("/")

    if len(path_parts) < 2:
        raise RepositoryException("Invalid repository URL")

    owner, repo = path_parts[:2]

    # Ensure that the owner is on the allowed list
    if owner.lower() not in ["onsdigital"]:
        raise RepositoryException("Unauthorized repository owner")

    # GitHub API URL to fetch the raw content of the specified file
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    headers = {"Accept": "application/vnd.github.v3.raw"}  # Request raw content

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.text
    elif response.status_code == 404:
        raise RepositoryException(f"File '{file_path}' not found in the repository")
    else:
        raise RepositoryException(
            f"Error fetching file '{file_path}', error code: {response.status_code}"
        )


def get_repo_version(url: str) -> str:
    """
    Return the version of a repository using the poetry pyproject.toml file.

    :param url: The URL of the repository (GitHub)
    :return: str - The version of the repository, or an error message
    """
    # Fetch the raw content of the pyproject.toml file
    raw_content = fetch_raw_content(url, "pyproject.toml")

    try:
        pyproject_data = toml.loads(raw_content)
        return pyproject_data["tool"]["poetry"]["version"]
    except (KeyError, toml.TomlDecodeError):
        raise RepositoryException(
            "Error parsing pyproject.toml file or version not found"
        )


def get_repo_python_version(url: str) -> str:
    """
    Return the Python version of a repository using the poetry pyproject.toml file.

    :param url: The URL of the repository (GitHub)
    :return: str - The Python version of the repository, or an error message
    """
    # Fetch the raw content of the pyproject.toml file
    raw_content = fetch_raw_content(url, "pyproject.toml")

    try:
        pyproject_data = toml.loads(raw_content)
        python_version = pyproject_data["tool"]["poetry"]["dependencies"]["python"]
        # Remove the caret from the version
        return python_version.replace("^", "")
    except (KeyError, toml.TomlDecodeError):
        raise RepositoryException(
            "Error parsing pyproject.toml file or Python version not found"
        )
