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
        self.next_page='main'
        self.page_num=0

    def on_pre_enter(self):
        ##### key_color and title #####
        if 'Notice' in self.name:
            self.key_color=[151/255, 71/255, 255/255,1]
            self.ids.main_title.text="공지사항"
        if 'Memo' in self.name:
            self.key_color=[198/255, 128/255, 255/255,1]
            self.ids.main_title.text="필기노트"
        if 'Quiz' in self.name:
            self.key_color=[77/255, 166/255, 96/255,1]
            self.ids.main_title.text="퀴즈"
        if 'Survey' in self.name:
            self.key_color=[0/255, 176/255, 240/255,1]
            self.ids.main_title.text="설문조사"

        ##title
        self.ids.num1.text="번호 1"
        self.ids.title1.text=self.name
        self.ids.writer1.text="작성자 1"
        self.ids.date1.text="날짜 1"
        self.ids.num2.text="번호 2"
        self.ids.title2.text="제목 2"
        self.ids.writer2.text="작성자 2"
        self.ids.date2.text="날짜 2"
        self.ids.num3.text="번호 3"
        self.ids.title3.text="제목 3"
        self.ids.writer3.text="작성자 3"
        self.ids.date3.text="날짜 3"
        self.ids.num4.text="번호 4"
        self.ids.title4.text="제목 4"
        self.ids.writer4.text="작성자 4"
        self.ids.date4.text="날짜 4"
        self.ids.num5.text="번호 5"
        self.ids.title5.text="제목 5"
        self.ids.writer5.text="작성자 5"
        self.ids.date5.text="날짜 5"
        self.ids.middle.text=str(self.manager.page_num)

        ##icons
        if self.manager.page_num==1:
            self.ids.before2.source='./icon/None.png'
            self.ids.before1.source='./icon/None.png'
        else:
            self.ids.before2.source='./icon/left_double.png'
            self.ids.before1.source='./icon/left_double.png'
        
        if self.manager.page_num==self.manager.max_page_num:
            self.ids.after1.source='./icon/None.png'
            self.ids.after2.source='./icon/None.png'
        else:
            self.ids.after1.source='./icon/right_single.png'
            self.ids.after2.source='./icon/right_double.png'

    def page_num_reset(self):
        self.manager.page_num=1

    def next_flag_setup(self, btn_direction):
        self.next_flag=1
        if btn_direction=="before" and self.manager.page_num==1:
            self.next_flag=0
        if btn_direction=="after" and self.manager.page_num==self.manager.max_page_num:
            self.next_flag=0
        
        if btn_direction=="before" : self.manager.page_num-=self.next_flag
        if btn_direction=="after" : self.manager.page_num+=self.next_flag

    def next_page_setup(self, page_hint):
        if self.next_flag:
            if self.manager.before_page=='main':
                if self.name=='Notice_list1': self.next_page='Notice_list2'
                if self.name=='Memo_list1': self.next_page='Memo_list2'
                if self.name=='Quiz_list1': self.next_page='Quiz_list2'
                if self.name=='Survey_list1': self.next_page='Survey_list2'

            else:
                self.next_page=self.manager.before_page
            if page_hint=="start":self.manager.page_num=1
            if page_hint=="end": self.manager.page_num=self.manager.max_page_num
        else:
            self.next_page=self.name

    def on_leave(self):
        self.manager.before_page=self.name

        
class list_test_App(App):
    def build(self):
        Builder.load_file('list_page.kv')
        return List_Screen()

if __name__=="__main__":
    list_test_App().run()