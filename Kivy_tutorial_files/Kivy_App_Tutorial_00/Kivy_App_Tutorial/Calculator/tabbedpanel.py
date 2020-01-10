from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
#to create more than 1 tab use tabbedPanel
Builder.load_string('''
<Test>:
    size_hint: .7 , .7
    pos_hint: {'center_x': .5, 'center_y': .5}
    background_color: 1,2,1,2       
    do_default_tab: False
    TabbedPanelItem:
        text:'tab 1'
        BoxLayout:
            Label:
                text:'Jonathan Almawi'
            Button:
                text:'this is a Button for tab1'
                background_color: 4,1,6,2             
            
    TabbedPanelItem:
        text:'tab 2'
        BoxLayout:
            Label:
                text:'Welcome to tab 2!' 
        RstDocument:
            text:
                '\\n'.join(('RstDoc is basically an article, etc', '____________',
                'The join() method is a string method and returns a string',
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed fermentum ipsum et quam porttitor, sit', 
                'amet hendrerit mi pulvinar. Donec quam urna, pharetra in posuere eu, gravida vel nulla. Suspendisse', 
                'tincidunt neque et nunc venenatis pulvinar. Aenean tristique odio non sapien sollicitudin pretium.',))
                
       
             
                
 
''')

class Test(TabbedPanel):
    pass

class MultiTabbedPanelApp(App):
    def build(self):
        return Test()

if __name__ == '__main__':
    MultiTabbedPanelApp().run()
