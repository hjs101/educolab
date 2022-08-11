from audioop import reverse
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image, AsyncImage
import requests, json
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
        self.next_page='main'
        self.page_num=0

    def on_pre_enter(self):
        # Contents reset
        for i in range(5):
            self.ids['num' + str(i+1)].text=''
            self.ids['writer'+str(i+1)].text=''
            self.ids['date'+str(i+1)].text=''
            self.ids['title'+str(i+1)].text=''

        # Screen Contents setting
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

        # icons
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

    def notice_list(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        res = requests.get('https://i7c102.p.ssafy.io/api/notice/main', headers={'Authorization' : 'Bearer ' + self.acc_token})
        data_full = json.loads(res.text)
        self.manager.max_page_num = int(len(data_full) / 5) + 1
<<<<<<< HEAD
        data_full.sort(key=lambda x: -x['pk'])
        i = 1

        for data in data_full[self.manager.start_page_num : self.manager.start_page_num + 5]:
=======
        res = requests.get('http://127.0.0.1:8000/notice/main', headers={'Authorization' : 'Bearer ' + self.acc_token})
=======
        res = requests.get('https://i7c102.p.ssafy.io/api/notice/main', headers={'Authorization' : 'Bearer ' + self.acc_token})
>>>>>>> 1a93471 (Style: API 수정)
        data_full = json.loads(res.text)
        data_full.sort(key=lambda x: -x['pk'])
        i = 1
        for data in data_full:
>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)
=======
        data_full.sort(key=lambda x: -x['pk'])
        i = 1

        for data in data_full[self.manager.start_page_num : self.manager.start_page_num + 5]:
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)
            for key in data:
                if key=='pk': self.ids['num' + str(i)].text = str(data[key])
                elif key=='teacher': self.ids['writer' + str(i)].text = str(data[key]['name'])
                elif key=='updated_at':
                    temp = str(data[key]).split('T')
                    self.ids['date' + str(i)].text = str(temp[0])
                elif key=='title': self.ids['title' + str(i)].text = str(data[key])
            i += 1
<<<<<<< HEAD
<<<<<<< HEAD
=======
        self.manager.max_page_num = int(i / 5) + 1
>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)

        ##**# 게시물이 5개 미만일때 정보 없는 버튼 비활성화 목적의 flag > 함수 content_btn으로 이어집니다.
        self.deact_flag=(i-1)%5
        if self.deact_flag==0: self.deact_flag=5

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if self.manager.page_num!=self.manager.max_page_num:
            self.deact_flag=5
=======
=======
        print(self.deact_flag)
        print(self.manager.max_page_num)        
=======
        if self.manager.page_num!=self.manager.max_page_num:
            self.deact_flag=5
>>>>>>> 76eca37 (Fix : 공지사항 상세페이지 연결 오류 해결)

>>>>>>> 31e39c9 (Fix : 목록 화면 분기 조정)


>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)

    def memo_list(self):
        pass
    def quiz_list(self):
        pass
    def survey_list(self):
<<<<<<< HEAD
        res = requests.get('https://i7c102.p.ssafy.io/api/survey/main_stu', headers={'Authorization' : 'Bearer ' + self.acc_token})
        data_full = json.loads(res.text)
        self.manager.max_page_num = int(len(data_full) / 5) + 1
=======
        res = requests.get('https://i7c102.p.ssafy.io/api/notice/main', headers={'Authorization' : 'Bearer ' + self.acc_token})
        data_full = json.loads(res.text)
        self.manager.max_page_num = int(len(data_full) / 5) + 1
>>>>>>> d61ea9f (fix: embedded update)
        data_full.sort(key=lambda x: -x['pk'])
        i = 1

        for data in data_full[self.manager.start_page_num : self.manager.start_page_num + 5]:
            for key in data:
                if key=='pk': self.ids['num' + str(i)].text = str(data[key])
                elif key=='teacher': self.ids['writer' + str(i)].text = str(data[key]['name'])
                elif key=='updated_at':
                    temp = str(data[key]).split('T')
                    self.ids['date' + str(i)].text = str(temp[0])
                elif key=='title': self.ids['title' + str(i)].text = str(data[key])
            i += 1
<<<<<<< HEAD
=======
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)
=======
>>>>>>> d61ea9f (fix: embedded update)

        ##**# 게시물이 5개 미만일때 정보 없는 버튼 비활성화 목적의 flag > 함수 content_btn으로 이어집니다.
        self.deact_flag=(i-1)%5
        if self.deact_flag==0: self.deact_flag=5

        if self.manager.page_num!=self.manager.max_page_num:
            self.deact_flag=5
<<<<<<< HEAD
<<<<<<< HEAD
=======
        pass
