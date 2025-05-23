import os
from dotenv import load_dotenv

load_dotenv()
# Get Redis credentials from environment variables
REDIS_USER = os.getenv('REDIS_USER', '')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD','')
REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.getenv('REDIS_PORT', '6379')
# Construct Redis URL with authentication
REDIS_URL = f"redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0"
class Settings:
    # Construct Redis URL with authentication
    REDIS_URL = f"redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0"

settings = Settings()