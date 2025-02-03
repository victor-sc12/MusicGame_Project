import tkinter as tk
from tkinter import ttk
from tkinter.constants import HORIZONTAL
from ventana import set_dpi_awareness as vista_ventana
import pygame
from mutagen.mp3 import MP3
import time

vista_ventana()

class Tkinter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        container = ttk.Frame(self)
        container.grid(pady=10, padx=10)
        ttk.Label(container, text="HOLAMUNDO").grid()
        reproductor = Reproductor(container)
        reproductor.grid()


class Reproductor(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.music = "C:\\Users\\victo\\my_things\\code_things\\Audios para programas\\MusicaFondo.mp3"
        self.music_mut = MP3(self.music)
        self.music_leght = self.music_mut.info.length
        self.time_form = time.strftime('%M:%S', time.gmtime(self.music_leght))
        self.music_time = tk.StringVar(value="04:50")
        print(self.time_form)
        print(self.music_leght)

        self.scale = ttk.Scale(self, from_=0, to=self.music_leght, orient=HORIZONTAL, value=0)
        self.scale.grid()

        counter = ttk.Label(self, textvariable=self.music_time)
        counter.grid()

        self.increment_time()
        self.increment_slide()

    def increment_time(self):
        music_time = self.music_time.get()
        if music_time != self.time_form:
            minutes, seconds = music_time.split(":")
            if int(seconds) >= 0:
                seconds = int(seconds) + 1
                minutes = int(minutes)
            if int(seconds) > 59:
                seconds = 0
                minutes += 1

            self.music_time.set(f"{minutes:02d}:{seconds:02d}")
            self.after(1000, self.increment_time)

    def increment_slide(self):
        if self.scale.get() < self.scale.cget("to"):
            self.scale.set(self.scale.get()+1)
            self.after(1000, self.increment_slide)

    def slide(self):
        pass

root = Tkinter()
root.mainloop()