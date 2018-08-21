from tkinter import *
from encode import encode
import config

class Encode:
    def __init__(self, master):
        self.main_frame = Frame(master)
        self.main_frame['padx'] = 10
        self.main_frame['pady'] = 10
        self.main_frame.grid()

        self.method_label = Label(self.main_frame)
        self.method_label['text'] = 'Method'
        self.method_label.grid(row=0, column=0, sticky=E, pady=10, padx=10)

        self.methods = ['Binary', 'Pig Latin', 'Hex']
        self.method = StringVar(master)
        self.method.set('None')

        self.method_select = OptionMenu(self.main_frame, self.method, *self.methods, command=self.update_info)
        self.method_select['width'] = 10
        self.method_select['relief'] = GROOVE
        self.method_select.grid(row=0, column=1, sticky=W)

        self.image = PhotoImage(file='settings_icon.png')

        self.config_button = Button(self.main_frame)
        self.config_button['image'] = self.image
        self.config_button['command'] = self.config_window
        self.config_button['relief'] = GROOVE
        self.config_button.grid(row=0, column=2)

        self.input_box = Text(self.main_frame, width=40, height=10)
        self.input_box['padx'] = 5
        self.input_box['pady'] = 5
        self.input_box['relief'] = GROOVE
        self.input_box.grid(row=1, columnspan=5)

        self.input = StringVar()

        self.encode_button = Button(self.main_frame)
        self.encode_button['fg'] = 'white'
        self.encode_button['bg'] = 'green'
        self.encode_button['activeforeground'] = 'green'
        self.encode_button['activebackground'] = 'white'
        self.encode_button['width'] = 10
        self.encode_button['height'] = 2
        self.encode_button['text'] = 'Encode'
        self.encode_button['cursor'] = 'hand2'
        self.encode_button['command'] = self.update_output
        self.encode_button['relief'] = FLAT
        self.encode_button.grid(row=2, column=0, padx=10, pady=10)

        self.info = StringVar()

        self.info_label = Label(self.main_frame)
        self.info_label['textvariable'] = self.info
        self.info_label['width'] = 30
        self.info_label.grid(row=2, column=1, sticky=W)

        self.output_box = Text(self.main_frame, width=40, height=10)
        self.output_box['padx'] = 5
        self.output_box['pady'] = 5
        self.output_box['relief'] = GROOVE
        self.output_box.config(state=DISABLED)
        self.output_box.grid(row=3, columnspan=5)

    def config_window(self):
        window = config.config_window(root, self.method.get())

    def update_output(self):
        self.output_box.config(state=NORMAL)
        text = self.input_box.get(1.0, END)
        try:
            text = encode(text, self.method.get())
            text = text.replace('\n','')
        except ValueError:
            self.info.set(sys.exc_info()[0])
        except:
            self.info.set('ERROR: Unable to encode text')
        self.input.set(text)
        self.output_box.delete(1.0, END)
        self.output_box.insert(1.0, self.input.get())
        self.output_box.config(state=DISABLED)

    def update_info(self, method):
        text = {
            'Pig Latin': '',
            'Binary': 'BETA',
            'Hex': 'BETA'
        }.get(method, '')
        self.info.set(text)


root = Tk()
root.title('Project Enigma')
# root.geometry('200x100')
encode_app = Encode(root)
root.mainloop()