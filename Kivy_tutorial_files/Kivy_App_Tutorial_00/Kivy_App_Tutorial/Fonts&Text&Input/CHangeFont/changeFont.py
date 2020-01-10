from kivy.app import App
from kivy.lang import Builder




root = Builder.load_string('''
Label:
    text: 
        ('[b]Hello[/b] [color=046720]User![/color]\\n'
        '[u]Hello[/u] [color=046720]User![/color]\\n'
        '[i]Hello[/i] [color=046720]User![/color]\\n'
        '[s]Hello[/s] [color=046720]User![/color]\\n'
        '[font=RobotoMono-Regular]Hello[/font] [color=046720]User![/color]')
        
    font_size:'45'
    markup:True



''')


class text_tag(App):
    def build(self):
        return root

if __name__ =='__main__':
    text_tag().run()