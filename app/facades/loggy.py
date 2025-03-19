import logging

from tabulate import tabulate


class Loggy:
    """
    A facade for logging operations, providing a consistent interface for logging messages
    Note: we use stacklevel=2 to ensure the correct file and line number are logged, otherwise the log will point to the
    LogFacade method that called the logger method.
    """

    _loggers = {
        "application": logging.getLogger(__name__),
        "uvicorn": logging.getLogger("uvicorn"),
    }

    @staticmethod
    def disable_logging():
        """
        Disable all logging below CRITICAL level.
        """
        Loggy.configure_logger(level=logging.CRITICAL, null_handler=True)

    @staticmethod
    def configure_logger(level=logging.INFO, null_handler=False):
        """
        Set up a basic logging configuration with a consistent format and default level.
        """

        if null_handler:
            # Set a null handler to prevent any logging from being output
            null_logger = logging.getLogger()
            null_logger.setLevel(logging.CRITICAL)
            null_logger.addHandler(logging.NullHandler())
            return

        # Set up a formatter
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S",
        )

        # Set up a handler for the application logger
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        # Set the level and add the handler to the application logger
        app_logger = Loggy._loggers["application"]
        app_logger.setLevel(level)
        app_logger.addHandler(handler)

    @staticmethod
    def info(message: any, logger: str = "application"):
        """Log an INFO level message."""
        Loggy._get_logger(logger).info(message, stacklevel=2)

    @staticmethod
    def log(level, message: any, logger: str = "application"):
        """Log an INFO level message."""
        Loggy._get_logger(logger).log(level, message, stacklevel=2)

    @staticmethod
    def warning(message: any, logger: str = "application"):
        """Log a WARNING level message."""
        Loggy._get_logger(logger).warning(message, stacklevel=2)

    @staticmethod
    def error(message: any, logger: str = "application"):
        """Log an ERROR level message."""
        Loggy._get_logger(logger).error(message, stacklevel=2)

    @staticmethod
    def debug(message: any, logger: str = "application"):
        """Log a DEBUG level message."""
        Loggy._get_logger(logger).debug(message, stacklevel=2)

    @staticmethod
    def critical(message: any, logger: str = "application"):
        """Log a CRITICAL level message."""
        Loggy._get_logger(logger).critical(message, stacklevel=2)

    @staticmethod
    def _get_logger(logger_name: str) -> logging.Logger:
        """
        Retrieve a logger by name.

        Args:
            logger_name (str): The name of the logger (e.g., 'application', 'uvicorn').

        Returns:
            logging.Logger: The logger instance.

        Raises:
            KeyError: If the logger name is invalid.
        """
        if logger_name not in Loggy._loggers:
            raise KeyError(
                f"Logger '{logger_name}' not found. Available loggers: {list(Loggy._loggers.keys())}"
            )
        return Loggy._loggers[logger_name]

    @staticmethod
    def log_table(level, title: str, headers: list[str], table: list[list[str]]):
        # Format the table
        table_with_title = Loggy.format_table(title, headers, table)

        # Log the table with the specified level
        Loggy.log(level, table_with_title)

    @staticmethod
    def log_table_info(title: str, headers: list[str], table: list[list[str]]):
        Loggy.log_table(logging.INFO, title, headers, table)

    @staticmethod
    def log_table_error(title: str, headers: list[str], table: list[list[str]]):
        Loggy.log_table(logging.ERROR, title, headers, table)

    @staticmethod
    def format_table(title: str, headers: list[str], table: list[list[str]]) -> str:
        formatted_table = tabulate(table, headers=headers, tablefmt="grid")

        # Add a title to the table
        return f"\n\n{title}\n{'=' * len(title)}\n{formatted_table}\n"
