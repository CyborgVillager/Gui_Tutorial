from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage

class CarouselApp(App):
    def build(self):
        carousel = Carousel(
            direction='right',
            loop = True,
        )
        for i in range(2):


            src0 ='images/city.gif'
            src1 ='images/clouds.gif'
            src2 ='images/Eve_Online_Battle_01.jpg'
            image = AsyncImage(source = src2)
            carousel.add_widget(image)
        return carousel

CarouselApp().run()