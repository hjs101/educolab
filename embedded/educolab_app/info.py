from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image, AsyncImage
import requests
from myTextInput import limitedTextInput
from kivy.properties import ListProperty
from myPopup import MyPopUp
import json

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
## self.ID  = 입력받은 ID
## self.PW  = 입력받은 ID

>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)
=======
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)
=======
>>>>>>> d61ea9f (fix: embedded update)
class Info_Screen(Screen):
    key_color=ListProperty([1,1,1,1])
    def __init__(self, **kwargs):
        super(Info_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

    def on_pre_enter(self):
=======
        # Builder.load_file('info.kv')

    def on_pre_enter(self):
        # self.page_pk = self.manager.get_screen('Notice_list1').content_num
        ##**# Notice_list1, Notice_list2에서 오는 두 가지 경우를 다 따지는 방식
<<<<<<< HEAD
        self.page_pk = self.manager.get_screen(self.manager.before_page).content_num

>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)
=======
        self.page_pk = self.manager.get_screen(self.manager.before_page).content_number
>>>>>>> 1a93471 (Style: API 수정)
=======

    def on_pre_enter(self):
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)
=======

    def on_pre_enter(self):
>>>>>>> d61ea9f (fix: embedded update)
        with open("./login_info.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.acc_token = data["access"]
        if 'Notice' in self.name:
            self.key_color=[151/255, 71/255, 255/255,1]
            self.notice_detail()
        ##**# 다른 곳에서 Info_Screen 형식을 쓸지 잘 모르겠어요
        # if 'Memo' in self.name:
        #     self.key_color=[198/255, 128/255, 62/255,1]
        #     self.memo_detail()
        # if 'Quiz' in self.name:
        #     self.key_color=[77/255, 166/255, 96/255,1]
        #     self.quiz_detail()
        # if 'Survey' in self.name:
        #     self.key_color=[0/255, 176/255, 240/255,1]
        #     self.survey_detail()


    def notice_detail(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        res = requests.get('https://i7c102.p.ssafy.io/api/notice/detail', params={'notice_num': self.manager.content_number}, headers={'Authorization' : 'Bearer ' + self.acc_token})
=======
        res = requests.get('http://127.0.0.1:8000/notice/detail', params={'notice_num': self.page_pk}, headers={'Authorization' : 'Bearer ' + self.acc_token})
>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)
=======
        print(self.page_pk)
        res = requests.get('https://i7c102.p.ssafy.io/api/notice/detail', params={'notice_num': self.page_pk}, headers={'Authorization' : 'Bearer ' + self.acc_token})
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1a93471 (Style: API 수정)
=======
        # print(json.loads(res))
>>>>>>> 31e39c9 (Fix : 목록 화면 분기 조정)
=======
        # print(res.text)
>>>>>>> 76eca37 (Fix : 공지사항 상세페이지 연결 오류 해결)
=======
        res = requests.get('https://i7c102.p.ssafy.io/api/notice/detail', params={'notice_num': self.manager.content_number}, headers={'Authorization' : 'Bearer ' + self.acc_token})
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)
=======
        res = requests.get('https://i7c102.p.ssafy.io/api/notice/detail', params={'notice_num': self.manager.content_number}, headers={'Authorization' : 'Bearer ' + self.acc_token})
>>>>>>> d61ea9f (fix: embedded update)
        data = json.loads(res.text)['notice']
        self.ids.title.text=data['title']
        temp = str(data['updated_at']).split('T')
        self.ids.info.text="작성자: " + data['teacher']['name'] + " | 작성날짜: " + temp[0] + " | 조회수: " + str(data['views'])
        self.ids.content.text=data['content']

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    ##**# 다른 곳에서 Info_Screen 형식을 쓸지 잘 모르겠어요
    # def memo_detail(self):
    #     pass
    # def quiz_detail(self):
    #     pass
    # def survey_detail(self):
    #     pass

>>>>>>> bb0c570 (Feat : 설문조사 화면 추가)
=======
>>>>>>> c2b1e4f (Feat: 각종 게시물 리스트 구현 완)
=======
>>>>>>> d61ea9f (fix: embedded update)
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