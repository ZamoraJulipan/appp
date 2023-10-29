from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.widget import Widget
from uiautomator import Device

KV = '''
<ui>:
    MDScreen:
        MDBoxLayout:
            MDRectangleFlatButton:
                text: 'empezar'
                on_release:
                    app.start_recording()
            
            MDRectangleFlatButton:
                text: 'terminar'
                on_release:
                    app.stop_recording()
        MDBoxLayout:
            MDLabel:
                id: label_final
                pos_hint: {'center_x':.5,'center_y':.5}
                text: ''
        MDBoxLayout:
            MDRectangleFlatButton:
                pos_hint: {'center_x':1.2,'center_y':.6}
                text: 'primer toque'
            MDRectangleFlatButton:
                pos_hint: {'center_x':.9,'center_y':.7}
                text: 'segundo toque'
'''

class Ui(ScreenManager):
    pass

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)
        self.touches = []
        self.recording = False  # Variable para indicar si se está grabando

    def on_touch_down(self, touch):
        if self.recording:
            print("Se detectó un toque")
            self.touches.append(("down", touch.pos))

    def on_touch_move(self, touch):
        if self.recording:
            print("Se detectó un movimiento")
            self.touches.append(("move", touch.pos))

    def on_touch_up(self, touch):
        if self.recording:
            print("Se levantó el dedo")
            self.touches.append(("up", touch.pos))


class TouchRecorderApp(MDApp):
    def build(self):
        self.recorder = Touch()
        Builder.load_string(KV)
        return Ui()

    def start_recording(self):
        print("Comenzando grabación...")
        self.recorder.recording = True
        self.recorder.touches = []  # Limpia los datos anteriores

    def stop_recording(self):
        print("Deteniendo grabación.")
        self.recorder.recording = False

        # Guarda los movimientos en un archivo al detener la grabación
        with open('movimientos.txt', 'w') as file:
            for action, pos in self.recorder.touches:
                file.write(f'{action}: {pos}\n')
        
        self.root.ids.label_final.text = 'Ya acabaron'

TouchRecorderApp().run()
