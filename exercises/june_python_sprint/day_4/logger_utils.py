import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:  # Avoid adding multiple handlers

        # --- Formatter ---
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # --- Console Handler ---
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        # --- File Handler with Date and Rotation ---
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        today_str = datetime.now().strftime("%Y-%m-%d")
        log_file = os.path.join(log_dir, f"{name}_{today_str}.log")

        fh = RotatingFileHandler(
            log_file,
            mode="a",
            maxBytes=1_000_000,  # Rotate at ~1MB
            backupCount=3,  # Keep 3 old log files
            encoding="utf-8",
        )
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


# Use it:
# logger = get_logger()
# logger.info("Python is behaving again ✅")
