<<<<<<< HEAD
from audioop import reverse
=======
>>>>>>> a84fab8 (Refactor : 기능 및 화면 조정)
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image, AsyncImage
<<<<<<< HEAD
import requests, json
=======
import requests
>>>>>>> a84fab8 (Refactor : 기능 및 화면 조정)
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
<<<<<<< HEAD
=======
        # Builder.load_file('list_page.kv')
>>>>>>> a84fab8 (Refactor : 기능 및 화면 조정)
        self.next_page='main'
        self.page_num=0

    def on_pre_enter(self):
<<<<<<< HEAD
        ######## 여기 컨텐츠 받아와서 넣으셔야 합니다 #####
        for i in range(5):
            self.ids['num' + str(i+1)].text=''
            self.ids['writer'+str(i+1)].text=''
            self.ids['date'+str(i+1)].text=''
            self.ids['title'+str(i+1)].text=''
        #################################################
        ##### key_color and title #####
        with open("./login_info.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.acc_token = data["access"]
        if 'Notice' in self.name:
            self.key_color=[151/255, 71/255, 255/255,1]
            self.ids.main_title.text="공지사항"
            self.notice_list()
        if 'Memo' in self.name:
            self.key_color=[198/255, 128/255, 62/255,1]
            self.ids.main_title.text="필기노트"
            self.memo_list()
        if 'Quiz' in self.name:
            self.key_color=[77/255, 166/255, 96/255,1]
            self.ids.main_title.text="퀴즈"
            self.quiz_list()
        if 'Survey' in self.name:
            self.key_color=[0/255, 176/255, 240/255,1]
            self.ids.main_title.text="설문조사"
            self.survey_list()

        self.ids.middle.text=str(self.manager.page_num)
=======
        ##### key_color and title #####
        if 'Notice' in self.name:
            self.key_color=[151/255, 71/255, 255/255,1]
            self.ids.main_title.text="공지사항"
        if 'Memo' in self.name:
            self.key_color=[198/255, 128/255, 62/255,1]
            self.ids.main_title.text="필기노트"
        if 'Quiz' in self.name:
            self.key_color=[77/255, 166/255, 96/255,1]
            self.ids.main_title.text="퀴즈"
        if 'Survey' in self.name:
            self.key_color=[0/255, 176/255, 240/255,1]
            self.ids.main_title.text="설문조사"

        ######## 여기 컨텐츠 받아와서 넣으셔야 합니다 #####
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
        #################################################
        self.ids.middle.text=str(self.manager.page_num)
        
>>>>>>> a84fab8 (Refactor : 기능 및 화면 조정)

        ##icons
        if self.manager.page_num==1:
            self.ids.before2.source='./icon/None.png'
            self.ids.before1.source='./icon/None.png'
        else:
            self.ids.before2.source='./icon/left_double.png'
            self.ids.before1.source='./icon/left_single.png'
        
        if self.manager.page_num==self.manager.max_page_num:
            self.ids.after1.source='./icon/None.png'
            self.ids.after2.source='./icon/None.png'
        else:
            self.ids.after1.source='./icon/right_single.png'
            self.ids.after2.source='./icon/right_double.png'

<<<<<<< HEAD
    def notice_list(self):
        res = requests.get('http://127.0.0.1:8000/notice/main', headers={'Authorization' : 'Bearer ' + self.acc_token})
        data_full = json.loads(res.text)
        data_full.sort(key=lambda x: -x['pk'])
        i = 1
        for data in data_full:
            for key in data:
                if key=='pk': self.ids['num' + str(i)].text = str(data[key])
                elif key=='teacher': self.ids['writer' + str(i)].text = str(data[key]['name'])
                elif key=='updated_at':
                    temp = str(data[key]).split('T')
                    self.ids['date' + str(i)].text = str(temp[0])
                elif key=='title': self.ids['title' + str(i)].text = str(data[key])
            i += 1
        self.manager.max_page_num = int(i / 5) + 1
    def memo_list(self):
        pass
    def quiz_list(self):
        pass
    def survey_list(self):
        pass

=======
>>>>>>> a84fab8 (Refactor : 기능 및 화면 조정)
    def content_btn(self, content_num): ##### 각각의 게시물을 들어갈때 들어가는 페이지 설정 
        if self.name=='Notice_list1' or self.name=='Notice_list2': self.content_page="Notice_info"
        else : self.content_page=self.name
        ##### 몇번째 게시물로 들어가는지 확인 #####
        ### Content_num : 1 ~ 5
        print("게시물 "+str(content_num)+"번")
<<<<<<< HEAD
        self.content_num = int(self.ids['num' + str(content_num)].text)
=======
>>>>>>> a84fab8 (Refactor : 기능 및 화면 조정)


    def page_num_reset(self): ##### main 페이지로 넘어갈때 
        self.manager.page_num=1

    def next_flag_setup(self, btn_direction): ##### list 옆 페이지로 넘어가는 flag 정의
        self.next_flag=1
        if btn_direction=="before" and self.manager.page_num==1:
            self.next_flag=0
        if btn_direction=="after" and self.manager.page_num==self.manager.max_page_num:
            self.next_flag=0
        
        if btn_direction=="before" : self.manager.page_num-=self.next_flag
        if btn_direction=="after" : self.manager.page_num+=self.next_flag

    def next_page_setup(self, page_hint):  ##### list 옆 페이지로 넘어가는 페이지 정의
        if self.next_flag:
            if self.manager.before_page=='main':
                if self.name=='Notice_list1': self.next_page='Notice_list2'
                if self.name=='Memo_list1': self.next_page='Memo_list2'
                if self.name=='Quiz_list1': self.next_page='Quiz_list2'
                if self.name=='Survey_list1': self.next_page='Survey_list2'

            else:
                if self.name=='Notice_list1': self.next_page='Notice_list2'
                if self.name=='Notice_list2': self.next_page='Notice_list1'
                if self.name=='Memo_list1': self.next_page='Memo_list2'
                if self.name=='Memo_list2': self.next_page='Memo_list1'
                if self.name=='Quiz_list1': self.next_page='Quiz_list2'
                if self.name=='Quiz_list2': self.next_page='Quiz_list1'
                if self.name=='Survey_list1': self.next_page='Survey_list2'
                if self.name=='Survey_list2': self.next_page='Survey_list1'
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