from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.filemanager import MDFileManager
from kivy.lang import Builder
from kivymd.toast import toast
from kivy.clock import Clock
import threading

KV = '''
<ui>:
    MDScreen:
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
            self.file_manager.close()
            def actualizar1(norma,path):
                from rembg import remove
                from PIL import Image
                if norma == 1:
                    output_path = 'salida.png'
                    entrada = Image.open(path)
                    salida = remove(entrada)
                    salida.save(output_path)
            empieza = threading.Thread(target=actualizar1,args=(1,path))
            empieza.start()
            toast('imagen png descargada')
        except PermissionError:
            self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

dev().run()