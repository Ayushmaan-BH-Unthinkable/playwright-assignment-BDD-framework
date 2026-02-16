import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com")
USERNAME_ADMIN = os.getenv("USERNAME_ADMIN")
PASSWORD_ADMIN = os.getenv("PASSWORD_ADMIN")

USERNAME_ESS_USER = os.getenv("USERNAME_ESS_USER")
PASSWORD_ESS_USER = os.getenv("PASSWORD_ESS_USER")
