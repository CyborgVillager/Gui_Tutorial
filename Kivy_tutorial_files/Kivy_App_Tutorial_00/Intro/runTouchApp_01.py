from kivy.base import runTouchApp
from kivy.lang import Builder

#This will load a string that will be shown onto your window

#runTouchApp(Builder.load_string('''

#StackLayout:
#    Label:
 #       text:"Hello This is a Label, cannot interact with me"

#'''))


#By changing Label to Button your able to make the while screen into a clickable object for the
#user to interact with
runTouchApp(Builder.load_string('''

StackLayout:
    Button:
        text:"Testing Button, you can interact" + "" + " with me"
        

'''))