from pathlib import Path
import os
# from db_connection import get_songs
from music_class import Music as Mc
import music_class

class MusicProcess:
    def __init__(self):
        super().__init__()
    #    self.path = Path("C:/Users/victo/my_things/code_things/Audios para programas")
        self.musicobj_list = []
        self.set_objsong()

    def get_objsong(self, idx):
       return self.musicobj_list[idx]

    def set_objsong(self):
        """
        for fila in get_songs():
            self.musicobj_list.append(Mc(f'{fila[1]}', f'{fila[2]}', f'{fila[3]}',
                                         f'{fila[5]}', f'{fila[6]}', f'{fila[7]}'))
        """
        for fila in music_class.get_objlist():
            self.musicobj_list.append(fila)

#mp = MusicProcess()
#print(mp.musicobj_list[0].get_artist())