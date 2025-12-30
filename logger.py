"""
Logging setup - writes to bot.log and console.
Helps with debugging when things go wrong.
"""
import logging
import sys
from pathlib import Path


def setup_logger(name: str = "trading_bot") -> logging.Logger:
    """Configure logger to write to file and console."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Don't add handlers twice
    if logger.handlers:
        return logger
    
    # Write to bot.log
    log_file = Path("bot.log")
    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    
    # Also show in console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    
    # Simple format with timestamp
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger


logger = setup_logger()
