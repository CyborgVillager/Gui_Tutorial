#LR = left to right
#RL = right to left
#TB = top to bottom
#BT = bottom to top
from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""

StackLayout:
 #   orientation: 'rl-bt'
    orientation: 'rl-tb'
    padding: 20
    spacing: 10
    Button:
        text:'Button_00'
        size_hint:.2,.2
    Button:
        text:'Button_01'
        size_hint:.2,.2
    Button:
        text:'Button_03'
        size_hint:.2,.2
    Button:
        text:'Button_04'
        size_hint:.2,.2


"""))
