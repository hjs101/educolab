from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.logger import Logger
from time import sleep
from threading import Timer, Lock
import mysql.connector
import sys
import datetime

class myapp(BoxLayout):
    def __init__(self, **kwargs):
        super(myapp, self).__init__(**kwargs)
        self.padding = 250
        self.init()
        self.setting_btn()
        
    def init(self):
        self.db = mysql.connector.connect(host = '13.125.213.119', user = 'educolab', password = 'educolab', database = 'educolab', auth_plugin='mysql_native_password')
        self.cur = self.db.cursor()

    def setting_btn(self):
        btn = Button(text = 'print DB')
        btn.bind(on_press = self.print_DB)
        self.add_widget(btn)
        btn2 = Button(text = 'bye')
        btn2.bind(on_press = self.closeKivy)
        self.add_widget(btn2)

    def print_DB(self, obj):
        self.cur.execute("select username, email, name from accounts_userinfo")
        for (username, email, name) in self.cur:
            print("{} {} {}\n".format(username, email, name))
        self.db.commit()

    def closeKivy(self, obj):
        self.cur.close()
        self.db.close()
        App.get_running_app().stop()
        Window.close()

class SimpleKivy(App):
    def on_stop(self):
        Logger.critical('Good Bye')
    def build(self):
        return myapp()
    
if __name__=='__main__':
    SimpleKivy().run()