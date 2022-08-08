from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from kivy.clock import Clock
import requests


class Quiz_Select_Screen(Screen):
    angle=NumericProperty(0)
    def __init__(self, **kwargs):
        super(Quiz_Select_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
        ##### change label #####
        self.people_num =35
        self.ids.title.text="대기하세요"
        self.ids.sub_title.text= f'대기 인원 : {self.people_num}'
        self.ids.loading.source='./icon/Loading.png'
        self.event1=Clock.schedule_interval(self.update_image, 0.1)
        self.animate_flag=False

    def test(self):
        if self.animate_flag:
            self.animate_flag=False
            self.event1()
        else:
            self.animate_flag=True
            Clock.unschedule(self.event1)


    def update_image(self, dt):
        self.ids.img.angle-=30
        if self.ids.img.angle==-360: self.ids.img.angle=0

    def on_leave(self):
        self.manager.before_page=self.name

    def onStop(self): # 창 종료 버튼
        App.get_running_app().stop()


class quiz_test_App(App):
    def build(self):
        Builder.load_file('quiz_select.kv')
        return Quiz_Select_Screen()

if __name__=="__main__":
    quiz_test_App().run()
