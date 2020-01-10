from kivy.app import App
from kivy.lang import Builder

kivy = '''
FloatLayout:
    #Button:
    Label:
        text:'Hello User'   
        size_hint:None,None
        pos_hint:{'center_x':.5, 'center_y':.5}
        canvas.before:
            Rotate:
                #angle: 45
                #angle: 90
                angle:100 #has been rotated 100 degrees
                origin: self.center



'''

class rotate(App):
    def build(self):
        return Builder.load_string(kivy)

rotate().run()