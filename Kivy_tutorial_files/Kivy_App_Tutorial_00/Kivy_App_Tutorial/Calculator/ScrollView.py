from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class ScrollViewApp(App):
    def build(self):
        layout = GridLayout(cols=1,
                            padding=10,
                            spacing=5,
                            size_hint=(None,None),
                            width=500)
#Now adding movement to allow user to 'scroll'
        layout.bind(minimum_height=layout.setter('height'))


#putting the numbers in 20
        for i in range(21):
            buttons = Button(text=str(i), #this will loop over 20 times
                             size_hint=(None,None),
                             size=(500,40),
                             )
            layout.add_widget(buttons) #this connects to buttons=Button(etc,etc,etc)

        root = ScrollView(size_hint=(None,None),
                          size=(500, 333),
                          pos_hint={'center_x':.5, 'center_y':.5},
                             )
        root.add_widget(layout)
        return root


if __name__ == '__main__':
    ScrollViewApp().run()