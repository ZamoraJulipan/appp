from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import SlideTransition
import numpy

class main(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepPurple'
        return Builder.load_file('main.kv')
    
    def presionado(self,user,psswd):
        if user == 'Ayayitas' and psswd == 'K4r3n2?2?':
            self.root.current = "main_opciones"
        else:
            self.root.current = "main_opciones"
    
    def rendimiento(self,nombre):
        if not self.root.has_screen(nombre):
            if nombre.startswith('a'):
                self.root.add_widget(Builder.load_file(f'.\\areas\\{nombre}.kv'))
    
    def regresar(self,pantalla):
        self.root.transition = SlideTransition(direction='right')
        self.root.current = pantalla
        self.root.transition = SlideTransition(direction='left')
    
    def cambio(self,nombre_pantalla):
        if nombre_pantalla == 'opciones_calculadora':
            self.root.current = nombre_pantalla
        else:
            self.rendimiento(nombre_pantalla)
            self.root.current = nombre_pantalla

    def area_triangulo(self,b,h):
        if b and h:
            b,h = float(b),float(h)
            area = str(round((b*h)/2,3))
            self.root.get_screen('a_triangulo').ids.rt.text = f'Area = {area} u²'
    
    def area_romboide(self,b,h):
        if b and h:
            b,h = float(b),float(h)
            area = str(round(b*h,3))
            self.root.get_screen('a_romboide').ids.rt.text = f'Area = {area} u²'

    def area_trapecio(self,b1,b2,h):
        if b1 and b2 and h:
            b1,b2,h = float(b1),float(b2),float(h)
            area = round(((b1+b2)/2)*h,3)
            self.root.get_screen('a_trapecio').ids.rt.text = f'Area = {area} u²'
    
    def area_rombo(self,dM,dm):
        if dM and dm:
            dM,dm = float(dM),float(dm)
            area = str(round((dM*dm)/2,3))
            self.root.get_screen('a_rombo').ids.rt.text = f'Area = {area} u²'
    
    def area_poligono(self,nl,l,a):
        if nl and l and a:
            nl,l,a = float(nl),float(l),float(a)
            area = round((nl*l*a)/2,3)
            self.root.get_screen('a_poligono').ids.rt.text = f'Area = {area} u²'
    
    def area_circulo(self,r):
        if r:
            r = float(r)
            area = round(numpy.pi*r**2,3)
            self.root.get_screen('a_circulo').ids.rt.text = f'Area = {area} u²'
    
    def area_sectorc(self,a,r):
        if a and r:
            a,r = float(a),float(r)
            area = round((numpy.pi*a*r**2)/360,3)
            self.root.get_screen('a_sectorc').ids.rt.text = f'Area = {area} u²'

main().run()