from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""
#If your using BoxLayout, it will make your button into an elongated button either horizontal or vertical, depending on your settings
FloatLayout:


    Button:
        text: 'Button_00'
        size_hint: 0.2, 0.2
#        pos_hint: {'x': .2, 'y': .3}
#        pos_hint: {'x': .7, 'y': .5}
#        pos_hint: {'top': 1,  'lift': 1}
        pos_hint: {'down': 1,  'lift': 1}
#        pos_hint: {'down': 1,  'right': 1}

"""))