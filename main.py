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
            title = 'Batipython',  
            message = 'Esta es una notificacion',  
            app_icon = None,  
            timeout = 10,  
            toast = False,
            app_name = 'Batipy'
        )

dev().run()
