# Python stdlib
import logging


# Project Dependencies


# Project Imports
from {{ cookiecutter.project_slug }}.project import Project



def get_logger(
    name: str = "{{ cookiecutter.project_slug }}.log", log_to_file: bool = False
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.propagate = False
    # clear handlers if they exist
    logger.handlers = []
    if len(logger.handlers) == 0 or (log_to_file and len(logger.handlers) == 1):
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] (%(module)s:%(lineno)d): %(message)s",
            datefmt="%a, %Y-%m-%d %I:%M:%S %p",
        )
        # Create console handler and set the formatter
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # If log_to_file is True, add a file handler
        if log_to_file:
            file_handler = logging.FileHandler(Project.log_dir / f"{name}")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    logger.setLevel(logging.INFO)
    return logger
