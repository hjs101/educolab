from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition
from kivy.properties import NumericProperty
from kivy.clock import Clock
import requests


class Quiz_Select_Screen(Screen):
    def __init__(self, **kwargs):
        super(Quiz_Select_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
    
    def on_pre_enter(self):
        ##### change label #####
        self.quiz_prob_num=self.manager.prob_num
        self.ids.title.text=f'오늘 저녁 메뉴는 뭔가요? - {self.quiz_prob_num}번'
        self.cnt_time=5
        self.ids.time.text=f'잔여시간 : {self.cnt_time}초'

        self.event1=Clock.schedule_interval(self.update_count, 1)
        self.ans=-1

    def update_count(self, dt):
        self.cnt_time-=1
        if self.cnt_time>0:
            self.ids.time.text=f'잔여시간 : {self.cnt_time}초'
        if self.cnt_time==0:
            self.ids.time.text=f'잔여시간 : {self.cnt_time}초'
            Clock.unschedule(self.event1)
            self.manager.transition=NoTransition()
            self.manager.current="Quiz_wait"
    def button_click(self, ans):
        # self.ans=ans
        Clock.unschedule(self.event1)
        self.manager.transition=NoTransition()
        self.manager.current="Quiz_wait"
        ##**# Quiz 답변 socket 전송 : 답변=ans [int]
        ##########################
        print(ans)

    def onStop(self): # 창 종료 버튼
        App.get_running_app().stop()


class quiz_test_App(App):
    def build(self):
        Builder.load_file('quiz_select.kv')
        return Quiz_Select_Screen()

if __name__=="__main__":
    quiz_test_App().run()
