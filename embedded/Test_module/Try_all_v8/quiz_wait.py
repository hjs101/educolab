from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition
from kivy.properties import NumericProperty
from kivy.clock import Clock
from threading import Timer, Lock
import json, websocket, asyncio


class Quiz_Waiting_Screen(Screen):
    angle=NumericProperty(0)
    def __init__(self, **kwargs):
        super(Quiz_Waiting_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
    
    # async def connect(self):
    #     async with websockets.connect("ws://127.0.0.1:8000/api/ws/chat/" + str(self.room_number) + "/") as websocket:
    #         await websocket.send(json.dumps(send_dict))
    #         self.data = await websocket.recv()

    def on_pre_enter(self):
        ##### change label #####
        self.room_number=self.manager.get_screen("Quiz_list1").midInput
        self.people_num =35
        self.ids.title.text="대기하세요"
        self.ids.sub_title.text= f'방 번호 : {self.room_number}'
        self.ids.loading.source='./icon/Loading.png'
        self.event1=Clock.schedule_interval(self.update_image, 0.01)
        self.animate_flag=False
        self.cnt=0
        self.next_flag=0
        # self.send_msg = {
        #     "message": "학생 입장",
        #     "id": self.manager.userID,
        #     "room_num": self.room_number
        # }
        # self.manager.quiz_flag = True
        # self.manager.access_quiz(self.send_msg)
        
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
    
    def next(self): ##**# 임시로 화면 넘기는 버튼. Socket 구현시 삭제/조정 예정
        self.next_flag=1
    def next2(self): ##**# 임시로 화면 넘기는 버튼. Socket 구현시 삭제/조정 예정
        self.next_flag=-1

    def update_image(self, dt):
        ##**# 대기 인원 업데이트
        self.ids.sub_title.text= f'방 번호 : {self.room_number}'
        ##**# self.next_flag 신호 받으면 다음 화면 넘기는 flag
        ##**# socket 코딩하실 때 신호 받으면 self.next_flag 변환
        if self.next_flag > 0 : # 퀴즈로 넘어가기
            print(self.next_flag)
            Clock.unschedule(self.event1)
            self.manager.transition=NoTransition()
            # self.manager.transition.direction=NoTransition()
            self.manager.current="Quiz_count"
        if self.next_flag<0 : # 결과로 넘어가기
            Clock.unschedule(self.event1)
            self.manager.transition=NoTransition()
            # self.manager.transition.direction=NoTransition()
            self.manager.current="Quiz_result"               
        ####################################################

        self.cnt+=1
        if self.cnt==10:
            self.cnt=0
            self.ids.img.angle-=30
            if self.ids.img.angle==-360: self.ids.img.angle=0

    def on_pre_leave(self):
        Clock.unschedule(self.event1)
        
    def onStop(self): # 창 종료 버튼
        App.get_running_app().stop()


class quiz_test_App(App):
    def build(self):
        Builder.load_file('quiz_wait.kv')
        return Quiz_Waiting_Screen()

if __name__=="__main__":
    quiz_test_App().run()
