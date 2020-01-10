from kivy.lang import Builder
from kivy.base import runTouchApp

# 0.3 is the height 0.1 is the width
runTouchApp(Builder.load_string("""

BoxLayout:
    Button:
        text:'Button_00'
        size_hint_x: 0.5
    Button:
        text:'Button_01'
        size_hint_x: 0.6
    Button:
        text:'Button_02'
        size_hint_x: 0.4
    Button:
        text:'Button_03'
        size_hint_x: 1



"""))
