import os
from dotenv import load_dotenv

load_dotenv()

APP_KEY = os.getenv("DROPBOX_APP_KEY")
APP_SECRET = os.getenv("DROPBOX_APP_SECRET")
REFRESH_TOKEN = os.getenv("DROPBOX_REFRESH_TOKEN")

BASE_DROPBOX_FOLDER = "/transcript"
DROPBOX_FILEPATH = f"{BASE_DROPBOX_FOLDER}/transcript.pdf"
LOCAL_PATH = "data/transcript.pdf"
