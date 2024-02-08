from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import os
import requests

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        video_title = yt.title
        highest_res_stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        
        with open(save_path, 'wb') as f, requests.get(highest_res_stream.url, stream=True) as response:
            total_size = int(response.headers.get('content-length', 0))
            bytes_received = 0

            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    bytes_received += len(chunk)
                    progress = (bytes_received / total_size) * 100
                    print(f"\rDownloading... {progress:.2f}%", end='', flush=True)

        print(f"\nVideo '{video_title}' downloaded successfully.")

    except Exception as e:
        print(e)

def open_file_dialog():
    return filedialog.askdirectory()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        save_path = os.path.join(save_dir, f"{YouTube(video_url).title}.mp4")
        print("Video is downloading...")
        download_video(video_url, save_path)
    else:
        print("Invalid save location.")
