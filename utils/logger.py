# utils/logger.py
"""
Simple logging utility that writes to a rotating log file and stdout.
Keeps interface minimal for easy import across modules.
"""
import logging
import logging.handlers
import os

LOG_DIR = os.path.abspath(os.path.join(os.getcwd(), "logs"))
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "thermal_conversion.log")

def get_logger(name="thermal_conversion"):
    """
    Returns a configured logger instance.
    """
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)
    # File handler (rotating)
    fh = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=2*1024*1024, backupCount=3, encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
