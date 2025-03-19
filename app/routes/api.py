from enum import Enum

from fastapi import APIRouter, Response

from app.exceptions import RepositoryException
from app.repo import get_repo_version, get_repo_python_version
from app.svg import generate_svg

api_router = APIRouter(prefix="/api")


class BadgeColour(str, Enum):
    success = "success"
    danger = "danger"
    warning = "warning"
    grey = "grey"
    standard = "standard"


@api_router.get("/badge/standard", response_class=Response)
def get_badge(
    left_text: str,
    right_text: str,
    colour: BadgeColour = BadgeColour.standard,
):
    """
    Generate a standard badge as an SVG with left_text, right_text, and an optional colour.
    Allowed colours: success, danger, warning, grey, standard.
    :param left_text: str - the text to display on the left
    :param right_text: str - the text to display on the right
    :param colour: BadgeColour - the colour of the right section
    :return: SVG badge
    """

    # Choose bg and fg colours based on the colour parameter
    colour_map = {
        BadgeColour.success: ("#0F8243", "#ffffff"),
        BadgeColour.danger: ("#D0021B", "#ffffff"),
        BadgeColour.warning: ("#FA6401", "#000000"),
        BadgeColour.grey: ("#414042", "#ffffff"),
        BadgeColour.standard: ("#013B61", "#ffffff"),
    }

    bg, fg = colour_map[colour]

    svg_content = generate_svg(
        left_text=left_text,
        right_text=right_text,
        bg=bg,
        fg=fg,
    )

    return Response(content=svg_content, media_type="image/svg+xml")


@api_router.get("/repo/version", response_class=Response)
def get_version(
    url: str,
):
    """
    Generate a badge for a repository version.
    :param url:  the url of the repository
    :return: A badge with the version of the repository
    """

    try:
        version = get_repo_version(url)
    except RepositoryException as e:
        return Response(content=str(e), status_code=422)

    svg_content = generate_svg(
        left_text="version",
        right_text=version,
        bg="#013B61",
        fg="#ffffff",
    )

    return Response(content=svg_content, media_type="image/svg+xml")


@api_router.get("/repo/python-version", response_class=Response)
def get_python_version(
    url: str,
):
    """
    Generate a badge for a repository python version.
    :param url:  the url of the repository
    :return: A badge with the python version of the repository
    """

    try:
        version = get_repo_python_version(url)
    except RepositoryException as e:
        return Response(content=str(e), status_code=422)

    svg_content = generate_svg(
        left_text="python",
        right_text=version,
        bg="#013B61",
        fg="#ffffff",
    )

    return Response(content=svg_content, media_type="image/svg+xml")

