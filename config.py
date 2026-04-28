import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY in .env")
if not DATABASE_URL:
    raise ValueError("Missing DATABASE_URL in .env")