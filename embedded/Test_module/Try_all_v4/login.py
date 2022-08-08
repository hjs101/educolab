from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from pymysql import NULL
import requests
from myTextInput import limitedTextInput
from myPopup import MyPopUp
import json

## self.ID  = 입력받은 ID
## self.PW  = 입력받은 ID

class Login_Screen(Screen):
    def __init__(self, **kwargs):
        super(Login_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
        Builder.load_file('login.kv')
        self.popup = MyPopUp()

    def loginbtn(self):
        self.ID = self.ids.ID_input.text
        self.PW = self.ids.PW_input.text

        self.data = {
            'username': self.ID,
            'password': self.PW,
        }

        self.res = requests.post('http://127.0.0.1:8000/accounts/login/', data=self.data)

        if len(self.ID) == 0 or len(self.PW) == 0 or self.res.status_code == 401:
            self.next_flag = 0 ## 현재 페이지 유지 + 팝업
        else: 
            self.next_flag = 1 ## 다음 페이지 이동

    def onPopUp(self):
        if self.next_flag:
            self.login_next_page="main"
            with open("./login_info.json", 'w', encoding='utf-8') as file:
                json.dump(self.res.json(), file)
        else:
            self.popup.ids.alert.text="아이디와 비밀번호를\n다시 확인하여 주십시오"
            self.popup.open()
            self.login_next_page=self.name

    def on_leave(self):
        self.ids.ID_input.text=""
        self.ids.PW_input.text=""
        self.manager.before_page=self.name

class login_test_App(App):
    def build(self):
        Builder.load_file('login.kv')
        return Login_Screen()

if __name__=="__main__":
    login_test_App().run()