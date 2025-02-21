import tkinter as tk
from first_view import FirstView as Fv
from reproductor import Reproductor as Rp
from tkinter import ttk
from tkinter.constants import HORIZONTAL
from ventana import set_dpi_awareness as vista_ventana
from music import MusicProcess as Mp

class MusicFrame(ttk.Frame):
    def __init__(self, conteiner, controller):
        super().__init__(conteiner)

        # Frame principal que abarca t0do el contenido:
        # self.main_frame = ttk.Frame(self)
        # self.main_frame.grid(pady='15')

        # Instanciamiento de MusicProcess
        self.music = Mp()

        # self.index = 0

        # Obtención del objeto Music actual y de su atributo 'song':
        self.generador = self.generador_lista()
        self.current_music = next(self.generador) #self.music.get_objsong(self.index)
        self.current_music_audio = self.current_music.get_song()

        # Instanciamiento de la clase FirstView:
        self.firstView = Fv(self, self.current_music)
        self.firstView.grid()

        # Instanciamiento de la clase Reproductor
        rp = Rp(self, self.current_music_audio)
        rp.grid()

        # Change song button:
        self.validation = False
        self.firstView.changesong_button.configure(command=self.update_obj)

        # Change page button:
        chage_button = ttk.Button(self, text='Check Results', command=lambda: controller.switch_frame(FrontPage))

    def update_obj(self):
        #print("Si funciono: " + str(self.index))
        # self.validation = True
        self.current_music = next(self.generador)
        self.current_music_audio = self.current_music.get_song()

        self.firstView = Fv(self, self.current_music)
        self.firstView.grid(row = 0)

        rp = Rp(self, self.current_music_audio)
        rp.grid(row = 1)


    def generador_lista(self):
        for obj in self.music.musicobj_list:
            yield obj


class FrontPage(ttk.Frame):
    def __init__(self, conteiner, controller):
        super().__init__(conteiner)

        tittle_label = ttk.Label(self, text='THE MUSIC GAME')
        tittle_label.grid()

        init_button = ttk.Button(self, text='Iniciar', command=lambda: controller.switch_frame(MusicFrame))
        init_button.grid()


class Tkinter(tk.Tk):
    def __init__(self):
        super().__init__()
        main_frame = ttk.Frame(self)
        main_frame.grid(pady='15')
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (FrontPage, MusicFrame):
            frame = F(main_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0)

        self.switch_frame(FrontPage)

    def switch_frame(self, frame):
        game_page = self.frames[frame]
        game_page.tkraise()


root = Tkinter()
root.mainloop()