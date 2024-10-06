import yt_dlp
from tqdm import tqdm
import os

# Specify the path to FFmpeg executable
ffmpeg_path = r'C:\ffmpeg\bin\ffmpeg.exe'  # Replace with actual path

def download_video(url):
    ydl_opts = {
        'ffmpeg_location': ffmpeg_path,
        'outtmpl': r'C:\Users\ASUS\Documents\Python\youtube video downloader\videos\%(title)s.%(ext)s',
        'progress_hooks': [on_progress],
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            if 'entries' in info:
                # This is a playlist, so download all videos
                for entry in info['entries']:
                    ydl.download([entry['url']])
            else:
                # Download the video
                ydl.download([url])
        
        print(f"\nDownload completed for {url}")
    except Exception as e:
        print(f"\nError downloading {url}: {str(e)}")

def on_progress(d):
    if d['status'] == 'downloading':
        print(f"\rDownloading: [{d['_percent_str']}]", end='')
    elif d['status'] == 'finished':
        print("\nDownload completed!")

# Read URLs from file
with open(r'C:\Users\ASUS\Documents\Python\youtube video downloader\L.txt', 'r') as file:
    urls = file.readlines()

# Download videos
for url in tqdm(urls):
    url = url.strip()
    download_video(url)

print("\nAll downloads completed.")
