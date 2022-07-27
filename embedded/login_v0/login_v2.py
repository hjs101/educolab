import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.logger import Logger
import mysql.connector

class loginApp(App):
    def __init__(self, **kwargs):
        super(loginApp, self).__init__(**kwargs)
        self.db = mysql.connector.connect(
            host='3.36.69.192',
            user='educolab',
            password='c102_edu',
            database='educolab'
        )
        self.cur = self.db.cursor()

    def build(self):
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        return Builder.load_file('login_v2.kv')
        
    def forgetID(self):
        print("forgotID page") # ID 찾기 버튼 클릭시 실행되는 것을 여기에 작성해 주세요
    def forgetPW(self):
        print("forgotPW page") # PW 찾기 버튼 클릭시 실행되는 것을 여기에 작성해 주세요
    def loginbtn(self):
        print(self.cur.execute(""))
    def onStop(self):
        self.cur.close()
        self.db.close()
        Logger.critical('Good Bye')
        ##window close
        App.get_running_app().stop()

if __name__=="__main__":
    loginApp().run()


