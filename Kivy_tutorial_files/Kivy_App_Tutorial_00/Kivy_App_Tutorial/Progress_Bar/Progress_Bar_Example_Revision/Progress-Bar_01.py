from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

BoxLayout:
    orientation:'vertical'
    #orientationl:'horizontal'
    padding: 50
    Slider: #This your able to touch/move 
        max:450
        id:Sliderid
    
    ProgressBar: #static
        max:450
        value:150
        
    ProgressBar: #connected to Slider
        max:450
        value:Sliderid.value
        
    Slider:
        #max:600 #slider 1 has value of 450, therefore once you use this slider slider1 will go out of screen
        #max:450 #bascially same value as slider 1 therefore go at the same area of screen
        max:250 #under 450 -> slider2 will not meet slider 1
        on_value:Sliderid.value = self.value  #connected with its own value as a priortiy
                #default value is 100-0 


'''))

