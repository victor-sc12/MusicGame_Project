import tkinter as tk
from tkinter import ttk
from music import MusicProcess as Mp
from PIL import Image, ImageTk

class FirstView(ttk.Frame):
    def __init__(self, cointainer, music):
        super().__init__(cointainer)
        self.music = music
        self.music_image = ImageTk.PhotoImage(Image.open(self.music.get_image()).resize((320,320)))
        self.artist_name = self.music.get_artist()
        self.song_name = self.music.get_name()
        self.char_values = []
        self.char_values_entry = []
        self.input_frame = ttk.Frame()
        self.input_frame.grid()
        self.boton = ttk.Button(self.input_frame, text="Comprobar", command=self.process_entry)
        self.boton.grid(row=2, columnspan=3)
        self.label_img = ttk.Label(self, image=self.music_image)
        self.label_img.grid()
        self.label_title = ttk.Label(self, text=self.artist_name)
        self.label_title.grid()
        self.put_spaces()

    def process_entry(self):
        i = 0
        for values in self.char_values_entry:
            self.char_values_entry[i] = values.get()
            i+=1
        # self.char_values_entry = [v for v in self.char_values_entry if v != '']
        if self.char_values_entry == self.char_values:
            ttk.Label(self.input_frame, text="Well Done").grid(row = 1)
        else:
            ttk.Label(self.input_frame, text="Error. Try again").grid(row=1)
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
                print(j, self.char_values_entry[j])
                j+=1
            else:
                ttk.Label(self.input_frame, width=5).grid(row=0, column=i)
            i += 1
