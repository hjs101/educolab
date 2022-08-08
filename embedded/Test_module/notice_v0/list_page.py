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

class List_Screen(Screen):
    key_color=ListProperty([1,1,1,1])
    def __init__(self, **kwargs):
        super(List_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
        Builder.load_file('list_page.kv')
        self.key_color=[151/255, 71/255, 255/255,1]

        ##icons
        self.ids.before2.img_path='./icon/left_double.png'
        self.ids.before1.img_path='./icon/None.png'
        self.ids.after1.img_path='./icon/right_single.png'
        self.ids.after2.img_path='./icon/right_double.png'


    def onStop(self): # 창 종료 버튼
        App.get_running_app().stop()
        
class list_test_App(App):
    def build(self):
        Builder.load_file('list_page.kv')
        return List_Screen()

if __name__=="__main__":
    list_test_App().run()