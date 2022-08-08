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
    # progress_all:0.8*root.width
    # progress_set:self.progress_all*self.percent
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
        a=23
        b=3
        # ##icons
        self.ids.before.source='./icon/left_button.png'
        self.ids.after.source='./icon/right_button.png'
        self.percent=b/a
        self.ids.progress.text=f'{self.percent*100:.1f}%'
        self.result=[]
        ##### 필수 설문에서 중복 가능 : self.several_flag #####
        self.several_flag=True ##  중복 가능
        # self.several_flag=False ## 중복 불가능
        ######################################################
        ##### 필수 설문이 완료되었는지 체크 : self.end_flag #####
        self.end_flag=True ##  필수 설문 끝나따
        # self.end_flag=False ##
        ######################################################

        # if self.several_flag:
        #     for i in range(5):
        #         self.ids['ans'+str(i+1)].group='ans'+str(i+1)
        # else:
        #     for i in range(5):
        #         self.ids['ans'+str(i+1)].group='ans'
        
        # ####### 임시로 보기 데이터 넣기 ######
        # temp_list=["샤브샤브", "함박 스테이크", "민트초코", "파인애플 피자", "파스타"]

        # for i in range(5):
        #     self.ids['ex'+str(i+1)].text=temp_list[i]

    #     #list sort
    #     self.result.sort()

    # def checkbox_click(self, instance, value, ans_num): ## 체크박스 클릭시 결과를 넣어준다.
    #     if value==True:
    #         self.result.append(ans_num)
    #     else:
    #         self.result.remove(ans_num)

    # def toggle_btn(self, btn): # 체크박스 뿐 아니라 보기를 눌렀을 때 활성화 하기 위한 용도의 함수
    #     if self.ids[btn].active==True:
    #         self.ids[btn].active=False
    #     else:
    #         self.ids[btn].active=True

    def onPopUp(self):
        if self.end_flag:
            self.popup.ids.alert.text="설문이 완료되었습니다. 종료하시겠습니까?\n설문 종료시 답변을 더 이상 수정할 수 없습니다"
            self.popup.open()
        else:
            self.popup.ids.alert.text="설문이 끝나지 않았습니다. 종료하시겠습니까?\n종료시 현재까지 진행된 내용은 저장하지 않습니다."
            self.popup.open()

    def checkPopup(self):
        print(self.popup.sig)



    def onStop(self): # 창 종료 버튼
        App.get_running_app().stop()
        
class list_test_App(App):
    def build(self):
        Builder.load_file('survey_word.kv')
        return Survey_Word_Screen()

if __name__=="__main__":
    list_test_App().run()