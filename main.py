from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.toast import toast
import os

class Ui(ScreenManager):
    pass

class main(MDApp):
    def build(self):
        Builder.load_file('main.kv')
        return Ui()
    
    def comprobar(self):
        if os.path.exists('texto_nuevo.txt'):
            toast('Sí')
        else:
            toast('No')

    def guardar(self,texto):
        try:
            with open('texto_nuevo.txt','w+') as archivo:
                archivo.write(texto)
                archivo.close()
        except TypeError:
            pass

main().run()
