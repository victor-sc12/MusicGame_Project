import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class FirstView(ttk.Frame):
    def __init__(self, cointainer, music):
        super().__init__(cointainer)
        self.music = music # Inicializar propiedad self.music con el objeto (music) enviado como paramétro

        # Inicializar atributos (img, artista, songname) del objeto dentro de esta clase:
        self.music_image = ImageTk.PhotoImage(Image.open(self.music.get_image()).resize((320,320)))
        self.artist_name = self.music.get_artist()
        self.song_name = self.music.get_name()

        # Definición del frame donde se ubicaran los 'Entry Widgets' para los datos de entrada:
        self.input_frame = ttk.Frame(self)
        self.input_frame.grid(padx='10')
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.rowconfigure(0, weight=1)

        # StringVars y Entry widgtes que gestionaran los valores ingresados:
        self.song_name_value = tk.StringVar(value='Put the song name here')
        self.artist_name_value = tk.StringVar(value='Put the artist name here')
        self.song_name_entry = ttk.Entry(self.input_frame, textvariable=self.song_name_value)
        self.song_name_entry.grid(column=0, row=0, sticky="ew")
        self.artist_name_entry = ttk.Entry(self.input_frame, textvariable=self.artist_name_value)
        self.artist_name_entry.grid(column=0, row=1, sticky="ew")

        # Un diccionario que también permitirá gestionar validaciones:
        self.entrys = {self.song_name_entry: self.song_name_value, self.artist_name_entry: self.artist_name_value}

        # Definición del Button widget para procesar el dato ingresado
        self.boton = ttk.Button(self, text="Comprobar", command=self.process_entry)
        self.boton.grid()

        # Colocación de los atributos img, artistname dentro del frame principal
        self.label_img = ttk.Label(self, image=self.music_image)
        self.label_img.grid()

        # Definición del Button widget para cambiar de canción:
        self.changesong_button = ttk.Button(self, text='Next Song')

        # Acá se pone esto porque se pretende que esta clase Frame se expanda a lo largo de la pantalla:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def validar_entry(self, value, entry_widget):
        if self.entrys[entry_widget].get().upper() != value.upper():
            self.entrys[entry_widget].set('Your entry data is incorrect. Try again.')
            entry_widget.configure(textvariable=self.entrys[entry_widget])
            return False
        else:
            entry_widget.configure(textvariable=self.entrys[entry_widget])
            return True

    def process_entry(self):
        song_name_entry = self.validar_entry(self.song_name, self.song_name_entry)
        artist_name_entry = self.validar_entry(self.artist_name, self.artist_name_entry)

        if song_name_entry and artist_name_entry:
            self.changesong_button.grid()
