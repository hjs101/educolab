from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition, SlideTransition
import requests, json
from kivy.clock import Clock


## self.ID  = 입력받은 ID
## self.PW  = 입력받은 ID

class Loading_Screen(Screen):
    def __init__(self, **kwargs):
        super(Loading_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
        # Builder.load_file('loading.kv')

    def on_pre_enter(self):
        Clock.schedule_once(self.go_page,0)

    def go_page(self,dt):
        ######로그인 flag 정의 요청##########
        with open("./login_info.json", 'r') as file:
            ref_data = json.load(file)
        if ref_data.get('refresh')!=None:
            user_data = {}
            self.login_flag = True
            user_data.update({"refresh": ref_data['refresh']})
            res = requests.post(
                'https://i7c102.p.ssafy.io/api/accounts/login/refresh/',
                data=ref_data
            )
            user_data.update(res.json())
            with open("./login_info.json", 'w', encoding='utf-8') as file:
                json.dump(user_data, file)
        else: self.login_flag=False # login
        ####################################
        if self.login_flag:
            self.manager.transition=NoTransition()
            self.manager.current='main'
            self.manager.transition=SlideTransition()
        else:
            self.manager.transition=NoTransition()
            self.manager.current='login'
            self.manager.transition=SlideTransition()
    def on_leave(self):
        self.manager.before_page=self.name

class loading_test_App(App):
    def build(self):
        Builder.load_file('loading.kv')
        return Loading_Screen()

if __name__=="__main__":
    loading_test_App().run()