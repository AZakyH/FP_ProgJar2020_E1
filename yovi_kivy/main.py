import kivy
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import *
from kivy.core.window import Window

# Multi Window
kivy.require('1.9.0') 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from kivy.properties import ListProperty, ObjectProperty
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse,Line)
from kivy.graphics.context_instructions import Color

from client import *
import threading  

################################################################### Window Manager
class WindowManager(ScreenManager):
    pass

################################################################### Login Window
class LoginWindow(Screen):

    def joinButton(self):
        print ("IP : ", self.ip.text)
        print ("Username : ", self.username.text)
        
        join(self.ip.text, self.username.text)

################################################################### Loading Window
class LoadingWindow(Screen):

    def on_enter(self):
        Clock.schedule_interval(self.update, 0.1)

    def update(self, dt):
        jumUser = getJumlahUser()
        self.jumlahUser.text = jumUser+' : 3'
        if jumUser == '3':
            self.manager.current = "maketable"

    def on_leave(self):
        Clock.unschedule(self.update)

################################################################### Make Table Window
class MaketableWindow(Screen):

    def __init__(self, **kwargs):
        return super(MaketableWindow, self).__init__(**kwargs)

    def table_done(self):
        sendTableDone()

    def on_touch_random(self):
        rand_table()

    def on_touch_box(self, str, holder, box):
        box_tmp = get_box()
        if(box_tmp is not None and box != box_tmp):
            box_tmp.opacity = 1

        if set_box(box, box.pos, holder.pos):
            box.opacity = 0.5
        else:
            box.pos = holder.pos
            box.opacity = 1

    def on_touch_holder(self, str, holder):
        box = get_box()
        if box is not None and holder.opacity == 0.01:
            box.pos = holder.pos
            makeTable(str, box.text)

################################################################### Loading Table Window
class LoadingtableWindow(Screen):

    def on_enter(self):
        Clock.schedule_interval(self.update, 0.1)

    def update(self, dt):
        jumUser = getJumlahTableDone()
        self.jumlahUser.text = jumUser+' : 3'
        if jumUser == '3':
            self.manager.current = "main"

    def on_leave(self):
        Clock.unschedule(self.update)

################################################################### Win Window
class WinWindow(Screen):

    def on_enter(self):
        Clock.schedule_interval(self.update, 4)

    def update(self, dt):
        self.manager.current = "maketable"

    def on_leave(self):
        sendTableReset()
        Clock.unschedule(self.update)

################################################################### Lose Window
class LoseWindow(Screen):

    def on_enter(self):
        Clock.schedule_interval(self.update, 4)

    def update(self, dt):
        self.manager.current = "maketable"

    def on_leave(self):
        sendTableReset()
        Clock.unschedule(self.update)

################################################################### Main Window
class MainWindow(Screen):

    def __init__(self, **kwargs):
        return super(MainWindow, self).__init__(**kwargs)

    def on_pre_enter(self):
        init_table()
        
        self.box_1.text = str(table[1][1])
        self.box_2.text = str(table[1][2])
        self.box_3.text = str(table[1][3])
        self.box_4.text = str(table[1][4])
        self.box_5.text = str(table[1][5])
        self.box_6.text = str(table[2][1])
        self.box_7.text = str(table[2][2])
        self.box_8.text = str(table[2][3])
        self.box_9.text = str(table[2][4])
        self.box_10.text = str(table[2][5])
        self.box_11.text = str(table[3][1])
        self.box_12.text = str(table[3][2])
        self.box_13.text = str(table[3][3])
        self.box_14.text = str(table[3][4])
        self.box_15.text = str(table[3][5])
        self.box_16.text = str(table[4][1])
        self.box_17.text = str(table[4][2])
        self.box_18.text = str(table[4][3])
        self.box_19.text = str(table[4][4])
        self.box_20.text = str(table[4][5])
        self.box_21.text = str(table[5][1])
        self.box_22.text = str(table[5][2])
        self.box_23.text = str(table[5][3])
        self.box_24.text = str(table[5][4])
        self.box_25.text = str(table[5][5])

        self.box_1.opacity = 1
        self.box_2.opacity = 1
        self.box_3.opacity = 1
        self.box_4.opacity = 1
        self.box_5.opacity = 1
        self.box_6.opacity = 1
        self.box_7.opacity = 1
        self.box_8.opacity = 1
        self.box_9.opacity = 1
        self.box_10.opacity = 1
        self.box_11.opacity = 1
        self.box_12.opacity = 1
        self.box_13.opacity = 1
        self.box_14.opacity = 1
        self.box_15.opacity = 1
        self.box_16.opacity = 1
        self.box_17.opacity = 1
        self.box_18.opacity = 1
        self.box_19.opacity = 1
        self.box_20.opacity = 1
        self.box_21.opacity = 1
        self.box_22.opacity = 1
        self.box_23.opacity = 1
        self.box_24.opacity = 1
        self.box_25.opacity = 1

        self.bingo_point.text = getBingoPoint()
        self.username.text = getUsername()
        self.turn.opacity = 0

    def on_enter(self):
        Clock.schedule_interval(self.update, 0.5)

    def update(self, dt):
        key = getKey()
        if key != "":
            self.turn.opacity = 1

        if getUpdateStatus():
            setUpdateStatus()
            box_name = getBoxName()
            sql = 'self.'+box_name+'.opacity = 0.5'
            exec(sql)

            str1 = getBoxVal()
            # print("STR : ", str1)
            if update_table(str1):
                setBingoPoint()
                sendBingo()
                self.manager.current = "win"
        
        if getGameOver():
            setGameOver()
            self.manager.current = "lose"

    def on_pre_leave(self):
        Clock.unschedule(self.update)

    def on_touch_box(self, str, box):
        key = getKey()
        # print("Key : ", key)
        if box.opacity != 0.5 and key != "" :
        # if box.opacity != 0.5 :
            box.opacity = 0.5
            sendNomor(box.text)
            self.turn.opacity = 0
            if update_table(box.text):
                sendBingo()
                setBingoPoint()
                self.manager.current = "win"
    
################################################################### Kv Builder
kv = Builder.load_file("login.kv")
kv = Builder.load_file("loading.kv")
kv = Builder.load_file("maketable.kv")
kv = Builder.load_file("loadingtable.kv")
kv = Builder.load_file("main.kv")
kv = Builder.load_file("win.kv")
kv = Builder.load_file("lose.kv")

################################################################### Main Class
class BingoApp(App):
    def build(self):
        Window.size = (800,600)
        return kv

if __name__ == "__main__":
    BingoApp().run()