from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image, AsyncImage
<<<<<<< HEAD
import requests, json
=======
import requests
>>>>>>> 207a577 (Refactor : v4_backup 추가)
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
<<<<<<< HEAD
        # Builder.load_file('main_page.kv')

    def on_pre_enter(self):
        ##### 여기 문구를 수정해주세요 #####
        with open("./login_info.json", 'r') as file:
            # 학생정보 db 받아오기
            self.data = json.load(file)
            self.query1 = 'select name from accounts_schoolinfo where code=%s'
            self.args1 = (self.data["schoolcode"], )
            self.cur1 = self.manager.DB.execute(query=self.query1, args=self.args1)
            for (name, ) in self.cur1:
                self.school_name = name + ' '
            self.query2 = 'select grade, class_field, name, plus_point, minus_point from accounts_userinfo where email=%s and name=%s'
            self.args2 = (self.data["email"], self.data["name"])
            self.cur2 = self.manager.DB.execute(query=self.query2, args=self.args2)
            for (grade, class_field, name, plus_point, minus_point) in self.cur2:
                self.student_name = name
                self.grade = str(grade) + '학년 '
                self.class_field = str(class_field) + '반 '
                self.plus_point = str(plus_point)
                self.minus_point = str(minus_point)

        # 적용
        self.ids.userinfo.text=self.school_name + self.grade + self.class_field + self.student_name
        self.ids.good_points.text="상점: " + self.plus_point
        self.ids.bad_points.text="벌점: " + self.minus_point

        self.ids.challenge.text="최초로 퀴즈를 1등한 자"
=======
        Builder.load_file('main_page.kv')

    def on_pre_enter(self):
        ##### 여기 문구를 수정해주세요 #####
        self.ids.userinfo.text="싸피중학교 3학년 1반 24번 OOO"
        self.ids.challenge.text="최초로 퀴즈를 1등한 자"
        self.ids.good_points.text="상점 :1201"
        self.ids.bad_points.text="벌점 : 316"
>>>>>>> 207a577 (Refactor : v4_backup 추가)
        self.ids.homework.text="과제 (4) | 08/22 : SSAFY 멀티캠퍼스 방문 후기 작성"
        self.ids.survey.text="설문 (5) | 08/22 : SSAFY 강의 만족도 조사"
        ##################################
        # 프로필 이미지는 아직 수정이 안됩니다.
        self.ids.profile.img_path='./profile.jpg' # profile in Computer
<<<<<<< HEAD
=======
        #icons
>>>>>>> 207a577 (Refactor : v4_backup 추가)
        self.ids.userinfo_icon.img_path='./icon/info.png'
        self.ids.challenge_icon.img_path='./icon/challenge.png'
        self.ids.good_points_icon.img_path='./icon/plus.png'
        self.ids.bad_points_icon.img_path='./icon/minus.png'
        self.ids.homework_icon.img_path='./icon/homework.png'
        self.ids.survey_icon.img_path='./icon/survey.png'

<<<<<<< HEAD
<<<<<<< HEAD
    def for_logout(self):
=======
=======
    def for_logout(self):
        pass
>>>>>>> 42a2e09 (Feat : 공지사항 상세 내용 추가)
    def go_notice(self):
        pass
    def go_memo(self):
        pass
    def go_quiz(self):
        pass
    def go_survey(self):
>>>>>>> 207a577 (Refactor : v4_backup 추가)
        pass

    def on_leave(self):
        self.manager.before_page=self.name
        
class main_test_App(App):
    def build(self):
        Builder.load_file('main_page.kv')
        return Main_Screen()

if __name__=="__main__":
    main_test_App().run()