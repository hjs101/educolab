from kivy.config import Config
Config.set('kivy','keyboard_mode', 'systemandmulti')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from loading import Loading_Screen
from login import Login_Screen
from find_input1_button1 import Find_input1_button1
from find_input2_button2 import Find_input2_button2
from find_input2_button1 import Find_input2_button1
from main_page import Main_Screen
from list_page import List_Screen
from info import Info_Screen
from survey_select import Survey_Select_Screen
from survey_word import Survey_Word_Screen

from find_result import Find_result
from find_renew import Find_renew
from data.db_init import db_proc
<<<<<<< HEAD
<<<<<<< HEAD
import requests, json
=======
>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)
=======
import requests, json
>>>>>>> e2ab9d8 (Feat: 설문조사 상세기능 구현)

##### to remove warning message ######
Builder.load_file('loading.kv')
Builder.load_file('login.kv')
Builder.load_file('find_input1_button1.kv')
Builder.load_file('find_input2_button1.kv')
Builder.load_file('find_input2_button2.kv')
Builder.load_file('find_renew.kv')
Builder.load_file('find_result.kv')

Builder.load_file('myPopup.kv')

Builder.load_file('main_page.kv')
Builder.load_file('list_page.kv')
Builder.load_file('info.kv')

Builder.load_file('survey_select.kv')
Builder.load_file('survey_word.kv')
###########################################


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.DB=db_proc()
        self.DB.create_db()
        self.before_page=''
<<<<<<< HEAD
<<<<<<< HEAD
        self.start_page_num=0   #list 시작 게시물 index
=======
>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)
=======
        self.start_page_num=0   #list 시작 게시물 index
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)
        self.page_num=1     #list 현재 페이지
        self.max_page_num=5 #list 최대 페이지
        self.prob_num=1     #현재 문항 번호
        self.max_prob_num=5 #최대 문항 번호
        self.survey_ans={}  #설문 답안
        self.survey_cnt=0   #설문에 답변한 문항 수
<<<<<<< HEAD
<<<<<<< HEAD
        self.content_number=0    #어떤 글?
=======
>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)
=======
        self.content_number=0    #어떤 글?
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)

    def onStop(self): # 창 종료 버튼
        self.DB.db_close()
        App.get_running_app().stop()

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e2ab9d8 (Feat: 설문조사 상세기능 구현)
    def access_api(self):
        with open("./login_info.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data["access"]

    def survey_save(self):
        self.send_data = {}
        self.send_data.update({'survey_num': self.content_number})
        self.send_data.update({'answers': []})
        for ans in self.survey_ans:
            if len(self.survey_ans[ans]) == 1: 
                self.send_data['answers'].append({
                    'id': ans,
                    'answer': self.survey_ans[ans][0]
                })
            else:
                self.send_data['answers'].append({
                    'id': ans,
                    'answer': self.survey_ans[ans]
                })

        self.res = requests.post(
            'https://i7c102.p.ssafy.io/api/survey/submit/',
            headers={'Authorization' : 'Bearer ' + self.access_api()},
            data=self.send_data
        )
<<<<<<< HEAD
=======
    def survey_save(self): ##**# 팝업 종료시 Yes를 누르면 이 함수 호출 후 > 팝업 종료 및 페이지 이동
        pass
    
>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)
=======
>>>>>>> e2ab9d8 (Feat: 설문조사 상세기능 구현)

class masterApp(App):
    def build(self):
        return Builder.load_file('main.kv')

if __name__ =='__main__':
    masterApp().run()