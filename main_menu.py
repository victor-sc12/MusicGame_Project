import tkinter as tk
from first_view import FirstView as Fv
from reproductor import Reproductor as Rp
from tkinter import ttk
from tkinter.constants import HORIZONTAL
from ventana import set_dpi_awareness as vista_ventana
from music import MusicProcess as Mp

class Tkinter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(pady='15')
        self.music = Mp()
        self.current_music = self.music.get_objsong(1)
        self.current_music_audio = self.current_music.get_song()
        fv = Fv(self.main_frame, self.current_music)
        fv.grid()
        rp = Rp(self.main_frame, self.current_music_audio)
        rp.grid()


root = Tkinter()
root.mainloop()