>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)
=======
=======
>>>>>>> d61ea9f (fix: embedded update)

    def memo_list(self):
        pass
    def quiz_list(self):
        pass
    def survey_list(self):
        res = requests.get('https://i7c102.p.ssafy.io/api/survey/main_stu', headers={'Authorization' : 'Bearer ' + self.acc_token})
        data_full = json.loads(res.text)
        self.manager.max_page_num = int(len(data_full) / 5) + 1
        data_full.sort(key=lambda x: -x['pk'])
        i = 1

        for data in data_full[self.manager.start_page_num : self.manager.start_page_num + 5]:
            for key in data:
                if key=='pk': self.ids['num' + str(i)].text = str(data[key])
                elif key=='teacher': self.ids['writer' + str(i)].text = str(data[key]['name'])
                elif key=='updated_at':
                    temp = str(data[key]).split('T')
                    self.ids['date' + str(i)].text = str(temp[0])
                elif key=='title': self.ids['title' + str(i)].text = str(data[key])
            i += 1

        ##**# 게시물이 5개 미만일때 정보 없는 버튼 비활성화 목적의 flag > 함수 content_btn으로 이어집니다.
        self.deact_flag=(i-1)%5
        if self.deact_flag==0: self.deact_flag=5

        if self.manager.page_num!=self.manager.max_page_num:
            self.deact_flag=5
<<<<<<< HEAD
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)
=======
>>>>>>> d61ea9f (fix: embedded update)
        ##**# self.deact_flag = 한 페이지에 나와있는 게시물 개수. 상세 내용은 notice_list를 참조해서 작성 요청
        ##**#                   게시물이 5개 미만일때 정보 없는 버튼 비활성화 목적의 flag > 함수 content_btn으로 이어집니다.


    def content_btn(self, content_num): # List에서 각각의 게시물 들어갈때 페이지 구분 
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e2ab9d8 (Feat: 설문조사 상세기능 구현)
=======
>>>>>>> d61ea9f (fix: embedded update)
        if content_num > self.deact_flag: self.content_page=self.name
        else:
            self.manager.content_number = int(self.ids['num' + str(content_num)].text)

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 76eca37 (Fix : 공지사항 상세페이지 연결 오류 해결)
=======
>>>>>>> e2ab9d8 (Feat: 설문조사 상세기능 구현)
=======
>>>>>>> d61ea9f (fix: embedded update)
        if self.name=='Notice_list1' or self.name=='Notice_list2': 
            if content_num>self.deact_flag:
                self.content_page=self.name
            else:
                self.content_page="Notice_info"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d61ea9f (fix: embedded update)
        elif self.name=='Survey_list1' or self.name=='Survey_list2':
            self.res = requests.get('https://i7c102.p.ssafy.io/api/survey/detail', params={'survey_num': self.manager.content_number}, headers={'Authorization' : 'Bearer ' + self.acc_token})
            self.temp_data = json.loads(self.res.text)
            self.manager.max_prob_num = len(self.temp_data) - 1
            if self.temp_data[self.manager.prob_num]['multiple_bogi'] == None:
                self.type_flag=False #주관식
            else: self.type_flag=True  #객관식

<<<<<<< HEAD
=======
        if self.name=='Notice_list1' or self.name=='Notice_list2': self.content_page="Notice_info"
=======
        ##### 임시: 나중에 뒤로 내릴 것 #######################################
            if content_num > self.deact_flag: self.content_page=self.name
            else:
                ##### 몇번째 게시물로 들어가는지 확인 #####
                ### Content_num : 1 ~ 5
                print("게시물 "+str(content_num)+"번")
                self.content_number = int(self.ids['num' + str(content_num)].text)
        #####################################################################
>>>>>>> 76eca37 (Fix : 공지사항 상세페이지 연결 오류 해결)
=======
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)
        elif self.name=='Survey_list1' or self.name=='Survey_list2':
<<<<<<< HEAD
            ##**# 설문조사 1번 문항 : 주관식? 객관식? type_flag
            self.type_flag=True  #객관식
            # self.type_flag=False #주관식
>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)
=======
            self.res = requests.get('https://i7c102.p.ssafy.io/api/survey/detail', params={'survey_num': self.manager.content_number}, headers={'Authorization' : 'Bearer ' + self.acc_token})
            self.temp_data = json.loads(self.res.text)
            self.manager.max_prob_num = len(self.temp_data) - 1
            if self.temp_data[self.manager.prob_num]['multiple_bogi'] == None:
                self.type_flag=False #주관식
            else: self.type_flag=True  #객관식

