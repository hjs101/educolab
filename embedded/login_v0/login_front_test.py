from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from myTextInput import limitedTextInput
import mysql.connector
import requests
import hashlib


class Login_Screen(Screen):
    def __init__(self, **kwargs):
        super(Login_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
        Builder.load_file('login_v3.kv')
        self.db_init()

    def db_init(self):
        self.db = mysql.connector.connect(
            host='13.125.213.119',
            user='educolab',
            password='educolab',
            database='educolab'
        )
        self.cur = self.db.cursor()

    def forgetID(self):
        self.ID=self.ids.ID_input.text
        if len(self.ID) == 0:
            print("Nothing ID")
        else:
            print(self.ID) 

    def forgetPW(self):
        self.PW=self.ids.PW_input.text       
        if len(self.PW) == 0:
            print("Nothing PW")
        else:
            print(self.PW) 

    def loginbtn(self):
        # 여기에는 여동준 부분
        # email 대신 password, 창 넘기는 거까지 구현해야 할 듯
        # password는 request module 써서 넘겨야 하는데 그건 테스트 해봐야 할 듯
        self.query = ("SELECT username, email FROM accounts_userinfo "
                        "where username=%s and email=%s")
        self.ID = self.ids.ID_input.text
        self.PW = self.ids.PW_input.text
        self.cur.execute(self.query, (self.ID, self.PW))

        if len(self.ID) == 0 or len(self.PW) == 0:
            print("Nothing ID or PW")
        else:
            self.success_flag = False
            for (username, email) in self.cur:
                if username == self.ID and email == self.PW:
                    self.success_flag = True
                    break
            if self.success_flag == True: print("성공!")
            else: print("실패!")

    def onStop(self):
        self.db.close()
        self.cur.close()
        App.get_running_app().stop()


class login_test_App(App):
    def build(self):
        Builder.load_file('login_v3.kv')
        return Login_Screen()

if __name__=="__main__":
    login_test_App().run()