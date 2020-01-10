from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
Builder.load_string('''
<MyWidget>:
    direction: 'right'
    loop:True #making loop for carousel
    AsyncImage:
        source: 'images/blood_moon.jpg'
    AsyncImage:
        source: 'images/city.gif'   
    AsyncImage:
        source: 'images/lunar_mining.jpg'
    AsyncImage:
        source: 'images/Eve_Online_Battle_00.jpg'
    AsyncImage:
        source: 'images/Eve_Online_Battle_01.jpg'
    AsyncImage:
        source: 'images/Eve_Online_Battle_02.jpg'
    AsyncImage:
        source: 'images/planet3.png'     
    AsyncImage:
        source: 'images/planet4.png'
    AsyncImage:
        source: 'images/planet5.png'
                    
''')



class MyWidget(Carousel):
    pass

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()