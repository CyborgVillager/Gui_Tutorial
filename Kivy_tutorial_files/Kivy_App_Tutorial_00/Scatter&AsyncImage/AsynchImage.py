from kivy.app import App
from kivy.lang import Builder

kv = '''
AnchorLayout:
    canvas:
        Color:
            rgb: 1,2,0
        Rectangle:
            pos:self.pos
            size:self.size
    AsyncImage:
        size_hint:None,None
        size: dp(300), dp(275)  #size_hint & size - width,height
        source: 'http://d2ouvy59p0dg6k.cloudfront.net/img/original/field_school2016__133_1.jpg'
        anim_delay: .9 #speed of loading gif  high - >slower low->faster gif speed


'''

class AsynchImageAppApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    AsynchImageAppApp().run()
