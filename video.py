import tkinter as tk
from PIL import Image, ImageTk
from moviepy.editor import VideoFileClip

def play_video(video_path):
    # Load video
    video = VideoFileClip(video_path)
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    video_label = tk.Label(root)
    video_label.pack(expand=True, fill=tk.BOTH)
    video.preview()
    root.destroy()
