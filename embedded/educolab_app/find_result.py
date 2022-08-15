from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from myTextInput import limitedTextInput
import requests


class Find_result(Screen):
    def __init__(self, **kwargs):
        super(Find_result, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
        # Builder.load_file('find_result.kv')
        # self.IDresult = ''
        
    def on_pre_enter(self):
        ##### change label #####
        self.next_page_slide="down"
        if(self.name=='ID_result'):
            self.IDresult = self.manager.get_screen('ID_email').username
            self.ids.title.text="Find ID"
            self.ids.sub_title.text= f'당신의 아이디는 {self.IDresult}입니다.'
            
        if(self.name=='PW_result'):
            self.ids.title.text="Find PW"
            self.ids.sub_title.text= f'비밀번호가 성공적으로 변경되었습니다.'
        ########################
        if(self.name=='main'):
            self.ids.title.text="Main"
            self.ids.sub_title.text= f'축하합니다! 메인화면에 접속하셨습니다.'
            self.next_page_slide="right"

    def on_leave(self):
        self.manager.before_page=self.name

class find_test_App(App):
    def build(self):
        Builder.load_file('find_result.kv')
        return Find_result()

if __name__=="__main__":
    find_test_App().run()


