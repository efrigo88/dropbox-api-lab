# Dropbox Transcript Downloader

A Python application to download transcripts from Dropbox using the Dropbox API. This tool helps you:

- Securely connect to your Dropbox account using OAuth2 authentication
- Browse and list files in your Dropbox account
- Specifically target and download transcript files from a designated directory
- Store downloaded transcripts locally in a structured format
- Handle large files efficiently with proper error handling and progress tracking

The application is designed to be run either locally or in a Docker container, making it flexible for different deployment scenarios. It uses environment variables for secure credential management and supports both development and production environments.

## Setup

1. Create a Dropbox app in the [Dropbox Developer Console](https://www.dropbox.com/developers/apps)
2. Get your app key and secret from the app settings
3. Create a `.env` file in the project root with your credentials:
   ```
   DROPBOX_APP_KEY=your_app_key_here
   DROPBOX_APP_SECRET=your_app_secret_here
   ```

## Installation

### Local Development

1. Install uv (Python package installer):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Create and activate a virtual environment:

   ```bash
   uv venv
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

### Docker (Recommended)

Build the Docker image:

```bash
docker build -t api-lab .
```

## Authentication

The application uses OAuth2 with refresh tokens for authentication. To get your refresh token:

1. Run the token generation script:
   ```bash
   python src/get_refresh_token.py
   ```
2. Follow the prompts to authorize your app
3. Copy the refresh token and add it to your `.env` file:
   ```
   DROPBOX_REFRESH_TOKEN=your_refresh_token_here
   ```

## Usage

### Local Development

Run the main script:

```bash
python src/main.py
```

### Docker

Run the container with a volume mount for data persistence:

```bash
docker run -v $(pwd)/data:/app/data api-lab
```

Remember to stop and remove the containers after you finish.

The script will:

1. Connect to your Dropbox account
2. List files in the root directory
3. List files in the transcript directory
4. Download the specified transcript file

## Development

Run linters:

```bash
pylint src/
black src/
isort src/
```

## License

MIT
