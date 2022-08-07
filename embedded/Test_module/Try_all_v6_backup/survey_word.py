from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image, AsyncImage
import requests
from myTextInput import limitedTextInput
from kivy.properties import NumericProperty
from myPopup import MyPopUp2

## self.ID  = 입력받은 ID
## self.PW  = 입력받은 ID

class Survey_Word_Screen(Screen):
    ##**# self.manager.survey_ans [자료형: dictionary][key: 문항 번호(string)][value: 설문조사 답안(list-객관식/string-주관식)]
    ##**# 1번 문항의 주관식 답안 예시 {'1': "안녕하세요"}
    ##**# survey_select.py에서도 같은 형식이라 중복되는 부분이 있습니다.
    percent=NumericProperty(0.7)
    def __init__(self, **kwargs):
        super(Survey_Word_Screen, self).__init__(**kwargs)
        Window.top=50
        Window.left=10
        Window.clearcolor = (242/255,245/255,247/255,1)
        Window.size = (1280,720)
        Window.borderless=True
        # Builder.load_file('survey_select.kv')
        self.key_color=[0/255, 176/255, 240/255,1]
        self.popup = MyPopUp2()

    def on_pre_enter(self):
        # 초기화
        self.result=""
        self.prob_num=self.manager.prob_num

        ##**# 문제 표기
        self.ids.title.text="오늘 저녁 메뉴 선정 : "+str(self.prob_num)+"번"
        self.ids.prob.text="어제는 라면을 먹었고 오늘 점심에는 햇반을 먹었으며 오늘 저녁에는 치킨을 시켰다면 내일 점심으로 먹을 것은 무엇인가?"

        # 이전 답변이 있다면 복구
        if str(self.prob_num) in self.manager.survey_ans:
            self.ids.ans.text=self.manager.survey_ans[str(self.prob_num)]

        # ##icons
        ##icons
        if self.prob_num==1: self.ids.before.source='./icon/None.png'
        else: self.ids.before.source='./icon/left_button.png'
        if self.prob_num==self.manager.max_prob_num: self.ids.after.source='./icon/None.png'
        else: self.ids.after.source='./icon/right_button.png'
        self.percent=self.manager.survey_cnt/self.manager.max_prob_num
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
            # next_page_type = True  # 객관식
            next_page_type = False # 주관식
            #페이지 이동
            if next_page_type: # 주관식 > 객관식
                self.next_page="Survey_select1"
            else: # 주관식 > 주관식
                if self.name=="Survey_word1": self.next_page="Survey_word2"
                else : self.next_page="Survey_word1"
        else:
            self.next_page=self.name

    def cnt_setup(self): #정답을 낸 문항 개수를 즉시 반영하기 위한 함수
        self.result=self.ids.ans.text
        if len(self.result)==0: # 문항 답변 X
            if str(self.prob_num) in self.manager.survey_ans: self.manager.survey_cnt-=1 # 지운거
        else:
            if str(self.prob_num) not in self.manager.survey_ans: self.manager.survey_cnt+=1 # 추가한거

    def onPopUp(self):
        # 데이터 저장
        self.result=self.ids.ans.text
        self.cnt_setup()
        if len(self.result)!=0:
            self.manager.survey_ans[str(self.prob_num)]=self.result
        else:
            if str(self.prob_num) in self.manager.survey_ans: self.manager.survey_ans.pop(str(self.prob_num),None)

        # ##### 필수 설문이 완료되었는지 체크 : self.end_flag #####
        # self.end_flag=True  # 필수 설문 완료
        self.end_flag=False # 필수 설문 미완료
        #########################################################################
        if self.end_flag:
            self.popup.ids.alert.text="설문이 완료되었습니다. 종료하시겠습니까?\n설문 종료시 답변을 더 이상 수정할 수 없습니다"
            self.popup.open()
        else:
            self.popup.ids.alert.text="설문이 끝나지 않았습니다. 종료하시겠습니까?\n종료시 현재까지 진행된 내용은 저장하지 않습니다."
            self.popup.open()

    def on_pre_leave(self):
        # 데이터 저장
        self.result=self.ids.ans.text
        if len(self.result)!=0:
            self.manager.survey_ans[str(self.prob_num)]=self.result
        else:
            if str(self.prob_num) in self.manager.survey_ans: self.manager.survey_ans.pop(str(self.prob_num),None)
        self.ids.ans.text=""
        
class survey_test_App(App):
    def build(self):
        Builder.load_file('survey_word.kv')
        return Survey_Word_Screen()

if __name__=="__main__":
    survey_test_App().run()