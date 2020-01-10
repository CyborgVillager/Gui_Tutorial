from kivy.app import App
from kivy.lang import Builder

kivy = '''
AnchorLayout:
    TextInput:
        size_hint: None,None    #Width,height
        size:400,100
        text:'Type your text'
        use_bubble: True
        use_handles:True
        #password:True  #use for password login
        readonly: True  #read only



'''

class TextInput_Test(App):
    def build(self):
        return Builder.load_string(kivy)

if __name__ == '__main__':
    TextInput_Test().run()