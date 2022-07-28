import kivy

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang import Builder

class loginApp(App):
    def build(self):
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        return Builder.load_file('login.kv')
    def forgetID(self):
        print("Please make a function-forgetID") # ID 찾기 버튼 클릭시 실행되는 것을 여기에 작성해 주세요
    def forgetPW(self):
        print("Please make a function-forgetPW") # PW 찾기 버튼 클릭시 실행되는 것을 여기에 작성해 주세요
    def loginbtn(self):
        print("Please make a function-Login button") # login 버튼 클릭시 실행되는 것을 여기에 작성해 주세요

if __name__=="__main__":
    loginApp().run()


