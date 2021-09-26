import tkinter as tk
from tkinter.constants import END, N
import youtube_dl
from pathlib import Path
import os


class Window:
    def __init__(self, window):
        self.window = window
        self.window.geometry("700x500")
        self.window.title("Youtube Video Downloader")
        self.url_list = []
        self.SAVEPATH = os.path.join(Path.home(), "Downloads")

        self.url_input = tk.StringVar()

        # LABELS
        self.url_label = tk.Label(self.window, text="URL", height=4, font=13).grid(
            column=0, row=0, padx=20
        )

        # TEXTBOXES
        self.url_textbox = tk.Entry(window, width=40, textvariable=self.url_input)
        self.url_textbox.place(relx=0.5, anchor=N, rely=0.06)

        # BUTTONS
        self.url_button = tk.Button(
            window, text="ADD", width=4, height=1, command=self.add_button
        ).place(relx=0.9, anchor=N, rely=0.053)
        self.download_button = tk.Button(
            window,
            text="Download",
            command=self.download_button,
        ).place(relx=0.9, anchor=N, rely=0.9)

    def add_button(self) -> None:
        self.inputed_url = self.url_input.get()
        self.url_list.append(self.inputed_url)
        print(self.url_input, self.url_list)
        self.url_textbox.delete(0, END)

    def download_button(self) -> None:
        with youtube_dl.YoutubeDL(
            {
                "outtmpl": os.path.join(self.SAVEPATH, "%(title)s.%(ext)s"),
            }
        ) as ydl:
            try:
                ydl.download(self.url_list)
            except youtube_dl.utils.SameFileError as e:
                print("You already have this file!")


def main():
    root = tk.Tk()
    app = Window(root)
    root.mainloop()


if __name__ == "__main__":
    main()
