import tkinter as tk
from tkinter import ttk
import tkinter.font as fnt
from PIL import Image, ImageTk

# fnt.nametofont("TkDefaultFont").config(size=15)

class FirstView(ttk.Frame):
    def __init__(self, cointainer, music):
        super().__init__(cointainer)
        self.music = music # Inicializar propiedad self.music con el objeto (music) enviado como paramétro

        # Inicializar atributos (img, artista, songname) del objeto dentro de esta clase:
        self.music_image = ImageTk.PhotoImage(Image.open(self.music.get_image()))
        self.artist_name = self.music.get_artist()
        self.song_name = self.music.get_name()

        # Definición del frame donde se ubicaran los 'Entry Widgets' para los datos de entrada:
        self.input_frame = ttk.Frame(self)
        self.input_frame.grid(padx='10', sticky="ew")
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.columnconfigure(1, weight=2)
        # self.input_frame.rowconfigure(0, weight=1)

        # Labels para indicaciones:
        self.label_entry1 = ttk.Label(self.input_frame, text='Song Name: ', anchor='center')
        self.label_entry1.grid(column=0, row=0, sticky="ew", padx=(0, 5))
        self.label_entry2 = ttk.Label(self.input_frame, text='Artist Name: ', anchor='center')
        self.label_entry2.grid(column=0, row=1, sticky="ew", padx=(0, 5))

        # StringVars y Entry widgtes que gestionaran los valores ingresados:
        self.song_name_value = tk.StringVar(value='Put the song name here')
        self.artist_name_value = tk.StringVar(value='Put the artist name here')
        self.song_name_entry = ttk.Entry(self.input_frame, textvariable=self.song_name_value)
        self.song_name_entry.grid(column=1, row=0, sticky="ew")
        self.artist_name_entry = ttk.Entry(self.input_frame, textvariable=self.artist_name_value)
        self.artist_name_entry.grid(column=1, row=1, sticky="ew")

        for child in self.input_frame.winfo_children():
            child.grid_configure(pady=(0, 5))

        # Un diccionario que también permitirá gestionar validaciones:
        self.entrys = {self.song_name_entry: [self.label_entry1, self.song_name_value, self.song_name_entry],
                       self.artist_name_entry: [self.label_entry2, self.artist_name_value, self.artist_name_entry]}

        # Definición del Button widget para procesar el dato ingresado
        self.boton = ttk.Button(self, text="Comprobar", command=self.process_entry)
        self.boton.grid(pady=(0, 5))

        # Colocación de los atributos img, artistname dentro del frame principal
        self.label_img = ttk.Label(self, image=self.music_image, background="yellow")
        self.label_img.grid()
        # self.label_img.columnconfigure(0, weight=1)

        # Definición del Button widget para cambiar de canción:
        self.changesong_button = ttk.Button(self, text='Next Song')

        # Acá se pone esto porque se pretende que esta clase Frame se expanda a lo largo de la pantalla:
        self.columnconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)

        # Clean entrys:
        self.song_name_entry.bind("<FocusIn>", lambda event: self.clean_entry(self.song_name_entry))
        self.artist_name_entry.bind("<FocusIn>", lambda event: self.clean_entry(self.artist_name_entry))

    def validar_entry(self, value, entry_widget):
        if self.entrys[entry_widget][1].get().upper() != value.upper():
            self.entrys[entry_widget][0].configure(foreground='red', font='bold')
            self.entrys[entry_widget][1].set('Your entry data is incorrect')
            # entry_widget.configure(textvariable=self.entrys[entry_widget])
            return False
        else:
            self.entrys[entry_widget][0].configure(foreground='green', font='bold')
            self.entrys[entry_widget][1].set(value)
            # self.entrys[entry_widget][2].configure(state='disabled')
            entry_widget.configure(state='disabled')
            # entry_widget.configure(textvariable=self.entrys[entry_widget])
            return True

    def process_entry(self):
        song_name_entry = self.validar_entry(self.song_name, self.song_name_entry)
        artist_name_entry = self.validar_entry(self.artist_name, self.artist_name_entry)

        if song_name_entry and artist_name_entry:
            self.changesong_button.grid()

    def clean_entry(self, entry_widget):
        self.entrys[entry_widget][2].delete(0, tk.END)