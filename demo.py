import os
from dotenv import load_dotenv

# Load variables from .env into environment
load_dotenv()

mongodb_url = os.getenv("MONGODB_URL")
print(mongodb_url)
