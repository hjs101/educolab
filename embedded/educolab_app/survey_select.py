from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image, AsyncImage
import requests, json
from myTextInput import limitedTextInput
from kivy.properties import NumericProperty,BooleanProperty
from myPopup import MyPopUp2, MyPopUp3
from kivy.clock import Clock

class Survey_Select_Screen(Screen):
    percent=NumericProperty(0.7)
    trigger=BooleanProperty(True)
    ##**# self.manager.survey_ans [자료형: dictionary][key: 문항 번호(string)][value: 설문조사 답안(list-객관식/string-주관식)]
    ##**# 3번 문항의 객관식 답안 예시{'3': [1,2,3]}
    ##**# survey_word.py에서도 같은 형식이라 중복되는 부분이 있습니다.

    def __init__(self, **kwargs):
        super(Survey_Select_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
        # Builder.load_file('survey_select.kv')
        self.key_color=[0/255, 176/255, 240/255,1]
        self.popup = MyPopUp2()
        self.popup2 = MyPopUp3()

    def my_callback(self,dt):
        self.trigger=True 
    
    def on_pre_enter(self):
        self.check_flag=True
        self.end_flag = False
        self.prob_num=self.manager.prob_num
        # with open("./login_info.json", 'r', encoding='utf-8') as file:
        #     data = json.load(file)
        #     self.acc_token = data["access"]
        self.res = requests.get(
            'https://i7c102.p.ssafy.io/api/survey/detail',
            params={'survey_num': self.manager.content_number},
            headers={'Authorization' : 'Bearer ' + self.manager.access_api()}
        )
        self.data_full = json.loads(self.res.text)
        self.result=[]

        ##**# 문제 표기
        self.ids.title.text=self.data_full[0]['survey_name']
        self.ids.prob.text ="<" + str(self.prob_num) + "번 문항>\n" + self.data_full[self.prob_num]['survey_question']
        temp_list = str(self.data_full[self.manager.prob_num]['multiple_bogi']).split('/')

        for i in range(5):
            self.ids['ex'+str(i+1)].text=temp_list[i]
        for i in range(5):
            self.ids['ans'+str(i+1)].group=str(self.prob_num)+'ans'
        

        # 이전 답변이 있다면 복구
        if self.data_full[self.prob_num]['id'] in self.manager.survey_ans:
            for num in  self.manager.survey_ans[self.data_full[self.prob_num]['id']]:
                self.ids['ans'+str(num)].active=True

        ##icons
        if self.prob_num==1: self.ids.before.source='./icon/None.png'
        else: self.ids.before.source='./icon/left_button.png'
        if self.prob_num==self.manager.max_prob_num: self.ids.after.source='./icon/None.png'
        else: self.ids.after.source='./icon/right_button.png'
        self.percent=len(self.manager.survey_ans)/self.manager.max_prob_num
        if self.percent==0: self.percent=0.00001
        self.ids.progress.text=f'{self.percent*100:.1f}%'


    def next_flag_setup(self, btn_direction): ##### list 옆 페이지로 넘어가는 self.next_flag 정의
        self.next_flag=1
        if btn_direction=="before" and self.prob_num==1:
            self.next_flag=0
        if btn_direction=="after" and self.prob_num==self.manager.max_prob_num:
            self.next_flag=0
        
        if btn_direction=="before" : self.manager.prob_num-=self.next_flag
        if btn_direction=="after" : self.manager.prob_num+=self.next_flag

    def next_page_setup(self):  # 옆 페이지로 넘어가는 페이지 정의
        if self.next_flag:
            ##**# 다음 페이지의 문항 번호 = self.manager.page_num (업데이트함)
            ##**# 다음 페이지의 문항 종류 = next_page_type (이거 정의해주세요)
            if self.data_full[self.manager.prob_num]['multiple_bogi'] == None: next_page_type = False
            else: next_page_type = True
            #페이지 이동
            if next_page_type: # 객관식 > 객관식
                if self.name=="Survey_select1": self.next_page="Survey_select2"
                else : self.next_page="Survey_select1"
            else: # 객관식 > 주관식
                self.next_page="Survey_word1"
        else:
            self.next_page=self.name

    def checkbox_click(self, instance, value, ans_num): # 체크박스 클릭시 결과를 넣어준다.
        if self.trigger==True:
            self.trigger=False    
            if self.check_flag:
                self.manager.survey_ans.pop(self.data_full[self.prob_num]['id'], None)

                if value==True:
                    self.result.append(ans_num)
                else:
                    self.result.remove(ans_num)
                
                self.result.sort()
                if len(self.result)!=0:
                    self.manager.survey_ans[self.data_full[self.prob_num]['id']]=self.result.copy()
                self.manager.survey_ans=dict(sorted(self.manager.survey_ans.items()))

                self.percent=len(self.manager.survey_ans)/self.manager.max_prob_num
                self.ids.progress.text=f'{self.percent*100:.1f}%'
                if self.percent == 1.0: self.end_flag = True
            Clock.schedule_once(self.my_callback,0.01)
        else:
            pass

    def toggle_btn(self, btn): # 체크박스 뿐 아니라 보기를 눌렀을 때 활성화 하기 위한 용도의 함수
        if self.trigger==True:
            self.trigger=False
            if self.ids[btn].active==True:
                self.ids[btn].active=False
            else:
                self.ids[btn].active=True
            Clock.schedule_once(self.my_callback,0.01)
        else:
            pass

    def onPopUp(self, btn_flag):
        if self.end_flag and btn_flag:
            self.popup2.ids.alert.text="설문이 완료되었습니다"
            self.popup2.open()
        else:
            self.popup.ids.alert.text="설문이 끝나지 않았습니다. 종료하시겠습니까?\n종료시 현재까지 진행된 내용은 저장하지 않습니다."
            self.popup.open()

    def on_leave(self):
        self.check_flag=False
        for i in range(5):
            self.ids['ans'+str(i+1)].active=False


class survey_test_App(App):
    def build(self):
        Builder.load_file('survey_select.kv')
        return Survey_Select_Screen()

if __name__=="__main__":
    survey_test_App().run()