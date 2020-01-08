from tkinter_source_file import *

class Window(Frame):

    def __init__(self, master=None):

        Frame.__init__(self,master)

        self.master = master

        self.init_window()


    def init_window(self):
        self.master.title('Gui Menu')
        self.pack(fill=BOTH, expand=1)

        # Now creating a menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file menu
        file = Menu(menu)
        # create example menu
        examp = Menu(menu)

        # This will show what subjects will be on the 'File' Category once
        # a user has clicked 'File'

        file.add_command(label='Open', command=self.client_open)
        examp.add_command(label='Exit',command=self.client_exit)

        # exit is now part of the menu
        menu.add_cascade(label='File', menu=file)


        menu.add_cascade(label='Examp', menu=examp)

        # creating the file obj
        edit = Menu(menu)
        # Add Categories in which will be shown for options, such as File, Edit, etc
        # on top of the window
        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit', menu=edit)
        menu.add_cascade(label='Now',menu=examp)

    def client_exit(self):
        exit()

root = Tk()
root.geometry('500x400')

application = Window(root)

root.mainloop()
