# ex01. Hello, World!

import kivy
kivy.require('2.1.0')

from kivy.app import App # base function class
from kivy.uix.label import Label # Module include UI(layout, widgets)

class MyApp(App): # basic screen
    def build(self): # initialize and return root widgets
        return Label(text='Hello world') # return instance == root widget

if __name__=='__main__':
    MyApp().run() # initialize and run. start kivy app.