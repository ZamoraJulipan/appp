from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

class Ui(ScreenManager):
    pass

class main(MDApp):
    def build(self):
        Builder.load_file('main.kv')
        return Ui()
    
    def guardar(self,texto):
        try:
            with open('.\\sdcard\\Documents\\texto_nuevo.txt','w+') as archivo:
                archivo.write(texto)
                archivo.close()
        except TypeError:
            pass

main().run()
