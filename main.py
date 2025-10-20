import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
VIDEO_DIR = './video'
def get_youtube_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json', SCOPES)
    credentials = flow.run_local_server(port=0)
    return build('youtube', 'v3', credentials=credentials)

def upload_video(youtube, file_path, title, description, category_id='22', privacy_status='private'):
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
