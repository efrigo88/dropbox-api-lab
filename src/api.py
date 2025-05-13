import dropbox
import os
from typing import Optional
from dropbox.files import FileMetadata


class DropboxAPI:
    """A class to handle Dropbox file operations.

    This class provides methods to interact with Dropbox API for listing directories
    and downloading files.
    """

    def __init__(
        self,
        access_token: str,
        dropbox_base_folder: str,
        dropbox_filepath: str,
        local_path: str,
    ) -> None:
        """Initialize the DropboxAPI with authentication and paths.

        Args:
            access_token: Dropbox API access token
            dropbox_base_folder: Base folder in Dropbox
            dropbox_filepath: Path to the file in Dropbox
            local_path: Local path where the file will be saved
        """
        self.dbx = dropbox.Dropbox(access_token)
        self.dropbox_base_folder = dropbox_base_folder
        self.dropbox_filepath = dropbox_filepath
        self.local_path = local_path
        self.account = self.dbx.users_get_current_account()
        print(
            f"Successfully connected to Dropbox account: {self.account.name.display_name}"
        )

    def list_root_directory(self) -> None:
        """List all files and folders in the Dropbox root directory."""
        result = self.dbx.files_list_folder("")
        if not result.entries:
            print("No files or folders found in root directory")
        else:
            print("Files in root directory:")
            for entry in result.entries:
                print(
                    f"- {entry.name} ({'folder' if isinstance(entry, dropbox.files.FolderMetadata) else 'file'})"
                )

    def list_base_folder(self) -> None:
        """List all files and folders in the transcript directory."""
        result = self.dbx.files_list_folder(self.dropbox_base_folder)
        if not result.entries:
            print("No files found in base folder")
        else:
            print("Files in base folder:")
            for entry in result.entries:
                print(
                    f"- {entry.name} ({'folder' if isinstance(entry, dropbox.files.FolderMetadata) else 'file'})"
                )

    def get_file_metadata(self) -> Optional[FileMetadata]:
        """Get metadata for the specified file in Dropbox.

        Returns:
            FileMetadata object if successful, None otherwise
        """
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
                    f"Warning: Downloaded file size ({downloaded_size} bytes) doesn't match Dropbox file size ({metadata.size} bytes)"
                )
            else:
                print(f"\nDownload completed successfully: {self.local_path}")

        except dropbox.exceptions.ApiError as e:
            print(f"\nError downloading file: {e}")
            if e.error.is_path() and e.error.get_path().is_not_found():
                print(f"The file was not found at path: {self.dropbox_filepath}")
                print("Please verify the file path and try again.")
        except Exception as e:
            print(f"\nUnexpected error: {e}")
