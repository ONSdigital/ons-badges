from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings

from app.facades.loggy import Loggy
from app.meta.singleton_meta import SingletonMeta

PROJECT_ROOT = Path(__file__).parent.parent


class Environment(BaseSettings):
    """
    We use this class to define the environment variables
    and fetch them from the .env file.
    """

    # This will automatically fetch the value of the PROJECT_ID environment variable
    project_id: str = Field(validation_alias="PROJECT_ID")

    # Put other environment variables here ...

    class Config:
        env_file = PROJECT_ROOT / ".env"  # Ensure path always points to the root of the project


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

        # Allow project ID to be accessed directly
        self.project_id = env_settings.project_id

    def get_env_table(self) -> str:
        """
        Get a formatted table of the environment variables
        """
        table = [[key, value] for key, value in self._env_settings.model_dump().items()]
        return Loggy.format_table("Environment variables", ["Key", "Value"], table)


# Load settings
SETTINGS = AppSettings(Environment())
