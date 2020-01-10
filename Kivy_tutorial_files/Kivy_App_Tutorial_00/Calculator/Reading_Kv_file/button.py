import kivy
from kivy.app import App
from kivy.uix.button import Button


class MyWindowApp(App):
    def build(self):
        button = Button(text='Click Me!')
        return button

window = MyWindowApp()
window.run()
