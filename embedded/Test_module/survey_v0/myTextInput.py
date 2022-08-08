from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty

class limitedTextInput(TextInput):
    max_input_num = NumericProperty(0)
    def insert_text(self, substring, from_undo=False):
        if len(self.text)>=self.max_input_num and self.max_input_num > 0:
            substring=""
        TextInput.insert_text(self, substring, from_undo)