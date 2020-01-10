from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

#BoxLayout
runTouchApp(Builder.load_string("""

BoxLayout:
    orientation: 'vertical'
#   orientation: 'horizontal'  -> its on by default
# Can include spacing to give "room" / design features for your app
    spacing: 10 
    padding: 35
    Button:
        text: 'Button_00'
    Button:
        text: 'Button_01'   


"""))