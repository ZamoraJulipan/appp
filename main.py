from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.toast import toast
import webbrowser

KV = '''
<ui>:
    MDScreen:
        MDBoxLayout:
            MDRectangleFlatButton:
                text: 'Abrir imagen'
                on_release:
                    app.abrir_pagina()
'''

class Ui(ScreenManager):
    pass

class dev(MDApp):
    def build(self):
        Builder.load_string(KV)
        return Ui()
    def abrir_pagina(self):
        webbrowser.open('png.html',new=2)

dev().run()