from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string("""
ActionBar:
    pos_hint:{'top':1}
    
    ActionView:
        ActionPrevious:
            title:'Action BAr Demo' #makes the title of your app
            with_previous:False #removes the 'back icon' for your app
        
        ActionButton:
            text:'Button_00'  #Action buttons makes buttons on top of your app/similiar to categories
        ActionButton:          #On a webpage
            text:'Button_01'
        ActionButton:
            text:'Button_02'
        ActionButton:
            text:'Button_03'
        ActionButton:
            text:'Button_04'

"""))