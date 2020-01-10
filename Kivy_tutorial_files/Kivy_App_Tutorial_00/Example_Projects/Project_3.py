#Project will be using printtouch/self touch basically allow user to use their fingers
#print will show the information to the user, depending on where the user has clicked on
#then draw an ellipse with color, pos x & y
#remember width, height

#THIS IS A CONTINUATION FROM PROJECT_2
#Making Canvas clear function for your app

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color,Ellipse,Line
from random import random
from kivy.uix.button import Button

class PaintAppWidget(Widget):
    def on_touch_down(self, touch):
        #print(touch)
        color = (random(), random(), random())
        with self.canvas:
            Color(*color)
            parameter = 60 #size of your circles
            Ellipse(pos=(touch.x - parameter/2, touch.y - parameter/2),
                    size=(parameter,parameter))
            #Import Line for it to function properly
            touch.ud['Line'] = Line(points=(touch.x, touch.y))
    def on_touch_move(self, touch):
        touch.ud['Line'].points +=[touch.x, touch.y]


#Making the Clear function
class PrintApp(App):
    def build(self):
# return PaintAppWidget()
        parent = Widget()
        parent2 = PaintAppWidget()
        clearbutton = Button(text='Clear')

        parent.add_widget(parent2)
        parent.add_widget(clearbutton)

        #Now make a function

        def clear_canvas(obj):
            parent2.canvas.clear()
        clearbutton.bind(on_release=clear_canvas)
        return parent

if __name__ == '__main__':
    PrintApp().run()