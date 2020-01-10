#Project will be using printtouch/self touch basically allow user to use their fingers
#print will show the information to the user, depending on where the user has clicked on
#then draw an ellipse with color, pos x & y
#remember width, height

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color,Ellipse

class PaintAppWidget(Widget):
    def on_touch_down(self, touch):
        #print(touch)
        with self.canvas:
            Color(0,1,1,0.32)
            parameter = 100
            Ellipse(pos=(touch.x - parameter/2, touch.y - parameter/2),
                    size=(parameter,parameter))
            #width & height are = since its a circle


class PrintApp(App):
    def build(self):
        return PaintAppWidget()

if __name__ == '__main__':
    PrintApp().run()