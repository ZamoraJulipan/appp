from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.filemanager import MDFileManager
from kivy.lang import Builder
from kivymd.toast import toast
import threading

KV = '''
<ui>:
    MDScreen:
        MDBoxLayout:
            orientation: 'horizontal'
            pos_hint: {'center_y':.8}
            MDLabel:
                id: labeluno
                text: ''
        MDBoxLayout:
            orientation: 'horizontal'
            pos_hint: {'center_y':.5}
            MDLabel:
                id: labeldos
                text: ''
        MDBoxLayout:
            orientation: 'horizontal'
            pos_hint: {'center_y':.2}
            MDLabel:
                id: labeltres
                text: ''
        MDBoxLayout:
            MDRectangleFlatButton:
                text: 'Abrir imagen'
                on_release:
                    app.file_manager_open()
'''

class Ui(ScreenManager):
    pass

class dev(MDApp):
    def build(self):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path
        )
        Builder.load_string(KV)
        return Ui()
    def file_manager_open(self):
        self.file_manager.show('/')
    def select_path(self, path):
        try:
            self.root.ids.labeluno.text = ''
            self.root.ids.labeldos.text = ''
            self.root.ids.labeltres.text = ''
            self.file_manager.close()
            def actualizar1(norma,path):
                from rembg import remove
                from PIL import Image
                self.root.ids.labeldos.text = 'Sí se inició'
            empieza = threading.Thread(target=actualizar1,args=(1,path))
            empieza.start()
            toast('imagen png descargandose...')
        except PermissionError:
            self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

dev().run()