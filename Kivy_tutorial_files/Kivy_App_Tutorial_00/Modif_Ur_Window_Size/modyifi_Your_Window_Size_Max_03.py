from kivy.lang import Builder
from kivy.base import runTouchApp

# 0.3 is the height 0.1 is the width
runTouchApp(Builder.load_string("""
FloatLayout:
    Button:
        text: 'Button_00'
# By using 'None' it will take up the whole window screen, try it by uncommenting line 10!
#        size_hint_max_x: None
         size_hint_max_x: .3



"""))
