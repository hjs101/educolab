from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

from myTextInput import limitedTextInput

# self.leftInput = 입력받은 비밀번호

class Find_renew(Screen):
    def __init__(self, **kwargs):
        super(Find_renew, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
        Builder.load_file('find_renew.kv')

    def leftBtn(self):
        ##### 왼쪽 버튼 입력시 발동하는 함수
        self.leftInput=self.ids.left_input.text
        self.rightInput=self.ids.right_input.text

        ##### 비밀번호 일치 확인
        if(self.leftInput==self.rightInput and len(self.leftInput)>0): 
            self.next_page="PW_result"
            self.ids.right_info.text=""
        else:
            self.ids.right_info.text="비밀번호가\n일치하지 않습니다"
            self.next_page=self.name
        ###################################

        ##### 서버에 데이터 넣기


        ###################################

    def onStop(self): # 창 종료 버튼
        App.get_running_app().stop()
    def on_leave(self): # 페이지 이동시 기존 입력값 지우기
        self.ids.left_input.text=""
        self.ids.right_input.text=""
        self.ids.right_info_text=""

class find_test_App(App):
    def build(self):
        Builder.load_file('find_renew.kv')
        return Find_renew()

if __name__=="__main__":
    find_test_App().run()


