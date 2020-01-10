from kivy.app import App
from kivy.uix.label import Label
class MyApp(App):
    def build(self):
        return Label(text='Hello World!')
    #This returns the label() as a root widget remmber ^_*

if __name__ == '__main__':
    MyApp().run()