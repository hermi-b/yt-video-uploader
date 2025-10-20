import os
import google.auth.exceptions
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
TOKEN_FILE = 'token.json'
VIDEO_DIR = './video'

def get_youtube_service():
    creds = None

    # Load saved credentials if they exist
    if os.path.exists(TOKEN_FILE):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        except google.auth.exceptions.GoogleAuthError:
            creds = None

    # If credentials are invalid or don't exist, authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save credentials for future runs
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    return build('youtube', 'v3', credentials=creds)


def upload_video(youtube, file_path, title, description, category_id='22', privacy_status='public'):
    body=dict(
        snippet=dict(
            title=title,
            description=description,
            categoryId=category_id
        ),
        status=dict(
            privacyStatus=privacy_status
        )
    )
    media = MediaFileUpload(file_path, resumable=True)
    request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=media
    )
    response = request.execute()
    print(f"Uploaded: {file_path}, Video ID: {response['id']}")

if __name__ == '__main__':
    youtube = get_youtube_service()
    for filename in os.listdir(VIDEO_DIR):
        if filename.endswith((".mp4", ".mov", ".avi", ".mkv")):
            title = os.path.splitext(filename)[0]
            desc = f"Uploaded with Python: {title}"
            file_path = os.path.join(VIDEO_DIR, filename)
            upload_video(youtube, file_path, title, desc)
