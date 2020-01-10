from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

dropdown = DropDown()

# this range encloses all the buttons that are part of the main version
for i in range(11):
    button = Button(text='value %d' %i,  # each time the range loop it will be replaced by a new value
                    size_hint_y=None,
                    height=40,
                    )
    # Once you click on a button 'category' value0,1,2,etc it will collapse it self bck to its orignal form
    button.bind(on_release=lambda button: dropdown.select(button.text))
    dropdown.add_widget(button)

# main button or version I usually call it main version
mainbutton = Button(text='Hello!',
                    size_hint=(None,None),
                    )
# basically a repeating cycle, to take the value x (line #26) to text='value %d' at line 9.
# If line 9 or 26 updates update this comment!
# By doing this the user will see the updated 'value' at the button. If they click 7 they will see val 7, 8 ->
# see 8, etc
dropdown.bind(on_select = lambda instance, x: setattr(mainbutton, 'text', x))
# Once you 'release' the button it will open itself for the user
mainbutton.bind(on_release=dropdown.open)

runTouchApp(mainbutton)