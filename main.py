from plyer import notification
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

KV = '''
<ui>:
    MDScreen:
        MDBoxLayout:
            MDRectangleFlatButton:
                text: 'notificar'
                on_release:
                    app.notificar()
'''

class Ui(ScreenManager):
    pass

class dev(MDApp):
    def build(self):
        Builder.load_string(KV)
        return Ui()
    
    def notificar(self):
        notification.notify(
            title = "Coso"
            message = "Cosos content"
        )

dev().run()
