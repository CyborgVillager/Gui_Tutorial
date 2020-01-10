from kivy.app import App
from kivy.lang import Builder

kivy = '''

<lab@Label>:
    size_hint_y:None
    height: dp(200) #dp is measurment of units
    font_size:dp(70)
    text: 'Jonathan Almawi'
    color:1,2,.45,1
    disabled_color: self.color
    disabled:True
    
BoxLayout:
    orientation:'vertical'
    #orientation:'horizontal'
    Lab:
        markup: False
    Lab:
        markup: False
    Lab:
        markup: False
    
    

'''

class Textdisabled(App):
    def build(self):
        return Builder.load_string(kivy)

if __name__ == '__main__':
    Textdisabled().run()