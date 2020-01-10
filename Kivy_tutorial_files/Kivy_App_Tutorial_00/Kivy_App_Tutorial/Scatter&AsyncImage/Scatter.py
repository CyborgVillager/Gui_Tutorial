#Gives you the freedom to use any runTouch propertity that you place on your window
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

FloatLayout:
    Scatter&AsyncImage:  #Lets you drag anything, if you place in the proper procedures
        size: 80,80
        pos:100,100
        do_rotation: False #This disabled rotation, so the user can only max/min the img or text
        Label:
            text:'Hello'  #Once you activate the program you can move around the word "Hello"
        
    Scatter&AsyncImage:  #Lets you drag anything, if you place in the proper procedures
        size: 80,80
        pos:150,120
        Label:
            text:'World!'
            
    #Can also change size by right clicking it and dragging it out, similiar to a mobile phone
    


'''))