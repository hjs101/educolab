from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition
from kivy.properties import NumericProperty
from kivy.clock import Clock
import requests


class Quiz_Count_Screen(Screen):
    def __init__(self, **kwargs):
        super(Quiz_Count_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
    
    def on_pre_enter(self):
        ##### change label #####
        self.count=3
        self.people_num =35
        self.ids.title.text=f'{self.count}'
        # self.ids.sub_title.text= f'대기 인원 : {self.people_num}'
        # self.ids.loading.source='./icon/Loading.png'
        self.event1=Clock.schedule_interval(self.update_count, 0.3)
        # self.animate_flag=False
        # self.cnt=0
        # self.next_flag=False
        
        ##**# socket 통신 초기화 및 입장 신호 작성 요청
        ##**# socket 통신 신호 받는 것은 Thread 이용해야 하는 것 같은 데... 잘 모르겠음

    ### event 참고자료
    # def test(self):
    #     if self.animate_flag:
    #         self.animate_flag=False
    #         self.event1()
    #     else:
    #         self.animate_flag=True
    #         Clock.unschedule(self.event1)

    # def next(self): ##**# 임시로 화면 넘기는 버튼. Socket 구현시 삭제/조정 예정
        # self.next_flag=True

    def update_count(self, dt):
        self.count-=1
        if self.count>0:
            self.ids.title.text=f'{self.count}'
        if self.count==0:
            self.ids.title.text=f'시작!'
        if self.count<0:
            Clock.unschedule(self.event1)
            self.manager.transition=NoTransition()
            # self.manager.transition.direction=NoTransition()
            self.manager.current="Quiz_select"

    def onStop(self): # 창 종료 버튼
        App.get_running_app().stop()


class quiz_test_App(App):
    def build(self):
        Builder.load_file('quiz_count.kv')
        return Quiz_Count_Screen()

if __name__=="__main__":
    quiz_test_App().run()
