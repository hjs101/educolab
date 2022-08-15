from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image, AsyncImage
import requests, json
from myTextInput import limitedTextInput
from kivy.properties import StringProperty
from myPopup import MyPopUp

class Main_Screen(Screen):
    def __init__(self, **kwargs):
        super(Main_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
        self.emblem = ""

    def on_pre_enter(self):
        self.manager.quiz_flag = False
        self.manager.access_quiz("", "")
        with open("./login_info.json", 'r') as file:
            self.data = json.load(file)
        self.school_name = self.data["schoolname"] + ' '
        self.query1 = '''
            select username, grade, class_field, name, plus_point, minus_point 
            from accounts_userinfo where username=%s and name=%s
        '''
        self.args1 = (self.data["username"], self.data["name"])
        self.cur1 = self.manager.DB.execute(query=self.query1, args=self.args1)
        for (username, grade, class_field, name, plus_point, minus_point) in self.cur1:
            self.manager.userID = username
            self.student_name = name
            self.grade = str(grade) + '학년 '
            self.class_field = str(class_field) + '반 '
            self.plus_point = str(plus_point)
            self.minus_point = str(minus_point)

        self.res = requests.get(
            'https://i7c102.p.ssafy.io/api/survey/main_stu',
            headers={'Authorization' : 'Bearer ' + self.manager.access_api()}
        )
        self.survey_full = json.loads(self.res.text)
        self.survey_cnt = len(self.survey_full)
        self.current_survey = self.survey_full[0]['title']

        self.query2 = '''
            select title from pointshop_ptitle 
            inner join accounts_userinfo 
            on pointshop_ptitle.id=accounts_userinfo.wear_title_id 
            where accounts_userinfo.username=%s
        '''
        self.args2 = (self.manager.userID, )
        self.cur2 = self.manager.DB.execute(query=self.query2, args=self.args2)
        for (title, ) in self.cur2: self.emblem = title

        # 적용
        self.ids.userinfo.text=self.school_name + self.grade + self.class_field + self.student_name
        self.ids.good_points.text="상점: " + self.plus_point
        self.ids.bad_points.text="벌점: " + self.minus_point

        self.ids.challenge.text=self.emblem
        self.ids.survey.text="설문 (" + str(self.survey_cnt) + ") | " + self.current_survey

        self.ids.profile.img_path='./icon/profile.jpg' # profile in Computer
        self.ids.userinfo_icon.img_path='./icon/info.png'
        self.ids.challenge_icon.source='./icon/challenge.png'
        self.ids.good_points_icon.img_path='./icon/plus.png'
        self.ids.bad_points_icon.img_path='./icon/minus.png'
        self.ids.survey_icon.img_path='./icon/survey.png'
        
    def for_logout(self):
        with open("./login_info.json", 'w', encoding='utf-8') as file:
            json.dump({}, file)
        self.manager.userID = ''

    def on_leave(self):
        self.manager.before_page=self.name
        
class main_test_App(App):
    def build(self):
        Builder.load_file('main_page.kv')
        return Main_Screen()

if __name__=="__main__":
    main_test_App().run()