
class Music:
    def __init__(self, name, artist, album, song, lyric, image):
        super().__init__()
        self.name = name
        self.artist = artist
        self.album = album
        self.song = song
        self.lyric = lyric
        self.image = image

    def get_name(self): return self.name
    def get_artist(self): return self.artist
    def get_album(self): return self.album
    def get_song(self): return self.song
    def get_lyric(self): return self.lyric
    def get_image(self): return self.image

music = Music('Well I Wonder', 'The Smiths', 'Meat Is Murder',
              "C:/Users/victo/my_things/code_things/MusicProjectGUI/Songs2MusicProject/Well I Wonder.mp3",
              "C:/Users/victo/my_things/code_things/MusicProjectGUI/Letters2MusicProject/Well I Wonder.txt",
              "C:/Users/victo/my_things/code_things/MusicProjectGUI/Images2MusicProject/Well I Wonder.jpeg")
music2 = Music('Cachito de Galaxia', 'Porter', 'La Historia Sin Fin',
               "C:/Users/victo/my_things/code_things/MusicProjectGUI/Songs2MusicProject/Cachito de Galaxia.mp3",
               "C:/Users/victo/my_things/code_things/MusicProjectGUI/Letters2MusicProject/Cachito de Galaxia.txt",
               "C:/Users/victo/my_things/code_things/MusicProjectGUI/Images2MusicProject/Cachito de Galaxia.jpeg")
musicobj_list = [music, music2]
for objeto in musicobj_list:
    print(objeto.get_name(), objeto.get_artist(), objeto.get_album(), objeto.get_song(), objeto.get_lyric())

def get_objlist(): return musicobj_list