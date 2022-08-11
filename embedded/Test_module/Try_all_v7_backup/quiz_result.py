from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.properties import ListProperty
from kivy.clock import Clock
import requests


class Quiz_Result_Screen(Screen):
    key_color=ListProperty([1,1,1,1])
    def __init__(self, **kwargs):
        super(Quiz_Result_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
    
    def on_pre_enter(self):
        ##### change label #####
        self.key_color=[77/255, 166/255, 96/255,1]
        self.rank=1
        self.ids.title.text=f'당신은 순위에 들지 못했습니다'
        self.ids.content.text=f'1번 : O\n2번 : O\n3번 : O\n4번 : X\n5번 : O\n6번 : O\n7번 : X\n8번 : X\n9번 : O\n10번 : X\n11번 : O'
        # self.ids.title.text=f'당신은 {self.rank}위 입니다'
        # self.ids.sub_title.text= f'대기 인원 : {self.people_num}'
        # self.ids.loading.source='./icon/Loading.png'
        # self.event1=Clock.schedule_interval(self.update_count, 0.3)
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

    def go_next(self):
        self.manager.transition=SlideTransition()
        self.manager.transition.direction='down'
        self.manager.current='main'


    def onStop(self): # 창 종료 버튼
        App.get_running_app().stop()


class quiz_test_App(App):
    def build(self):
        Builder.load_file('quiz_result.kv')
        return Quiz_Result_Screen()

if __name__=="__main__":
    quiz_test_App().run()
