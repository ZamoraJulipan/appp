from android.permissions import check_permission, Permission
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.toast import toast

KV = '''
<ui>
    MDScreen:
        MDBoxLayout:
            MDRectangleFlatButton:
                text: 'probar'
                on_release:
                    app.acceso_almacenamiento()
'''

class Ui(ScreenManager):
    pass

class dev(MDApp):
    def build(self):
        Builder.load_string(KV)
        return Ui()
    def acceso_almacenamiento(self):
        if check_permission(Permission.WRITE_EXTERNAL_STORAGE):
            toast(text='se dió permiso')
        else:
            toast(text='No se pudo o hubo error')

dev().run()