import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Gridku(GridLayout):
    def __init__(self, **kwargs):
        super(Gridku, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Input Nama: "))
        
        self.nama= TextInput(multiline=False)
        self.add_widget(self.nama)

        self.join = Button(text="Join Main", font_size=25)  
        self.add_widget(self.join)

        self.exit = Button(text="Exit", font_size=25)  
        self.add_widget(self.exit)


class clientApp(App):
    def build(self):
        return Gridku()

if __name__ == "__main__":
    clientApp().run()
