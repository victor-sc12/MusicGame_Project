from tkinter import ttk
import tkinter as tk
import pygame.mixer
from music import MusicProcess as Mp
from pygame import mixer
from PIL import Image, ImageTk
from mutagen.mp3 import MP3
import time

class Reproductor(ttk.Frame):
    def __init__(self, container, music):
        super().__init__(container)
        self.music = Mp()
        # self.play_image = ImageTk.PhotoImage(Image.open("C:\\Users\\victo\\my_things\\code_things\\"
        #                             "Imagenes para programas\\play.png").resize((64,64)))
        self.play_button = ttk.Button(self, text='Star', command=self.play_music)
        self.play_button.grid()
        # self.current_song = self.music.get_objsong(0)
        # self.current_song_sound = self.current_song.get_song()
        self.music_sound = music
        self.music_mut = MP3(music)
        self.music_time_info = time.strftime('%M:%S', time.gmtime(self.music_mut.info.length))
        self.music_time = tk.StringVar(value="00:00")
        self.time_label = tk.Label(self, textvariable=self.music_time)
        self.time_label.grid()

    def load_music(self):
        pygame.mixer.init()
        mixer.music.load(self.music_sound)
        mixer.music.set_volume(0.3)

    def play_music(self):
        self.music_time.set(value="00:00")
        self.increment_time()
        self.load_music()
        mixer.music.play(-1)

    def increment_time(self):
        music_time = self.music_time.get()
        if music_time != self.music_time_info:
            minutes, seconds = music_time.split(":")
            if int(seconds) < 59:
                seconds = int(seconds) + 1
                minutes = int(minutes)
            else:
                seconds = 0
                minutes = int(minutes) + 1
            self.music_time.set(f"{minutes:02d}:{seconds:02d}")
            self.after(1000, self.increment_time)