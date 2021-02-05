import logging
import sys

from .formatter import DatadogFormatter


def init_logging(replace_existing_handlers=False):
    log_handler = logging.StreamHandler(sys.stdout)
    log_handler.setFormatter(DatadogFormatter())
    root_logger = logging.getLogger()
    if replace_existing_handlers:
        for handler in root_logger.handlers:
            root_logger.removeHandler(handler)
    root_logger.addHandler(log_handler)
