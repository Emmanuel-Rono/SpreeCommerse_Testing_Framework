import logging
import os

from rich.logging import RichHandler


def configure_logging(level: str = "INFO") -> None:
    log_level = os.getenv("LOG_LEVEL", level).upper()
    logging.basicConfig(
        level=log_level,
        format="%(message)s",
        datefmt="[%H:%M:%S]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )
