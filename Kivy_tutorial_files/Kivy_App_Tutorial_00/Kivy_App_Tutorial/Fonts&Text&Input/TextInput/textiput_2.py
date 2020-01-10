from kivy.app import App
from kivy.lang import Builder

kivy = '''
AnchorLayout:
    TextInput:
        size_hint: None,None
        size: 500,150
        background_color: 0,35,25,1
        hint_text: 'Enter your text here'
        text: ' Jonathan Almawi'
        font_size: 25
        focus : True
        on_scroll_y: print(self.focus)
        #multiline: False #cant enter 



'''

class TextInput_2(App):
    def build(self):
        return Builder.load_string(kivy)
if __name__ == '__main__':
    TextInput_2().run()