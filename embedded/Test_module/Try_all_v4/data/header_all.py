##### Dependency #####
import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.logger import Logger
# import mysql.connector
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen




from login import *



Builder.load_file('login.kv')