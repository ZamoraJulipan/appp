from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class FloatingApp(App):
    def build(self):
        self.create_floating_ui()

    def create_floating_ui(self):
        # Crea un diseño flotante
        float_layout = FloatLayout()

        # Crea un botón flotante
        floating_button = Button(
            text="Mi Botón Flotante",
            size_hint=(None, None),
            size=(180, 60),
            pos=(100, 100),
            background_color=get_color_from_hex('#3498db'),  # Color de fondo azul
            on_press=self.on_button_press
        )

        # Agrega el botón al diseño flotante
        float_layout.add_widget(floating_button)

        # Crea un diseño principal para la aplicación
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(Label(text="Mi Aplicación"))

        # Agrega el diseño flotante al diseño principal
        main_layout.add_widget(float_layout)

        return main_layout

    def on_button_press(self, instance):
        print("Botón Flotante Presionado")

if __name__ == '__main__':
    FloatingApp().run()