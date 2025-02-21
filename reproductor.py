from tkinter import ttk
import tkinter as tk
import pygame.mixer as mixer
from mutagen.mp3 import MP3
import time

mixer.init()

class Reproductor(ttk.Frame):
    def __init__(self, container, music):
        super().__init__(container)

        # Definición de botón encargado de dar lugar a la función de reproducir música
        self.play_button = ttk.Button(self, text='Star', command=self.play_music)
        self.play_button.grid()

        self.music = music # Asignación del argumento 'music' a una propiedad de la clase
        self.music_mut = MP3(music) # Definir arg 'music' como argumento de la clase MP3

        # Acceder a info (duración del audio) del MP3 object:
        self.music_time_info = time.strftime('%M:%S', time.gmtime(self.music_mut.info.length))

        # Declaración del StringVar y label que gestionara la ubicación del tiempo del audio en pantalla
        self.music_time = tk.StringVar(value="00:00")
        self.time_label = tk.Label(self, textvariable=self.music_time)
        self.time_label.grid()

        # Variable de control para la correcta ejucución de 'increment_time'
        self.time_running = False

    def load_music(self):
        mixer.music.load(self.music)
        mixer.music.set_volume(0.3)

    def play_music(self):
        self.music_time.set(value="00:00")
        self.load_music()
        if not self.time_running:
            self.increment_time()
        mixer.music.play(loops=0)

    def increment_time(self):
        self.time_running = True
        music_time = self.music_time.get()
        if music_time != self.music_time_info:
            minutes, seconds = music_time.split(":")
            if int(seconds) < 59:
                seconds = int(seconds) + 1
                minutes = int(minutes)
            else:
                seconds = 0
                minutes = int(minutes) + 1
        else:
            minutes, seconds = map(int, self.music_time_info.split(":"))
        self.music_time.set(f"{minutes:02d}:{seconds:02d}")
        self.after(1000, self.increment_time)