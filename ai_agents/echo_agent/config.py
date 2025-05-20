# echo_agent/config.py

import os

from dotenv import load_dotenv

load_dotenv()  # Load variables from the .env file if present.

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError(
        "OPEN_API_KEY not found. Please set it in your .env file or environment variables."
    )
