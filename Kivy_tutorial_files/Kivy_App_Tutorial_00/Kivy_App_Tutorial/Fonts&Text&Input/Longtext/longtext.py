from kivy.app import App
from kivy.uix.label import Label

long_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed aliquam posuere risus ut consequat. Praesent blandit 
tristique eros, in porta quam bibendum vitae. Cras facilisis, nisi sed consectetur interdum, odio lorem laoreet mi, 
elementum maximus nisi massa tempor mauris. Sed leo purus, sollicitudin sit amet enim eget, tempor aliquet tortor. 
Duis id consequat turpis, sed fringilla metus. Quisque accumsan suscipit massa vel faucibus. Phasellus imperdiet ex vel
 leo fermentum, eget scelerisque nunc vulputate. Vivamus finibus at ipsum vitae sagittis. Phasellus consequat felis 
suscipit mauris tincidunt, eu blandit tellus ornare.

Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis ornare purus 
vel dolor blandit, eget dictum nunc congue. Mauris consectetur magna eu posuere efficitur. Nullam tempus et 
justo vel hendrerit. Quisque maximus non nunc aliquet lobortis. Nulla facilisi. Cras at consequat purus. Etiam id 
dui ut sapien malesuada condimentum sed eget mi. Nulla id enim non nunc porttitor hendrerit eget at ligula. 
Pellentesque eget nisi et mauris convallis ornare at ac ex. Vestibulum condimentum orci ipsum, volutpat 
tincidunt dolor rutrum quis.


"""
class text_size(App):
    def build(self):
        textLabel = Label(
            text = long_text,
            text_size=(350,None),
            line_height=1.5
                        )
        return textLabel

if __name__ == '__main__':
    text_size().run()