from fileinput import close
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
from quiz_wait import Quiz_Waiting_Screen
from quiz_count import Quiz_Count_Screen
from quiz_select import Quiz_Select_Screen
from quiz_result import Quiz_Result_Screen
from quiz_start import Quiz_Start_Screen
from change_title import Change_Title_Screen

from find_result import Find_result
from find_renew import Find_renew
from data.db_init import db_proc
from data.websocket_info import *
from threading import *
import requests, json, websocket


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

Builder.load_file('quiz_wait.kv')
Builder.load_file('quiz_count.kv')
Builder.load_file('quiz_select.kv')
Builder.load_file('quiz_result.kv')
Builder.load_file('quiz_start.kv')
Builder.load_file('change_title.kv')
###########################################


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.ws = ws_proc()
        self.DB=db_proc()
        self.DB.create_db()
        self.before_page=''
        self.userID = ''
        self.start_page_num=0   #list 시작 게시물 index
        self.page_num=1     #list 현재 페이지
        self.max_page_num=5 #list 최대 페이지
        self.prob_num=1     #현재 문항 번호
        self.max_prob_num=5 #최대 문항 번호
        self.survey_ans={}  #설문 답안
        self.survey_cnt=0   #설문에 답변한 문항 수
        self.content_number=0    #어떤 글?
        self.room_num=0
        self.quiz_flag = False

    def access_quiz(self, send_msg, cmd):
        if self.quiz_flag:
            if cmd == "connect":
                self.ws.connect_ws(self.room_num, send_msg)
            elif cmd == "receive":
                self.recv_data = self.ws.recv_data()
        else:
            self.ws.close_ws()
            
    def onStop(self): # 창 종료 버튼
        self.DB.db_close()
        self.ws.close_ws()
        App.get_running_app().stop()

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

        with open("./login_info.json", 'r', encoding='utf-8') as file:
            acc_token = json.load(file)["access"]
        self.res = requests.post(
            'https://i7c102.p.ssafy.io/api/survey/submit/',
            headers={'Authorization' : 'Bearer ' + acc_token},
            json=self.send_data
        )

class masterApp(App):
    def build(self):
        return Builder.load_file('main.kv')

if __name__ =='__main__':
    masterApp().run()