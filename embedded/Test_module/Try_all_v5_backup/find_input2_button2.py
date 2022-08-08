from ast import arg
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from myTextInput import limitedTextInput
from myPopup import MyPopUp
import requests

# self.firstInput = 왼쪽에서 입력받은 텍스트
# self.secondInput = 오른쪽에서 입력받은 텍스트

class Find_input2_button2(Screen):
    def __init__(self, **kwargs):
        super(Find_input2_button2, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True

        # Builder.load_file('find_input2_button2.kv')
        self.popup=MyPopUp()
        # self.name_temp=''
        # self.username_temp=''

    def on_pre_enter(self):     
        # 화면 출력 내용 변환
        # 향후 find_input2_button2.json "config" 파일로 대체 예정 (정리)
        ##### change label #####
        self.ids.right_sub_title.text="인증번호"
        self.ids.left_btn.text="인증번호 받기"
        self.ids.right_btn.text="ID/PW 찾기"
        if(self.name=='ID_phone'):
            self.ids.title.text="Find ID"
            self.ids.left_sub_title.text="전화번호"
            ### next page path #####
            self.left_next_page_temp=self.name
            self.right_next_page_temp="ID_result"
            ########################
        if(self.name=='ID_email'):
            self.name_temp = self.manager.get_screen('ID_name').ids.mid_input.text
            self.ids.title.text="Find ID"
            self.ids.left_sub_title.text="E-mail"
            ### next page path #####
            self.left_next_page_temp=self.name
            self.right_next_page_temp="ID_result"
            ########################
        if(self.name=='PW_name'):
            self.ids.title.text="Find PW"
            self.ids.left_sub_title.text="이름"
            self.ids.right_sub_title.text="ID"
            self.ids.left_btn.text="E-mail로 인증"
            self.ids.right_btn.text="전화번호로 인증"
            ### next page path #####
            self.left_next_page_temp="PW_email"
            self.right_next_page_temp="PW_phone"
            ########################
        if(self.name=='PW_phone'):
            self.ids.title.text="Find PW"
            self.ids.left_sub_title.text="전화번호"
            ### next page path #####
            self.left_next_page_temp=self.name
            self.right_next_page_temp="PW_renew"
            ########################
        if(self.name=='PW_email'):
            self.name_temp = self.manager.get_screen('PW_name').ids.left_input.text
            self.username_temp = self.manager.get_screen('PW_name').ids.right_input.text
            self.ids.title.text="Find PW"
            self.ids.left_sub_title.text="E-mail"
            ### next page path #####
            self.left_next_page_temp=self.name
            self.right_next_page_temp="PW_renew"
            ########################
            
    def leftBtn(self):
        self.leftInput = self.ids.left_input.text
        self.rightInput = self.ids.right_input.text
    def rightBtn(self):
        self.leftInput = self.ids.left_input.text
        self.rightInput = self.ids.right_input.text


    def on_leave(self): # 페이지 이동시 기존 입력 값 지우기
        self.ids.left_input.text=""
        self.ids.right_input.text=""
        self.manager.before_page=self.name

    def left_onPopUp(self): # 왼쪽 버튼 클릭시 팝업 및 다음 페이지 경로 지정
        self.left_next_flag = False
        if(self.name=="PW_name"):
            self.query = 'select name, username from accounts_userinfo where name=%s and username=%s'
            self.args = (self.leftInput, self.rightInput)
            self.cur = self.manager.DB.execute(query=self.query, args=self.args)

            for (username, name) in self.cur:
                self.left_next_flag = True
                break
            if self.left_next_flag:
                self.left_next_page = self.left_next_page_temp
            else:
                self.popup.ids.alert.text = "사용자를\n찾을 수 없습니다"
                self.popup.open()
                self.left_next_page=self.name
        ######################################################
        else:
            if self.name == "ID_email":
                self.data = {
                    'name': self.name_temp,
                    'email': self.leftInput,
                }
                self.res = requests.post('http://127.0.0.1:8000/accounts/find_username/', data=self.data)
                if self.res.json()['success']: self.username = self.res.json()['username']
            elif self.name == "PW_email":
                self.data = {
                    'name': self.name_temp,
                    'email': self.leftInput,
                    'username': self.username_temp
                }
                self.res = requests.post('http://127.0.0.1:8000/accounts/send_pw_email/', data=self.data)
                # debug
                print(self.res.json()['auth_num'])
            if self.res.json()['success']: self.left_next_flag = True
        #######################################################
            if self.left_next_flag:
                self.popup.ids.alert.text="인증번호가\n정상적으로 발급되었습니다\n(ID 찾기의 경우 인증번호 생략)"
                self.popup.open()
                self.left_next_page=self.left_next_page_temp
            else:
                self.popup.ids.alert.text="다시 입력하여 주십시오"
                self.popup.open()
                self.left_next_page=self.name

    def right_onPopUp(self): # 오른쪽 버튼 클릭시 팝업 및 다음 페이지 경로 지정
        self.right_next_flag = False
        if self.name == "ID_email" and self.left_next_flag:
            self.right_next_flag = True
        elif self.name == "PW_email":
            if (self.res.json()['auth_num'] == self.rightInput) and self.left_next_flag:
                self.right_next_flag = True
    #######################################################
        if self.right_next_flag:
            if self.name == 'ID_email': self.right_next_page = "ID_result"
            elif self.name == 'PW_email': self.right_next_page = "PW_renew"
        else:
            self.popup.ids.alert.text="다시 입력하여 주십시오"
            self.popup.open()
            self.right_next_page=self.name

class find_test_App(App):
    def build(self):
        Builder.load_file('find_input2_button2.kv')
        return Find_input2_button2()

if __name__=="__main__":
    find_test_App().run()


