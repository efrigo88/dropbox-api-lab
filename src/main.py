from src.api import DropboxAPI
from src.constants import (
    BASE_DROPBOX_FOLDER,
    DROPBOX_FILEPATH,
    LOCAL_PATH,
)


def main():
    dbx = DropboxAPI(
        base_folder=BASE_DROPBOX_FOLDER,
        dropbox_filepath=DROPBOX_FILEPATH,
        local_path=LOCAL_PATH,
    )
    dbx.list_root_directory()
    dbx.list_base_folder()
    dbx.download_file()


if __name__ == "__main__":
    main()
