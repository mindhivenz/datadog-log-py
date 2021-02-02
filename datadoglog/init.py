import logging
import sys

from .formatter import DatadogFormatter


def init_logging():
    log_handler = logging.StreamHandler(sys.stdout)
    log_handler.setFormatter(DatadogFormatter())
    logging.getLogger().addHandler(log_handler)
