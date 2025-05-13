import os
import dropbox
from dotenv import load_dotenv

load_dotenv()
APP_KEY = os.getenv("DROPBOX_APP_KEY")
APP_SECRET = os.getenv("DROPBOX_APP_SECRET")


def main():
    # Create OAuth2 flow
    auth_flow = dropbox.DropboxOAuth2FlowNoRedirect(
        APP_KEY, consumer_secret=APP_SECRET, token_access_type="offline"
    )

    # Get the authorization URL
    authorize_url = auth_flow.start()
    print("1. Go to: " + authorize_url)
    print("2. Click 'Allow' (you might have to log in first)")
    print("3. Copy the authorization code")
    auth_code = input("Enter the authorization code here: ").strip()

    try:
        oauth_result = auth_flow.finish(auth_code)
        print(f"DROPBOX_REFRESH_TOKEN={oauth_result.refresh_token}")
        print(f"DROPBOX_ACCESS_TOKEN={oauth_result.access_token}")

    except dropbox.exceptions.AuthError as e:
        print(f"Authentication error: {e}")
    except dropbox.exceptions.BadInputError as e:
        print(f"Invalid authorization code: {e}")
    except dropbox.exceptions.ApiError as e:
        print(f"API error: {e}")


if __name__ == "__main__":
    main()
