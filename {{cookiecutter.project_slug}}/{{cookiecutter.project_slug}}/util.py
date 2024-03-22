import logging
from pathlib import Path
from typing import  Dict, Union
from box import Box
from {{ cookiecutter.project_slug }}.project import Project




def load_config(config_file: Union[str, Path]) -> Box:
    """
    Load the config from the specified yaml file

    :param config_file: path of the config file to load
    :return: the parsed config as dictionary
    """
    return Box.from_yaml(filename=config_file)



def load_default_config() -> Box:
    """
    Load the default config from the package

    :return: the parsed default config as a `Box`
    """
    return Box.from_yaml(filename=Project.main_config_file)

def logging_setup(config: Dict, logger: logging.Logger):
    """
    setup logging based on the configuration

    :param config: the parsed config tree
    :param logger: the logger to set up
    """
    log_conf = config["logging"]
    fmt = log_conf["format"]
    if not log_conf["enabled"]:
        logger.handlers = []
        logger.setLevel(logging.NOTSET)
        return logger
    new_level = log_conf["level"].upper()
    logger.setLevel(new_level)


    console_handler = logging.StreamHandler()
    console_handler.setLevel(new_level)
    console_handler.setFormatter(logging.Formatter(fmt))
    logger.addHandler(console_handler)
    if not log_conf["enabled"]:
        filehdlr = logging.FileHandler(Project.log_dir / f"{logger.name}.log")
        console_handler.setFormatter(logging.Formatter(fmt))
        logger.addHandler(filehdlr)
    return logger




def get_logger(
    name: str = "{{ cookiecutter.project_slug }}", log_to_file: bool = False
) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers == 2 and log_to_file:
        return logger

    if len(logger.handlers) == 1 and not log_to_file:
        return logger

    config = load_config(Project.main_config_file)
    logging_setup(config, logger)
    return logger
