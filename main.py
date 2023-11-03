from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.toast import toast

class TouchDetector(Widget):
    def on_touch_down(self, touch):
        # Se llama cuando se toca la pantalla
        toast("Se ha tocado la pantalla")

class MyApp(MDApp):
    def build(self):
        return TouchDetector()

MyApp().run()
