from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):

    def animation(self, instance):
        # first one is the size for max, the other is for the minimize
        animation = Animation(pos=(100,100))
        animation += Animation(pos=(100,100)) # positionj of the button will return back to its orginal shape & position
        animation &= Animation(size=(500,500)) # max
        animation += Animation(size=(120,40)) # min

        animation.start(instance)
    def build(self):
        button = Button(
            size_hint=(None,None),
            text='Jonathan Almawi',
            on_press=self.animation
        )
        return button



if __name__ == '__main__':
    TestApp().run()
