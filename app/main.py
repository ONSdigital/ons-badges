from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from app.config import SETTINGS
from app.facades.loggy import Loggy
from app.routes import router


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Defines the lifespan of a FastAPI application,
    we can use this to run code on startup and shutdown.
    :param _app: The instance of the FastAPI application.
    """

    # Configure logging
    Loggy.configure_logger()

    Loggy.info("Starting sdx-fastapi-boilerplate", logger="uvicorn")

    # Log all the config settings
    Loggy.info(SETTINGS.get_env_table())

    # Run the app
    yield

    Loggy.info("Shutting down sdx-fastapi-boilerplate", logger="uvicorn")


app = FastAPI(title="sdx-fastapi-boilerplate", lifespan=lifespan)
app.include_router(router)


def run():
    """
    Run the FastAPI app
    this is a function so it can be called externally
    by poetry etc
    """
    uvicorn.run(app, host="0.0.0.0", port=5000)


if __name__ == "__main__":
    run()
