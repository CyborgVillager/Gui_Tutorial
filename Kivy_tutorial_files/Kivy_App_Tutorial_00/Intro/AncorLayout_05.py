from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""

AnchorLayout:
#Both Button_00 & 01 are on top of each other
#By making the size of 01 20% smaller than 00 you are able to see
#that both buttons are indeed in the center of the window/on top of each other
    anchor_x:'right'
#   anchor_x:'left'
    anchor_y:'top'
    Button:
        text:'Button_00'
        size_hint:0.5,0.5
    Button:
        text:'Button_01'
        size_hint:0.2,0.2
        


"""))