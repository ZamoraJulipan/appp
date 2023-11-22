from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.toast import toast
import threading
import os

class Ui(ScreenManager):
    pass

class dev(MDApp):
    def build(self):
        import datetime
        hora = datetime.datetime.now().time().hour
        momento_del_dia = datetime.datetime.now().strftime('%p')
        if (hora in range(6,11) and momento_del_dia == 'PM') or (hora == 12 and momento_del_dia == 'AM') or (hora in range(1,6) and momento_del_dia == 'AM'):
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'
        self.opcion = None
        Builder.load_file('main.kv')
        return Ui()

    def download_yt(self,link,nombre):
        from pytube import YouTube
        self.listo = False
        if link == '' or nombre == '':
            toast('LLene todos los campos')
            return None
        video = YouTube(link)
        nombre = nombre + '.mp4'
        def descarga(name=nombre,vd=video):
            stream = vd.streams.get_highest_resolution()
            stream.download(filename=name)
            self.listo = True
        hilo = threading.Thread(target=descarga)
        hilo.start()
        toast('Descargando...')
    
    def eleccion_descarga(self,electiva):
        self.opcion = electiva
        self.root.ids.opcionVideo.disabled = True
        self.root.ids.opcionAudio.disabled = True
    
    def comprobar_existencia(self,nombre):
        revisar = str(os.path.exists(f'{nombre}.mp4'))
        toast(f'{self.listo},{revisar}')

dev().run()
