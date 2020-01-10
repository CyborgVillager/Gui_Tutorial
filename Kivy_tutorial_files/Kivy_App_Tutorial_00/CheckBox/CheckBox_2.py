from kivy.base import runTouchApp
from  kivy.lang import Builder
runTouchApp(Builder.load_string('''
GridLayout:
    cols:2  #to organize your checkboxes, if this were 
            #to be disabled they would stack on each other
    CheckBox:
        active:False
    Label:
        text:'CheckBox 1'
    CheckBox:
        active:True
    Label:
        text:'CheckBox 2'
        
    CheckBox:
        group:'Radio Button'  #radio button
        active:True
        
    Label:
        text:'Radio Button'


'''))
