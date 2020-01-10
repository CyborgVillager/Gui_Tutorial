from kivy.uix.spinner import Spinner
from kivy.base import runTouchApp

spinexample = Spinner (
    text='Home', #always remember to close by including , at the end
                #of your vals
    values=('Home','Profile','Gallary','Friends','Settings','Log Out'),
     size_hint=(None,None),
    size=(100,44),
    pos_hint={'center_x':.5, 'center_y':.5}

)

def Show_value(spinner,text):
    print('The user is on spinner text', text)

spinexample.bind(text=Show_value)

runTouchApp(spinexample)