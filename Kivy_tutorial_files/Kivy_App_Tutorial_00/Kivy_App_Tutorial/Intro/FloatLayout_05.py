from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""
<Button>:
    color: 159, 18, 248, 1     
    font_size: 50
    size_hint: .3,.2
    
FloatLayout: 
#Top Left
    Button:
        text:'Button_00'
        pos_hint:{'x':0, 'top':1}
#Bottom Right
    Button:
        text:'Button_01'
        pos_hint:{'y':0, 'right':1}
        
#Bottom Left       
    Button:
        text:'Button_02'
        pos_hint:{'down':1, 'lift':1}
#Top Right   
    Button:
        text:'Button_03'
        pos_hint:{'top':1, 'right':1}
#Center
    Button:
        text:'Button_04'
        pos_hint:{'x':.35, 'y':.4}


"""))