#Project will be using printtouch/self touch basically allow user to use their fingers
#print will show the information to the user, depending on where the user has clicked on
#then draw an ellipse with color, pos x & y
#remember width, height

#THIS IS A CONTINUATION FROM PROJECT_1

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color,Ellipse,Line
from random import random

class PaintAppWidget(Widget):
    def on_touch_down(self, touch):
        #print(touch)
        color = (random(), random(), random())
        with self.canvas:
            Color(*color)
            parameter = 100 #size of your circles
            Ellipse(pos=(touch.x - parameter/2, touch.y - parameter/2),
                    size=(parameter,parameter))
            #Import Line for it to function properly
            touch.ud['Line'] = Line(points=(touch.x, touch.y))
    def on_touch_move(self, touch):
        touch.ud['Line'].points +=[touch.x, touch.y]
        #Now your able to create a line
        #click on the window while at the same time holding it.
        #Now drag to outside of the circle, you shall bring a line of the same color


class PrintApp(App):
    def build(self):
        return PaintAppWidget()

if __name__ == '__main__':
    PrintApp().run()