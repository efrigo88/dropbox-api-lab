from api import DropboxAPI
from constants import (
    ACCESS_TOKEN,
    BASE_DROPBOX_FOLDER,
    DROPBOX_FILEPATH,
    LOCAL_PATH,
)


def main():
    dbx = DropboxAPI(
        ACCESS_TOKEN, BASE_DROPBOX_FOLDER, DROPBOX_FILEPATH, LOCAL_PATH
    )
    dbx.list_root_directory()
    dbx.list_base_folder()
    dbx.download_file()


if __name__ == "__main__":
    main()
