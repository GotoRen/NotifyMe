import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# LINE Notify Token
TOKEN = os.environ.get("TOKEN")
# LINE Notify API
API = os.environ.get("API")
