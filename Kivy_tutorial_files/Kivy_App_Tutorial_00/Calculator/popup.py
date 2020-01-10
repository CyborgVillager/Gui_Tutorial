from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

Builder.load_string('''
<box1>
    Button:
        text:'Press Me!!'
        on_press: root.edit_text()
''')


class box1(BoxLayout):
    def __init__(self, **kwargs):
        #kwargs main function responsible for pasing vars to the rest of program to your class
        super(box1, self).__init__(**kwargs)

    def edit_text(self, *args):
        #Now the text is connected to edit_text
        content = text1()

        popup = Popup(content=content, #this will be .exe in your popup & will be able to write inside
                      title='Jonathan Almawi',
                      size_hint=(None, None),
                      size=(400, 400))
        popup.open()

class text1(TextInput):
    def __init__(self, **kwargs):
        super(text1, self).__init__(**kwargs)



class SampleApp(App):
    def build(self):
        return box1()


if __name__ == '__main__':
    SampleApp().run()