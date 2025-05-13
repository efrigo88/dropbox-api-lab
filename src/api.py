import os
from typing import Optional

import dropbox
from dropbox.files import FileMetadata

from src.constants import APP_KEY, APP_SECRET, REFRESH_TOKEN


class DropboxAPI:
    def __init__(
        self,
        base_folder: str,
        dropbox_filepath: str,
        local_path: str,
    ) -> None:
        """Initialize the DropboxAPI with authentication and paths.

        Args:
            base_folder: Base folder in Dropbox
            dropbox_filepath: Path to the file in Dropbox
            local_path: Local path where the file will be saved
        """
        self.base_folder = base_folder
        self.dropbox_filepath = dropbox_filepath
        self.local_path = local_path

        try:
            # Initialize Dropbox client with OAuth2 refresh token
            self.dbx = dropbox.Dropbox(
                app_key=APP_KEY,
                app_secret=APP_SECRET,
                oauth2_refresh_token=REFRESH_TOKEN,
            )

            # Test the connection
            self.account = self.dbx.users_get_current_account()
            print(
                f"Successfully connected to Dropbox account: "
                f"{self.account.name.display_name}"
            )
        except dropbox.exceptions.AuthError as e:
            print(f"Authentication error: {e}")
            raise
        except Exception as e:
            print(f"Error connecting to Dropbox: {e}")
            raise

    def list_root_directory(self) -> None:
        """List all files and folders in the Dropbox root directory."""
        result = self.dbx.files_list_folder("")
        if not result.entries:
            print("No files or folders found in root directory")
        else:
            print("Files in root directory:")
            for entry in result.entries:
                entry_type = (
                    "folder"
                    if isinstance(entry, dropbox.files.FolderMetadata)
                    else "file"
                )
                print(f"- {entry.name} ({entry_type})")

    def list_base_folder(self) -> None:
        """List all files and folders in the transcript directory."""
        result = self.dbx.files_list_folder(self.base_folder)
        if not result.entries:
            print("No files found in base folder")
        else:
            print("Files in base folder:")
            for entry in result.entries:
                entry_type = (
                    "folder"
                    if isinstance(entry, dropbox.files.FolderMetadata)
                    else "file"
                )
                print(f"- {entry.name} ({entry_type})")

    def get_file_metadata(self) -> Optional[FileMetadata]:
        """Get metadata for the specified file in Dropbox."""
        metadata = self.dbx.files_get_metadata(self.dropbox_filepath)
        if not isinstance(metadata, dropbox.files.FileMetadata):
            print(f"Error: {self.dropbox_filepath} is not a file")
            return None
        print(f"\nFile size in Dropbox: {metadata.size} bytes")

        if metadata.size == 0:
            print("Warning: File in Dropbox is empty (0 bytes)")
            return None
        return metadata

    def download_file(self) -> None:
        """Download the specified file from Dropbox to local storage."""
        metadata = self.get_file_metadata()
        if not metadata:
            return

        try:
            with open(self.local_path, "wb") as f:
                _, res = self.dbx.files_download(path=self.dropbox_filepath)
                f.write(res.content)

            downloaded_size = os.path.getsize(self.local_path)
            print(f"Downloaded file size: {downloaded_size} bytes")

            if downloaded_size == 0:
                print("Error: Downloaded file is empty")
            elif downloaded_size != metadata.size:
                print(
                    f"Warning: Downloaded file size ({downloaded_size} bytes) "
                    f"doesn't match Dropbox file size ({metadata.size} bytes)"
                )
            else:
                print(f"\nDownload completed successfully: {self.local_path}")

        except dropbox.exceptions.ApiError as e:
            print(f"\nError downloading file: {e}")
            if e.error.is_path() and e.error.get_path().is_not_found():
                print(
                    f"The file was not found at path: {self.dropbox_filepath}"
                )
                print("Please verify the file path and try again.")
        except dropbox.exceptions.AuthError as e:
            print(f"\nAuthentication error: {e}")
        except OSError as e:
            print(f"\nFile system error: {e}")
