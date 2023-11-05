from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.toast import toast
import os

toque = []
grabar = False

class Ui(ScreenManager):
    def on_touch_down(self, touch):
        global grabar
        if grabar == True:
            toast("Se ha tocado la pantalla")
            toque.append((touch.x, touch.y))
        else:
            super(Ui, self).on_touch_down(touch)#estudiar

class MyApp(MDApp):
    def build(self):
        self.numero_de_archivo = 0
        Builder.load_file('toques.kv')
        return Ui()
    
    def on_stop(self): #mejorar, guardado y nombre
        while os.path.exists(f'coordenadas{self.numero_de_archivo}.txt'):
            self.numero_de_archivo = self.numero_de_archivo+1
        with open(f'coordenadas{self.numero_de_archivo}.txt', 'a+') as archivo:
            for coordenadas in toque:
                archivo.write(str(coordenadas) + '\n')
            archivo.close()

    def empezar_toques(self):
        global grabar
        grabar = True
    
    def verify_text(self):
        with open(f'coordenadas{self.numero_de_archivo}.txt', 'r') as archivo:
            self.root.ids.coordenadas.text = archivo.read()
            archivo.close()

MyApp().run()