# 🎥 YouTube Video Uploader

A Python automation tool that lets you upload all videos from a local folder directly to your YouTube channel using the **YouTube Data API v3**.

---

## ✨ Features

- Uploads all `.mp4`, `.mov`, `.avi`, and `.mkv` files from the `video/` folder  
- Automatically uses filenames as video titles  
- Sets a default description and privacy status  
- Authenticates securely with OAuth2  
- Easy setup and minimal configuration required  

---

## 🧰 Requirements

- **Python** 3.7 or higher  
- **Google Cloud Project** with YouTube Data API v3 enabled  
- `client_secret.json` file (OAuth credentials)  
- Required Python packages:

pip install google-api-python-client google-auth-oauthlib google-auth-httplib2

text

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/your-username/YouTube-Video-Uploader.git
cd YouTube-Video-Uploader

text

### 2. Enable the YouTube Data API

1. Go to [Google Cloud Console](https://console.developers.google.com/).  
2. Create a new project (or use an existing one).  
3. Enable **YouTube Data API v3** from the API Library.  
4. Navigate to **Credentials → Create Credentials → OAuth Client ID → Desktop App**.  
5. Download the `client_secret.json` file and place it in the project root.

### 3. Add Your Videos

Create a folder named `video/` (if it doesn't already exist) and place your video files inside.  
Example: `video/my_vlog.mp4`

### 4. Run the Script

python upload_youtube.py

text

On first run, a browser window will open for you to sign into your YouTube account.  
After authorization, videos in the `video/` folder will upload automatically.

---

## 🧩 How It Works

1. Authenticates the user with OAuth2.  
2. Scans the `./video` folder for video files.  
3. Uploads each video to YouTube using:
   - **Title:** filename  
   - **Description:** "Uploaded with Python: [filename]"  
   - **Privacy:** private (default)  
4. Prints the YouTube video ID upon successful upload.

---

## 🛠️ Customization

You can customize upload settings by editing the `upload_video()` function in your code:

upload_video(youtube, file_path, title, description, category_id='22', privacy_status='private')

text

- Change `privacy_status` to `"public"` or `"unlisted"`.  
- Use different `category_id` values for various YouTube categories (default is **22 – People & Blogs**).

---

## ⚠️ Notes

- YouTube API quotas limit how many videos you can upload per day.  
- Keep your OAuth credentials private.  
- Always comply with YouTube’s API Terms of Service.  

---

## 🧠 References

- [YouTube Data API Python Quickstart](https://developers.google.com/youtube/v3/quickstart/python)  
- [YouTube Data API Code Samples](https://developers.google.com/youtube/v3/code_samples)  
- [GitHub Markdown Formatting Guide](https://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)  

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 💡 Author

Created by **[Your Name]**  
Feel free to fork this repo, open issues, or contribute!
