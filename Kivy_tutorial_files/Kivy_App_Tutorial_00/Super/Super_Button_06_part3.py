from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button


class Controller2(FloatLayout):
    def __init__(self, **kwargs):
        super(Controller2, self).__init__(**kwargs)

        button = Button(text='Hello World',
                        color=(.7, .6, 0, 1), #the color format for your text 'Hello World'
                        font_size=15,   #font size for your text 'Hello World'
                        pos_hint={'x': .5, 'y': .6},  #position of your box
                        size_hint=(.2, .1)) #size of your box
        # need to draw for it to appear
        self.add_widget(button)
        button = Button(text='^_^',
                        color=(.9, .8, .5, 1),  # the color format for your text 'Hello World'
                        font_size=35,  # font size for your text 'Hello World'
                        pos_hint={'x': .3, 'y': .8},  # position of your box
                        size_hint=(.2, .1))  # size of your box
        # need to draw for it to appear
        self.add_widget(button)
        button = Button(text='(~_^)',
                        color=(.6, .3, .9, 1),  # the color format for your text 'Hello World'
                        font_size=50,  # font size for your text 'Hello World'
                        pos_hint={'x': .1, 'y': .4},  # position of your box
                        size_hint=(.2, .2))  # size of your box
        # need to draw for it to appear
        self.add_widget(button)


class YourBox_AppApp(App): #Name of your program
    def build(self):
        return Controller2()


if __name__ == '__main__':
    YourBox_AppApp().run() #runs your program
