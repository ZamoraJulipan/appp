from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.toast import toast

KV = '''
<ui>:
    MDScren:
        MDBoxLayout:
            MDRectangleFlatButton:
                text: 'Importar'
                on_release:
                    app.importar()
'''

class Ui(ScreenManager):
    pass

class dev(MDApp):
    def build(self):
        Builder.load_string(KV)
        return Ui()

    def importar(self):
        from pytube import YouTube
        toast('Se ha importado con exito')

dev().run()