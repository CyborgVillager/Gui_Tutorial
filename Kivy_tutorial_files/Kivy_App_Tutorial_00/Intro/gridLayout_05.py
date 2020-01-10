from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""
GridLayout:
    spacing: 20
    padding: 5
    cols:2
 #   rows:4
 #change size
#    size_hint_x:None
    Button:
        text:'Button_00'
        size_hint_x:None
        width:200
    Button:
        text:'Button_01'
    Button:
        text:'Button_02'
    Button:
        text:'Button_03'
    Button:
        text:'Button_04'
    Button:
        text:'Button_05'
    Button:
        text:'Button_06'
    Button:
        text:'Button_07'
    Button:
        text:'Button_08'
    Button:
        text:'Button_09'
        size_hint_x:None
        width:400
    Button:
        text:'Button_10'
    Button:
        text:'Button_11'
    Button:
        text:'Button_12'
    Button:
        text:'Button_13'
        size_hint_x:None
        width:200
    Button:
        text:'Button_14'
    Button:
        text:'Button_15'
    Button:
        text:'Button_16'
    Button:
        text:'Button_17'
    Button:
        text:'Button_18'
    Button:
        text:'Button_19'       
    Button:
        text:'Button_20'
"""))