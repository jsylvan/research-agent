"""
logging_utils.py

Configure advanced logging for your multi-agent system, hooking into metagpt.logs
"""
import logging
from metagpt.logs import logger as metagpt_logger

def configure_logging(level=logging.INFO):
    logging.basicConfig(
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=level
    )
    metagpt_logger.setLevel(level)
