from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
Builder.load_string('''
<MyWidget>:
    #direction: 'left'
    direction: 'right'
    loop:True #making loop for carousel
    Label:
        text:'Screen 1'
    Label:
        text:'Screen 2'  #making pages for you to swipe
    Label:
        text:'Screen 3'
    Label:
        text:'Screen 4'
        
    AsyncImage:
        source: 'images/blood_moon.jpg'  
    AsyncImage:
        source: 'images/lunar_mining.jpg'    
    AsyncImage:
        source: 'images/Eve_Online_Battle_00.jpg'
    AsyncImage:
        source: 'images/Eve_Online_Battle_01.jpg'
    AsyncImage:
        source: 'images/Eve_Online_Battle_02.jpg'
    AsyncImage:
        source: 'images/planet3.jpg'
    AsyncImage:
        source: 'images/planet4.jpg'
    AsyncImage:
        source: 'images/planet5.jpg'
   
   



''')



class MyWidget(Carousel):
    pass

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()