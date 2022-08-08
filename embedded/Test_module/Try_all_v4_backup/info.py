from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image, AsyncImage
import requests
from myTextInput import limitedTextInput
from kivy.properties import ListProperty
from myPopup import MyPopUp

## self.ID  = 입력받은 ID
## self.PW  = 입력받은 ID

class Info_Screen(Screen):
    key_color=ListProperty([1,1,1,1])
    def __init__(self, **kwargs):
        super(Info_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
        # Builder.load_file('info.kv')

    def on_pre_enter(self):
        if 'Notice' in self.name:
            self.key_color=[151/255, 71/255, 255/255,1]
        if 'Memo' in self.name:
            self.key_color=[198/255, 128/255, 62/255,1]
        if 'Quiz' in self.name:
            self.key_color=[77/255, 166/255, 96/255,1]
        if 'Survey' in self.name:
            self.key_color=[0/255, 176/255, 240/255,1]

        self.ids.title.text="시험범위(국어)"
        self.ids.info.text="작성자 OOO | 작성날짜 2022.08.05. | 조회수 OOO"
        self.ids.content.text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

        # ##icons
        # self.ids.before2.img_path='./icon/left_double.png'
        # self.ids.before1.img_path='./icon/None.png'
        # self.ids.after1.img_path='./icon/right_single.png'
        # self.ids.after2.img_path='./icon/right_double.png'


    def on_leave(self):
        self.manager.before_page=self.name

    def onStop(self): # 창 종료 버튼
        App.get_running_app().stop()
        
class list_test_App(App):
    def build(self):
        Builder.load_file('info.kv')
        return Info_Screen()

if __name__=="__main__":
    list_test_App().run()