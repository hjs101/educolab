from ast import arg
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from myTextInput import limitedTextInput
from myPopup import MyPopUp
import json, asyncio
from data.websocket_info import ws_proc

class Quiz_Start_Screen(Screen):
    def __init__(self, **kwargs):
        super(Quiz_Start_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
        self.popup=MyPopUp()
        self.ws=ws_proc()

    def midBtn(self):
        self.midInput = self.ids.mid_input.text

    def onPopUp(self): # 팝업 및 다음 페이지 경로 지정
        if len(self.midInput)==8 and self.midInput.isdigit():
            self.send_sockmsg = {
                "message": "학생 입장",
                "id": self.manager.userID,
                "room_num": self.midInput
            }
            self.ws.connect_ws(self.midInput, self.send_sockmsg)
            self.data = self.ws.recv_data()
            self.ws.close_ws()

            if json.loads(self.data)["message"] == "방이 없네요":
                self.popup.ids.alert.text="방이 없네요"
                self.popup.open()
                self.next_page = self.name
            else:
                self.next_page = 'Quiz_wait'
        else:
            self.popup.ids.alert.text="방 번호는 8자리 숫자입니다."
            self.popup.open()
            self.next_page = self.name

    def on_leave(self): # 페이지 이동시 기존 입력값 지우기
        self.ids.mid_input.text=""
        self.manager.before_page=self.name
        

class quiz_test_App(App):
    def build(self):
        Builder.load_file('quiz_start.kv')
        return Quiz_Start_Screen()

if __name__=="__main__":
    quiz_test_App().run()