import tkinter as tk
from tkinter.ttk import Progressbar
import pytube
from PIL import ImageTk, Image
from io import BytesIO
import urllib.request


class Window:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("1000x800")
        self.root.title("Youtube Downloader")
        self.stream = pytube.Stream

        img = None

        title_label = tk.Label(self.root, font="Arial, 20", foreground="black", text="Youtube Downloader")
        title_label.grid(column=0, row=0)

        url_text = tk.Entry(self.root, font="Arial,14", disabledbackground="", width=30)
        url_text.grid(column=0, row=1)

        # declaring file name for the download
        file_namer = self.stream.default_filename

        all_res_options = ["720p", "480p", "360p", "240p", "144p"]
        streams_list = []

        value = tk.StringVar(self.root)
        value.set(" ")

        canvas = tk.Canvas(height=300, width=300, bg="grey", image=img)
        canvas.grid(column=0, row=3)

        def url_read():
            global img
            yt_url = url_text.get()
            yt = pytube.YouTube(yt_url)

            title = yt.title
            video_title = tk.Label(self.root, font="Arial,14", text=title, wraplength=400)
            video_title.grid(column=0, row=2)

            thumbnail_link = urllib.request.urlopen(yt.thumbnail_url).read()
            html = BytesIO(thumbnail_link)
            converted_thumbnail = Image.open(html)
            resized_thumbnail = converted_thumbnail.resize((300, 300))
            img = ImageTk.PhotoImage(image=resized_thumbnail)
            canvas.config(height=img.height(), width=img.width())
            canvas.create_image((0, 0), image=img, anchor="nw")

            streams_list.clear()

            for res in all_res_options:
                stream = yt.streams.get_by_resolution(resolution=f"{res}")
                if stream is None:
                    pass
                else:
                    streams_list.append(f"{res}")

            download_options = tk.OptionMenu(self.root, value, *streams_list)
            download_options.grid(column=1, row=1)

        url_reader = tk.Button(height=1, width=3, background="red", command=url_read)
        url_reader.grid(column=1, row=2, padx=20)

        self.download_progress = tk.DoubleVar()
        progress_bar = tk.ttk.Progressbar(mode="determinate", variable=self.download_progress, orient=tk.VERTICAL)
        progress_bar.grid(column=1, row=3, pady=10)

        def downloading(stream, chunk, bytes_remaining):
            progress_bar.start()
            filesize = stream.filesize
            progress = (float(abs(bytes_remaining-filesize)/filesize))
            self.download_progress.set(progress)
            progress_bar.step(progress)

        def download_complete(stream, filepath):
            print("Download complete!")
            progress_bar.stop()

        def start_download():
            yt_url = url_text.get()
            yt = pytube.YouTube(yt_url)
            yt.register_on_progress_callback(func=downloading)
            yt.register_on_complete_callback(func=download_complete)
            download_choice = value.get()
            stream = yt.streams.get_by_resolution(resolution=f"{download_choice}")
            stream.download(output_path=r"C:\Users\drago\Downloads")

        # create a button to press when we're ready to start the download
        download_button = tk.Button(height=1, width=3, background="blue", command=start_download)
        download_button.grid(column=1, row=3, sticky="s", pady=20)

        self.root.mainloop()


Window()
