from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

class YourLabel_AppApp(App):
    def build(self):
        return Label(text='[color=e11809ff]Hello[/color]' +
                          '[color=09e16b][b] World![/b] [/color]' +
                          '[color=0d09e1][s] Color[/s] [/color]' +
                           '[color=14e109]2 [/color][sup]4[/sup]',
                     markup=True, # To show your text color must make 'markup' True for it to function properly
                     font_size='60',)

if __name__ == '__main__':
    YourLabel_AppApp().run()