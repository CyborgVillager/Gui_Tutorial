from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""
<Button>:
    color: 159, 18, 248, 1     
    font_size: 50
    size_hint: .3,.2

PageLayout:
    Button:
        text:'Button_00'
    Button:
        text:'Button_01'

"""))