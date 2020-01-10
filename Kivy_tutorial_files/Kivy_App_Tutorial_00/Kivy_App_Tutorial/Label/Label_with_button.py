from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string("""
BoxLayout:
    orientation: 'vertical'
#    orientation:'horizontal'
    size_hint_y:None
    height:sp(120) #
    Label:
        text:'Hello'
    Button:
        text:'World!'

"""))