from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image, AsyncImage
import requests
from myTextInput import limitedTextInput
from kivy.properties import StringProperty
from myPopup import MyPopUp

## self.ID  = 입력받은 ID
## self.PW  = 입력받은 ID

class Main_Screen(Screen):
    def __init__(self, **kwargs):
        super(Main_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
        Builder.load_file('main_page.kv')
        self.ids.profile.img_path='./profile.jpg' # profile in Computer

        #icons
        self.ids.userinfo_icon.img_path='./icon/info.png'
        self.ids.challenge_icon.img_path='./icon/challenge.png'
        self.ids.good_points_icon.img_path='./icon/plus.png'
        self.ids.bad_points_icon.img_path='./icon/minus.png'
        self.ids.homework_icon.img_path='./icon/homework.png'
        self.ids.survey_icon.img_path='./icon/survey.png'
        


    def on_pre_enter(self):
        ##### 여기 문구를 수정해주세요 #####
        self.ids.userinfo.text="싸피중학교 3학년 1반 24번 OOO"
        self.ids.challenge.text="최초로 퀴즈를 1등한 자"
        self.ids.good_points.text="상점 :1201"
        self.ids.bad_points.text="벌점 : 316"
        self.ids.homework.text="과제 (4) | 08/22 : SSAFY 멀티캠퍼스 방문 후기 작성"
        self.ids.survey.text="설문 (5) | 08/22 : SSAFY 강의 만족도 조사"
        ##################################
        # 프로필 이미지는 아직 수정이 안됩니다.

        
class main_test_App(App):
    def build(self):
        Builder.load_file('main_page.kv')
        return Main_Screen()

if __name__=="__main__":
    main_test_App().run()