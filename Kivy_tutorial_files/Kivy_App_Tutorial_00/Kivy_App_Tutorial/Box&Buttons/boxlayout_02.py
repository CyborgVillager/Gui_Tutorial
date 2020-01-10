from kivy.base import runTouchApp
#Importing Builder helps you to draw .kv files by loading them in
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


Builder.load_string("""
<BoxLayout>:
    orientation: 'vertical'
#   orientation: 'horizontal'
    Button:
        text:'Hello this is Button00'
    Button:
        text:'Hello this is Button01'
    Button:
        text:'Hello this is Button02'    

""")

class MyButton_List(BoxLayout):
    pass
if __name__ == '__main__':
    #This runs your application,and calls your class
    runTouchApp(MyButton_List())
