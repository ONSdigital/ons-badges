from pathlib import Path
from pydantic_settings import BaseSettings

from app.loggy import Loggy
from app.singleton import SingletonMeta

PROJECT_ROOT = Path(__file__).parent.parent


class Environment(BaseSettings):
    """
    We use this class to define the environment variables
    and fetch them from the .env file.
    """

    # Put other environment variables here ...
    # E.g project_id: str = Field(validation_alias="PROJECT_ID")
    class Config:
        env_file = (
            PROJECT_ROOT / ".env"
        )  # Ensure path always points to the root of the project


class AppSettings(metaclass=SingletonMeta):
    """
    This class is used to store the settings of the application
    and provide a way to access them
    In here we can store static config and also environment variables
    """

    def __init__(self, env_settings: Environment):
        """
        :param env_settings: The instance of the Environment class to allow
        access to the environment variables.
        """
        self._env_settings = env_settings

        # Allow project root to be accessed directly
        self.project_root = PROJECT_ROOT
        self.static_dir = PROJECT_ROOT / "app" / "static"
        self.ui_enabled = False

    def get_env_table(self) -> str:
        """
        Get a formatted table of the environment variables
        """
        table = [[key, value] for key, value in self._env_settings.model_dump().items()]
        return Loggy.format_table("Environment variables", ["Key", "Value"], table)


# Load settings
SETTINGS = AppSettings(Environment())
