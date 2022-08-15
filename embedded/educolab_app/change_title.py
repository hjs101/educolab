from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.properties import NumericProperty, ListProperty
from kivy.clock import Clock
import requests

class Temp_checkbox(CheckBox):
    ans_num=NumericProperty(0)
class Temp_button(Button):
    ans_num=NumericProperty(0)

class Change_Title_Screen(Screen):
    key_color=ListProperty([1,1,1,1])
    def __init__(self, **kwargs):
        super(Change_Title_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
    
    def on_pre_enter(self):
        ##### change label #####
        self.temp_check_list=[]
        self.temp_button_list=[]
        self.key_color=[77/255, 166/255, 96/255,1]
        self.multi = []
        self.now_title = ""
        self.rank=1

        ##**# 보기를 여기서 수정해주세요
        self.query1 = '''
            select title from pointshop_ptitle 
            inner join accounts_userinfo_own_title 
            on pointshop_ptitle.id=accounts_userinfo_own_title.ptitle_id 
            where accounts_userinfo_own_title.userinfo_id=%s
        '''
        self.args1 = (self.manager.userID, )
        self.cur1 = self.manager.DB.execute(query=self.query1, args=self.args1)
        for (title, ) in self.cur1: 
            self.multi.append(title)

        ##**# 현재 칭호를 여기로 세팅해주세요
        self.query2 = '''
            select title from pointshop_ptitle 
            inner join accounts_userinfo 
            on pointshop_ptitle.id=accounts_userinfo.wear_title_id 
            where accounts_userinfo.username=%s
        '''
        self.args2 = (self.manager.userID, )
        self.cur2 = self.manager.DB.execute(query=self.query2, args=self.args2)
        for (title, ) in self.cur2: self.now_title=title

        for i in range(len(self.multi)):
            if self.multi[i]==self.now_title:
                self.temp_check_list.append(Temp_checkbox(active=True,ans_num=i))
            else:
                self.temp_check_list.append(Temp_checkbox(ans_num=i))
            self.temp_button_list.append(Temp_button(text=self.multi[i],ans_num=i))
            self.ids.grid.add_widget(self.temp_check_list[i])
            self.ids.grid.add_widget(self.temp_button_list[i])
        self.result=[]
        self.result.append(self.now_title)


    def checkbox_click(self, instance, value, ans_num):
        if value==True:
            self.result.append(self.multi[ans_num])
        else:
            self.result.remove(self.multi[ans_num])
        print(self.result, ans_num)

    def save_title(self):
        query = '''
            update accounts_userinfo 
            inner join pointshop_ptitle on pointshop_ptitle.title=%s 
            set accounts_userinfo.wear_title_id=pointshop_ptitle.id 
            where accounts_userinfo.username=%s
        '''
        args = (self.result[0], self.manager.userID)
        cur = self.manager.DB.execute(query=query, args=args)
        self.manager.DB.db_commit()
        ##**# 여기서 타이틀 저장 기능 작성해주세면 됩니다.
        ##**# 타이틀은 self.result=["test3"] 이런식으로 저장되어 있습니다.

    def go_next(self):
        self.manager.transition=SlideTransition()
        self.manager.transition.direction='up'
        self.manager.current='main'


    def on_leave(self):
        for i in range(len(self.multi)):
            self.ids.grid.remove_widget(self.temp_check_list[i])
            self.ids.grid.remove_widget(self.temp_button_list[i])       
        self.manager.before_page=self.name

    def toggle_btn(self, ans_num):
        if self.temp_check_list[ans_num].active==True:
            self.temp_check_list[ans_num].active==False
        else:
            self.temp_check_list[ans_num].active=True


class quiz_test_App(App):
    def build(self):
        Builder.load_file('change_title.kv')
        return Change_Title_Screen()

if __name__=="__main__":
    quiz_test_App().run()
