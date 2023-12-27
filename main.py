from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
import pymysql
from kivymd.toast import toast

pre_diseno = list()
final_string = ''

with open('prestablecido.txt','r') as archivo:
    lectura = archivo.read()
    nueva_lectura = lectura.split('\n')
    for linea in nueva_lectura:
        pre_diseno.append(linea)
        
for contra in pre_diseno:
    if final_string == '':
        final_string = f'''
        OneLineListItem:
            text: {contra}
'''
    else:
        anterior_string = final_string
        final_string = f'''
{anterior_string}
        OneLineListItem:
            text: {contra}
'''
final_string.strip('')

class Ui(ScreenManager):
    pass

class dev(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        Builder.load_file('batiutiles.kv')
        return Ui()
    
    def log_in(self,usuario,contra):
        if usuario == '' or contra == '':
            toast('Complete')
        else:
            try:
                conexion = pymysql.connect(
                    host='192.168.0.16',
                    user=usuario,
                    password=contra,
                    db='ejemplo'
                )
                cursor = conexion.cursor()
            except Exception:
                toast('Error')

dev().run()