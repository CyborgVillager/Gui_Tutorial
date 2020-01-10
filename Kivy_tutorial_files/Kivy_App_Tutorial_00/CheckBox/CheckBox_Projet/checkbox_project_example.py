from kivy.app import App
from kivy.lang import Builder

kivy = '''
BoxLayout:
    orientation: 'vertical'
    #orientation: 'horizontal'
    CheckBox:
        group:'a'
        active: True
        
    CheckBox:
        id: Check
        group:'a'
        
    Button:
        text:'Yes'
        on_press: Check.active = True
    Button:
        text:'No'
        on_press: Check.active = False
        



'''
class CheckBoxProjectExampleApp(App):
    def build(self):
        return Builder.load_string(kivy)

if __name__ == '__main__':
    CheckBoxProjectExampleApp().run()