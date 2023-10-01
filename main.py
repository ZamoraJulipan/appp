from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from rembg import remove
from PIL import Image

class Ui(ScreenManager):
    pass

class dev(MDApp):
    def build(self):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path
        )
        Builder.load_file('pngDis.kv')
        return Ui()
    def file_manager_open(self):
        self.file_manager.show('/')
    def select_path(self, path):
        try:
            self.file_manager.close()
            output_path = 'salida.png'
            entrada = Image.open(path)
            salida = remove(entrada)
            salida.save(output_path)
            toast('imagen png descargada')
        except PermissionError:
            self.file_manager.close()
    def exit_manager(self,*args):
        self.file_manager.close()

dev().run()