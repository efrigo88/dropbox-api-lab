# Dropbox API Lab

This project provides a simple interface to interact with Dropbox using the Dropbox API. It allows you to list files and folders in your Dropbox and download files to your local machine.

## Features

- List files and folders in your Dropbox root or a specific folder
- Download files from Dropbox to your local system

## Setup

1. Clone this repository.
2. Install dependencies using uv (install this app first) and then:
   ```bash
   uv pip install . && uv pip install ".[dev]"
   ```
3. Create a `.env` file in the root directory and add your Dropbox API access token:
   ```env
   ACCESS_TOKEN=your_dropbox_access_token
   ```

## Configuration

- The Dropbox folder and file paths are set in `src/constants.py`.
- The downloaded file will be saved to `data/transcript.pdf` by default.

## Usage

You can use the `DropboxAPI` class in `src/api.py` to interact with Dropbox. Example usage:

```python
from src.api import DropboxAPI
from src.constants import ACCESS_TOKEN, BASE_DROPBOX_FOLDER, DROPBOX_FILEPATH, LOCAL_PATH

dbx_api = DropboxAPI(
    access_token=ACCESS_TOKEN,
    dropbox_base_folder=BASE_DROPBOX_FOLDER,
    dropbox_filepath=DROPBOX_FILEPATH,
    local_path=LOCAL_PATH,
)
dbx_api.list_root_directory()
dbx_api.list_base_folder()
dbx_api.download_file()
```

To run the project, execute:

```bash
python src/main.py
```

## License

MIT
