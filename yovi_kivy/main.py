import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import *

# Multi Window
kivy.require('1.9.0') 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Window Classes
class WindowManager(ScreenManager):
    pass

class LoginWindow(Screen):

    def joinButton(self):
        print("IP : ", self.ip.text)
        print("Username : ", self.username.text)
        self.ip.text = ""
        self.username.text = ""
        
class LoadingWindow(Screen):
    pass

class MainWindow(Screen):
    pass

# Kv Builder
kv = Builder.load_file("login.kv")
kv = Builder.load_file("loading.kv")
kv = Builder.load_file("main.kv")

# Main Class
class BingoApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    BingoApp().run()

