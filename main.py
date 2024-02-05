import tkinter
import customtkinter
from pytube import YouTube


def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        title.configure(text=yt_object.title, text_color="white")

        finish_label.configure(text="")
        video.download()
        finish_label.configure(text="Download complete!")
    except:
        finish_label.configure(text="Download Error", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progress_percentage.configure(text=per + '%')
    progress_percentage.update()

    # Update Progress 
    progress_bar.update(float(percentage_of_completion) / 100)

# Sytem Settings
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# App Frame
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("720x480")
app.title("Youtube Video Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a Youtube link")
title.pack(padx=10, pady=10)

# Link Input 
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Download 
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

# Progress Percentage 
progress_percentage = customtkinter.CTkLabel(app, text="0%")
progress_percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Download Button 
download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)

# Run App 
app.mainloop()