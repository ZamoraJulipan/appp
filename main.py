from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import SlideTransition
import numpy

class main(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepPurple'
        return Builder.load_file('main.kv')
    
    def regresar(self,pantalla):
        self.root.transition = SlideTransition(direction='right')
        self.root.current = pantalla
        self.root.transition = SlideTransition(direction='left')
    
    def cambio(self,nombre_pantalla):
        self.root.current = nombre_pantalla

main().run()
