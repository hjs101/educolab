from ast import arg
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from myTextInput import limitedTextInput
from myPopup import MyPopUp

# self.midInput = 입력받은 텍스트

class Find_input1_button1(Screen):
    def __init__(self, **kwargs):
        super(Find_input1_button1, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True

        Builder.load_file('find_input1_button1.kv')
        self.popup=MyPopUp()

    def midBtn(self):
        self.midInput = self.ids.mid_input.text
        ##### self.next_flag가 정의되었다면 지워도 좋습니다.
        self.query = 'select name from accounts_userinfo where name=%s'
        self.args = (self.midInput, )
        self.cur = self.manager.DB.execute(query = self.query, args = self.args)

        self.next_flag = False
        for (name, ) in self.cur:
            self.next_flag = True
            break
        #################################################

    def onPopUp(self): # 팝업 및 다음 페이지 경로 지정
        if self.next_flag:
            self.next_page = "ID_email"
        else:
            self.popup.ids.alert.text="사용자를 찾을 수 없습니다"
            self.popup.open()
            self.next_page = self.name

        
    def on_leave(self): # 페이지 이동시 기존 입력값 지우기
        self.ids.mid_input.text=""
        

class find_test_App(App):
    def build(self):
        Builder.load_file('find_input1_button1.kv')
        return Find_input1_button1()

if __name__=="__main__":
    find_test_App().run()