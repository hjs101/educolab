import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout): #base root widget : Grid Layout
    def __init__(self,**kwargs):
        super(LoginScreen,self).__init__(*kwargs) # override
        self.cols=2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False,font_name="./Jua-Regular.ttf") #한글 입력을 받는 방법
        self.add_widget(self.username)
        self.add_widget(Label(text='password',font_name="./Jua-Regular.ttf")) #한글 출력을 하는 방법
        self.password=TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
