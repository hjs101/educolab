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
        self.page_num=1     #list 현재 페이지
        self.max_page_num=5 #list 최대 페이지
        self.prob_num=1     #현재 문항 번호
        self.max_prob_num=5 #최대 문항 번호
        self.survey_ans={}  #설문 답안
        self.survey_cnt=0   #설문에 답변한 문항 수

    def onStop(self): # 창 종료 버튼
        self.DB.db_close()
        App.get_running_app().stop()

    def survey_save(self): ##**# 팝업 종료시 Yes를 누르면 이 함수 호출 후 > 팝업 종료 및 페이지 이동
        pass
    

class masterApp(App):
    def build(self):
        return Builder.load_file('main.kv')

if __name__ =='__main__':
    masterApp().run()