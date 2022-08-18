from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, BooleanProperty
from kivy.clock import Clock


class limitedTextInput(TextInput):
    max_input_num = NumericProperty(0)
    trigger=BooleanProperty(True)

    def my_callback(self,dt):
        self.trigger=True

    def insert_text(self, substring, from_undo=False):
        if self.trigger==True:
            self.trigger=False
            Clock.schedule_once(self.my_callback,0.01)
        else:
            substring=""
        if len(self.text)>=self.max_input_num and self.max_input_num > 0:
            substring=""
        TextInput.insert_text(self, substring, from_undo)
