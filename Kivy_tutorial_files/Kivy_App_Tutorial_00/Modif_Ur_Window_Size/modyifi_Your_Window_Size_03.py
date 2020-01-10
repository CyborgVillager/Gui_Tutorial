from kivy.lang import Builder
from kivy.base import runTouchApp

#0.3 is the height 0.1 is the width
runTouchApp(Builder.load_string("""
FloatLayout:
    Button:
        text: 'Button_00'
#        size_hint: x, y   <-order of placement
#        size_hint: 0.1,0.3
#        size_hint: 0.7,0.8
#You could also do this for making x & y values
        size_hint_x: .9
        size_hint_y: .2
        


"""))
