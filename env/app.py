import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
from tkinter import Tk
import os

def download_video():
    url = entry_url.get()
    resolution = resolution_var.get()

    progress_label.pack(pady="10p")
    progress_bar.pack(pady="10p")
    status_label.pack(pady="10p")

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(res=resolution).first()
        file_path = os.path.join("downloads", f"{yt.title}.mp4")

        # Download video to the specified file path
        stream.download(output_path="downloads")

        # Update status label
        status_label.configure(text="Downloaded!", text_color="white", fg_color="green")

    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}", text_color="white", fg_color="red")

def on_progress(stream, chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = bytes_downloaded / total_size *100
    progress_label.configure(text=str(int(percentage_completed)) + "%")
    progress_label.update()
    progress_bar.set(float(percentage_completed / 100))


root = ctk.CTk()
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")

root.title("YouTube Video Downloader")

root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

url_label_text = "Online Video Downloader"
url_label_font = ("Helvetica", 20)
url_label = ctk.CTkLabel(content_frame, text=url_label_text, font=url_label_font)
entry_url = ctk.CTkEntry(content_frame, width=400, placeholder_text="Enter URL here")
url_label.pack(pady=10)
entry_url.pack(pady=10)

download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack()

# Resolution combobox using CTkComboBox
resolutions = ["1080p", "720p", "360p"]
resolution_var = ctk.StringVar()
resolution_combobox = ctk.CTkComboBox(content_frame, values=resolutions, variable=resolution_var)
resolution_combobox.pack(pady="10p")
resolution_combobox.set("720p")  # Set the default resolution

# Label and the progress bar to display the download progress
progress_label = ctk.CTkLabel(content_frame, text="0%")


progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0.6)


status_label = ctk.CTkLabel(content_frame, text="Downloaded")

root.mainloop()
