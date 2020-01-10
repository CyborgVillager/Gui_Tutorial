from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_string('''
<GridLayout>
    canvas.before:
        BorderImage:
            source:'images/realm_of_shades.jpg'
            pos: self.pos
            size: self.size
            
<FontWidget>
    GridLayout:
        size_hint: .9,.9
        pos_hint: {'center_x': .5, 'center_y':.5}
        rows: 1
        
        Label:
            text:' Example text for your image for top'
            text_size: self.width-20, self.height-20
            valign: 'top'
           
            
        Label:
            text:' Example text for your image for top'
            text_size: self.width-20, self.height-20
            valign: 'top'
            
        Label:
            text:' Example text for your image for top'
            text_size: self.width-20, self.height-20
            valign: 'top'
            halign:'right'
            
        Label:
            text:' Example text for your image for center'
            text_size: self.width-20, self.height-20
            valign: 'center'
        
            
        Label:
            text:' Example text for your image for bottom'
            text_size: self.width-20, self.height-20
            valign: 'bottom'
           # halign:'left'
        Label:
            text:' Example text for your image for bottom'
            text_size: self.width-20, self.height-20
            valign: 'bottom'


''')

class FontWidget(FloatLayout):
    pass

class FontApp(App):
    def build(self):
        return FontWidget()

if __name__ == '__main__':
    FontApp().run()