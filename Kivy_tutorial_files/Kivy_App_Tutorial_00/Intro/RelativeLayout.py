from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""
RelativeLayout:
    Button:
        text:'Button_00'
        size_hint:.4,.4
#give only int values, DO NOT use %
        pos: 50, 100
    Button:
        text:'Button_01'
        size_hint:.3,.3
        pos: 160, 350
    Button:
        text:'Button_02'
        size_hint:.3,.3
        pos: 200, -3

"""))