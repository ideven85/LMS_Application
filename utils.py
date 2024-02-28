import os
import time
from hashlib import pbkdf2_hmac
from os import urandom
from pathlib import Path

from dotenv import load_dotenv
BASE_DIR = Path(__file__).resolve()
env = os.environ.get
secret=load_dotenv(BASE_DIR / '.env')
SECRET_KEY = env("DJANGO_SECRET_KEY", "secret")

salt = urandom(16)
key = pbkdf2_hmac('sha1',
                    SECRET_KEY.encode('utf-8'),
                  salt,
                  12345,
                  32)

