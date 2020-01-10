from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""
Label:
    Button:
        text:'Jonathan'
        font_size:32
        color:222, 233, 7, 0.96
        size:250,200
        pos:50,100
    Button:
        text:'Joshua'
        font_size:26
        color:.8,.1,0,1
        size:200,100
        pos:75,350
        

"""))