>>>>>>> e2ab9d8 (Feat: 설문조사 상세기능 구현)
=======
>>>>>>> d61ea9f (fix: embedded update)
            if self.type_flag:
                self.content_page="Survey_select1"
            else:
                self.content_page="Survey_word1"
            ##**# 설문조사 하나의 전체 문항개수 = self.manager.max_prob_num
            ##**# 설문조사 하나의 현재 문항개수 = self.manager.prob_num
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        else:
            self.content_page=self.name

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        if content_num > self.deact_flag: self.content_page=self.name
        else:
            self.manager.content_number = int(self.ids['num' + str(content_num)].text)
            if self.name=='Survey_list1' or self.name=='Survey_list2':
                res = requests.get('https://i7c102.p.ssafy.io/api/survey/detail', params={'survey_num': self.manager.content_number}, headers={'Authorization' : 'Bearer ' + self.acc_token})
                temp_data = json.loads(res.text)
                self.manager.max_prob_num = len(temp_data) - 1
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)
=======
>>>>>>> e2ab9d8 (Feat: 설문조사 상세기능 구현)
=======
        else:
            self.content_page=self.name

>>>>>>> d61ea9f (fix: embedded update)

        # self.content_number = content_num
        # print("now"+self.content_page)
        ##**# 데이터가 없어서 일단 화면 테스트를 목적으로 임시 주석
        ##**# 함수 survey_list에서 self.deact_flag 만들어 주시고 푸시면 정상 작동
        ##**# 게시물이 5개 미만일때 정보 없는 버튼 비활성화 목적의 flag 활용
<<<<<<< HEAD
=======

=======
>>>>>>> 1a93471 (Style: API 수정)
        else : self.content_page=self.name
=======
        else:
            self.content_page=self.name
>>>>>>> 31e39c9 (Fix : 목록 화면 분기 조정)

        self.content_number = content_num
        print("now"+self.content_page)
        ##**# 데이터가 없어서 일단 화면 테스트를 목적으로 임시 주석
        ##**# 함수 survey_list에서 self.deact_flag 만들어 주시고 푸시면 정상 작동
        ##**# 게시물이 5개 미만일때 정보 없는 버튼 비활성화 목적의 flag 활용
        # if content_num > self.deact_flag: self.content_page=self.name
        # else:
        #     ##### 몇번째 게시물로 들어가는지 확인 #####
        #     ### Content_num : 1 ~ 5
        #     print("게시물 "+str(content_num)+"번")
        #     self.content_num = int(self.ids['num' + str(content_num)].text)
>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)
=======
        # self.content_number = content_num
        # print("now"+self.content_page)
        ##**# 데이터가 없어서 일단 화면 테스트를 목적으로 임시 주석
        ##**# 함수 survey_list에서 self.deact_flag 만들어 주시고 푸시면 정상 작동
        ##**# 게시물이 5개 미만일때 정보 없는 버튼 비활성화 목적의 flag 활용
>>>>>>> 76eca37 (Fix : 공지사항 상세페이지 연결 오류 해결)
=======
>>>>>>> d61ea9f (fix: embedded update)


    def page_num_reset(self): ##### main 페이지로 넘어갈때 
        self.manager.page_num=1
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        self.manager.start_page_num=0
=======
>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)
=======
        self.manager.start_page_num=0
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)
=======
        self.manager.start_page_num=0
>>>>>>> d61ea9f (fix: embedded update)

    def next_flag_setup(self, btn_direction): ##### list 옆 페이지로 넘어가는 flag 정의
        self.next_flag=1
        if btn_direction=="before" and self.manager.page_num==1:
            self.next_flag=0
        if btn_direction=="after" and self.manager.page_num==self.manager.max_page_num:
            self.next_flag=0
        
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)
=======
>>>>>>> d61ea9f (fix: embedded update)
        if btn_direction=="before" :
            self.manager.page_num -= self.next_flag
            self.manager.start_page_num -= 5
        if btn_direction=="after" :
            self.manager.page_num += self.next_flag
            self.manager.start_page_num += 5
<<<<<<< HEAD
<<<<<<< HEAD
=======
        if btn_direction=="before" : self.manager.page_num-=self.next_flag
        if btn_direction=="after" : self.manager.page_num+=self.next_flag
>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)
=======
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)
=======
>>>>>>> d61ea9f (fix: embedded update)

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)
=======
>>>>>>> d61ea9f (fix: embedded update)
            if page_hint=="start":
                self.manager.page_num=1
                self.manager.start_page_num=0
            if page_hint=="end": 
                self.manager.page_num=self.manager.max_page_num
                self.manager.start_page_num = 5 * (self.manager.max_page_num - 1)
<<<<<<< HEAD
<<<<<<< HEAD
=======
            if page_hint=="start":self.manager.page_num=1
            if page_hint=="end": self.manager.page_num=self.manager.max_page_num
>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)
=======
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)
=======
>>>>>>> d61ea9f (fix: embedded update)
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