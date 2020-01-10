import kivy
import random
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

#now get the sound
#Now attach this to button.bind(on_press=lambda , etc,etc
sound = SoundLoader.load('sounds/wowox2.wav') #wow!!!
#sound = SoundLoader.load('sounds/wow.mp3') #wow!

# colors that the random will choose from
red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]


class Buttons(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        colors = [red, green, blue, purple]
        for i in range(6):
            button = Button(text='Test Button Sound %s ' % (i+1),  # each time %s is .exe it will be replaced by 1
                            # chaning background color from random
                            background_color=random.choice(colors),
                            )
            #essential to have this to let your sound funct to work prioperly -> bind it with button
            button.bind(on_press=lambda *args : sound.play())
            #
            layout.add_widget(button)
        return layout


if __name__ == '__main__':
    app = Buttons()
    app.run()
    #another way to start your program instead of doing
    #Buttons().run()


