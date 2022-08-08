from ast import arg
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from myTextInput import limitedTextInput
from myPopup import MyPopUp
import requests

# self.firstInput = 왼쪽에서 입력받은 텍스트
# self.secondInput = 오른쪽에서 입력받은 텍스트

class Find_input2_button1(Screen):
    def __init__(self, **kwargs):
        super(Find_input2_button1, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True

        Builder.load_file('find_input2_button1.kv')
        self.popup=MyPopUp()

    def on_pre_enter(self):     
        # 화면 출력 내용 변환
        # 향후 find_input2_button2.json "config" 파일로 대체 예정 (정리)
        ##### change label #####
        if(self.name=='PW_name'):
            self.ids.title.text="Find PW"
            self.ids.left_sub_title.text="이름"
            self.ids.right_sub_title.text="ID"
            self.ids.mid_btn.text="E-mail로 인증"
            ### next page path #####
            self.next_page_temp="PW_email"
            ########################

    def midBtn(self):
        self.leftInput = self.ids.left_input.text
        self.rightInput = self.ids.right_input.text
        
        self.next_flag=False

        if(self.name=="PW_name"):
            self.query = 'select name, username from accounts_userinfo where name=%s and username=%s'
            self.args = (self.leftInput, self.rightInput)
            self.cur = self.manager.DB.execute(query=self.query, args=self.args)

            for (username, name) in self.cur:
                self.next_flag = True
                break


    def on_leave(self): # 페이지 이동시 기존 입력 값 지우기
        self.ids.left_input.text=""
        self.ids.right_input.text=""
        self.manager.before_page=self.name

    def onPopUp(self): # 왼쪽 버튼 클릭시 팝업 및 다음 페이지 경로 지정
        if self.next_flag:
            self.next_page = self.next_page_temp
        else:
            self.popup.ids.alert.text = "사용자를\n찾을 수 없습니다"
            self.popup.open()
            self.next_page=self.name

class find_test_App(App):
    def build(self):
        Builder.load_file('find_input2_button2.kv')
        return Find_input2_button1()

if __name__=="__main__":
    find_test_App().run()


