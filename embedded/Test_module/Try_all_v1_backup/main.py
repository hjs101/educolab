from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from login import Login_Screen
from find_input1_button2 import Find_input1_button2
from find_input2_button2 import Find_input2_button2
from find_result import Find_result
from find_renew import Find_renew
from data.db_init import db_proc


class WindowManager(ScreenManager):
    pass

kv=Builder.load_file('main.kv')

class masterApp(App):
    def build(self):
        return kv

if __name__ =='__main__':
    masterApp().run()