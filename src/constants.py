import os
from dotenv import load_dotenv

load_dotenv()  # get access token from .env file
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
BASE_DROPBOX_FOLDER = "/transcript"
DROPBOX_FILEPATH = f"{BASE_DROPBOX_FOLDER}/transcript.pdf"
LOCAL_PATH = "dropbox_api_req/transcript.pdf"
