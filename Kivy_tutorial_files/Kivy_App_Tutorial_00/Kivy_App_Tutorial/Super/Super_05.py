from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button

class BoxClass00(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxClass00,self).__init__(**kwargs)
#To make space between
 #       self.padding = 100
        self.padding = 200
        button = Button(text='Jonathan Almawi')
        self.add_widget(button)
class BoxClass01(App):
    def build(self):
        return BoxClass00()


if __name__ == '__main__':
    BoxClass01().run()