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
<<<<<<< HEAD
from list_page import List_Screen
=======
>>>>>>> 210a2e8 (Feat : 메인화면 추가)

from find_result import Find_result
from find_renew import Find_renew
from data.db_init import db_proc


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.DB=db_proc()
        self.DB.create_db()
<<<<<<< HEAD
        self.before_page=''
        self.page_num=1 #list page_num
        self.max_page_num=5 #list max page_num
=======
>>>>>>> 210a2e8 (Feat : 메인화면 추가)

    def onStop(self): # 창 종료 버튼
        self.DB.db_close()
        App.get_running_app().stop()


class masterApp(App):
    def build(self):
        return Builder.load_file('main.kv')

if __name__ =='__main__':
    masterApp().run()