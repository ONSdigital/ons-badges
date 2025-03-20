import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from app.config import SETTINGS
from app.loggy import Loggy
from app.routes.main import router
from app.routes.api import api_router


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Defines the lifespan of a FastAPI application,
    we can use this to run code on startup and shutdown.
    :param _app: The instance of the FastAPI application.
    """

    # Configure logging
    Loggy.configure_logger()

    Loggy.info("Starting ons-badges", logger="uvicorn")

    # Log all the config settings
    Loggy.info(SETTINGS.get_env_table())

    # Check the static directory exists
    if os.path.isdir(SETTINGS.static_dir):
        # Check if index.html exists
        if os.path.exists(os.path.join(SETTINGS.static_dir, "index.html")):
            Loggy.info("Loaded frontend successfully!", logger="uvicorn")
            # Serve frontends static files
            app.mount("/static", StaticFiles(directory="app/static"), name="static")
            SETTINGS.ui_enabled = True
        else:
            Loggy.warning(
                "No index.html found, frontend will not be served", logger="uvicorn"
            )
    else:
        Loggy.warning(
            "No static directory found, frontend will not be served", logger="uvicorn"
        )

    # Run the app
    yield

    Loggy.info("Shutting down ons-badges", logger="uvicorn")


app = FastAPI(title="ons-badges", lifespan=lifespan)

app.include_router(router)
app.include_router(api_router)


def run():
    """
    Run the FastAPI app
    this is a function so it can be called externally
    by poetry etc
    """
    uvicorn.run(app, host="0.0.0.0", port=5005)


if __name__ == "__main__":
    run()
