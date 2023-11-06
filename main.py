from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivymd.toast import toast

class OverlayApp(MDApp):
    def build(self):
        layout = FloatLayout()
        button = Button(text='Mi Botón de Superposición')
        button.bind(on_press=self.show_overlay)
        layout.add_widget(button)
        return layout

    def show_overlay(self, *args):
        toast('funciona')

OverlayApp().run()