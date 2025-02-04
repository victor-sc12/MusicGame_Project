import tkinter as tk
from tkinter import ttk
from music import MusicProcess as Mp
from PIL import Image, ImageTk

class FirstView(ttk.Frame):
    def __init__(self, cointainer, music):
        super().__init__(cointainer)
        self.music = music # Inicializar propiedad self.music con el objeto (music) enviado como paramétro

        # Inicializar atributos (img, artista, songname) del objeto dentro de esta clase:
        self.music_image = ImageTk.PhotoImage(Image.open(self.music.get_image()).resize((320,320)))
        self.artist_name = self.music.get_artist()
        self.song_name = self.music.get_name()

        self.char_values = [] # lista para almacenar los char de songname
        self.char_values_entry = [] # lista para los valores de entrada

        # Definición del frame donde se ubicaran los 'Entry Widgets' para los datos de entrada:
        self.input_frame = ttk.Frame(self)
        self.input_frame.grid()

        # Definición del label donde se ubicarán los mensajes de alerta
        self.msg_label = ttk.Label(self, text='')
        self.msg_label.grid(row=1)

        # Definición del Button widget para procesar el dato ingresado
        self.boton = ttk.Button(self, text="Comprobar", command=self.process_entry)
        self.boton.grid(row=2)

        # Colocación de los atributos img, artistname dentro del frame principal
        self.label_img = ttk.Label(self, image=self.music_image)
        self.label_img.grid()
        self.label_title = ttk.Label(self, text=self.artist_name)
        self.label_title.grid()

        # Declaración de la función que coloca los Entry Widgets según el nombre de la canción
        self.put_spaces()

    def process_entry(self):
        i = 0
        for values in self.char_values_entry:
            self.char_values_entry[i] = values.get()
            i+=1
        # self.char_values_entry = [v for v in self.char_values_entry if v != '']
        if self.char_values_entry == self.char_values:
            self.msg_label.configure(text='Well Done')
            #ttk.Label(self.input_frame, text="Well Done").grid(row = 1)
        else:
            self.msg_label.configure(text='Error. Try again')
            #ttk.Label(self.input_frame, text="Error. Try again").grid(row=1)
        print(self.char_values_entry)
        print(self.char_values)
        self.char_values_entry = []
        self.char_values = []
        self.put_spaces()

    def put_spaces(self):
        i,j = 0,0
        print(j)
        for char in self.song_name:
            if char !=' ':
                self.char_values.append(char)
                self.char_values_entry.append(tk.StringVar())
                ttk.Entry(self.input_frame, width=5, textvariable=self.char_values_entry[j]).grid(row=0, column=i)
                #print(j, self.char_values_entry[j])
                j+=1
            else:
                ttk.Label(self.input_frame, width=5).grid(row=0, column=i)
            i += 1
