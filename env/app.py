import customtkinter as ctk
from tkinter import Tk

def download_video():
    print("clicked")

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

root.mainloop()
