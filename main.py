from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.toast import toast
import os

toque = []
grabar = False
n_toques = 0
toque_actual = 0

class Ui(ScreenManager):
    def on_touch_down(self, touch):
        global grabar
        global toque_actual
        if grabar == True:
            toast("Se ha tocado la pantalla")
            toque.append((touch.x, touch.y))
            toque_actual = toque_actual+1
            if toque_actual == n_toques:
                grabar = False
        else:
            super(Ui, self).on_touch_down(touch)#estudiar

class MyApp(MDApp):
    def build(self):
        self.numero_de_archivo = 0
        Builder.load_file('toques.kv')
        return Ui()
    
    def guardar(self): #mejorar, guardado y nombre
        while os.path.exists(f'coordenadas{self.numero_de_archivo}.txt'):
            self.numero_de_archivo = self.numero_de_archivo+1
        with open(f'coordenadas{self.numero_de_archivo}.txt', 'a+') as archivo:
            for coordenadas in toque:
                archivo.write(str(coordenadas) + '\n')
            archivo.close()

    def verify_bool(self):
        toast(str(os.path.exists(f'coordenadas{self.numero_de_archivo}.txt')) + '  ' +
              str(os.path.exists('normal.txt')))
    
    def empezar_toques(self,numero):
        global n_toques
        global grabar
        n_toques = numero
        grabar = True
    
    def verify_text(self):
        try:
            with open(f'coordenadas{self.numero_de_archivo}.txt', 'r') as archivo:
                self.root.ids.coordenadas.text = archivo.read()
                archivo.close()
        except FileNotFoundError:
            toast('No existe')

    def archivo_normal(self):
        with open('normal.txt','w+') as archivo_normal:
            archivo_normal.write('Hola')
            archivo_normal.close()
        toast('Ya se creó')

MyApp().run()