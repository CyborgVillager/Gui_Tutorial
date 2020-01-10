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
            icon:'atlas://data/images/defaulttheme/audio-volume-high'
        ActionButton:          #On a webpage
            text:'Button_01'
        ActionButton:
            text:'Button_02'
        ActionButton:
            text:'Button_03'
        ActionGroup:  #makes buttons into 1 group or category of your choosing
            text:'Group_00'         #Group must have more than 3 Buttons to display itself
            color:.7,.3,.9,1
            font_size:20
            ActionButton:
                text:'Button_00'               
            ActionButton:
                text:'Button_01'
            ActionButton:
                text:'Button_02'
            ActionButton:
                text:'Button_03'
            
            

"""))