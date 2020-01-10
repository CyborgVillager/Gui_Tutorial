from kivy.app import App
from kivy.app import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''
GridLayout:
    canvas:
        Color:
            rgb: 1,2,0
        Rectangle:
            #pos:self.pos
            pos:150,100
            #size:self.size  #size & pos will be used on your whole window
            size:100,100 


'''))