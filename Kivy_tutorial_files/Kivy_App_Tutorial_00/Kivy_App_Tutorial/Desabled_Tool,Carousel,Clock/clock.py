from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

root = Builder.load_string('''

FloatLayout:
    Scatter:
        id: clockscatter
        size_hint: None,None
        size: 100,100
        pos: root.width / 2 - self.width / 2, root.height / 2 - self.height / 2
        Button:
            text:'Clock'


''')

class TestApp(App):
    def build(self):
        Clock.schedule_interval(self.rotate, 1) #1 second to rotate the clock, 2 -> 2 seconds, 0-> full speed ahead!
        return root
    def rotate(self, dt):
        root.ids.clockscatter.rotation +=3 #move by 3 steps -> high # = increase speed of rotation, low # is opposite

if __name__ == '__main__':
    TestApp().run()