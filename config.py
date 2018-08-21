from tkinter import *
import json

class config_window():
    def __init__(self, master, method):
        self.window = Toplevel(master)
        self.frame = Frame(self.window)
        self.frame['padx'] = 10
        self.frame['pady'] = 10
        self.frame.grid()
        if method == 'Binary':
            self.binary()
        elif method == 'Pig Latin':
            self.pig_latin()
        # switch = {
        #     'Binary': self.binary(),
        #     'Pig Latin': self.pig_latin()
        # }
        # try:
        #     switch.get(method)
        # except:
        #     pass
    def binary(self):
        with open('config.json') as f:
            config = json.load(f)
        print(1)
        zero = StringVar()
        zero.set(config['binary']['0'])
        zero_label = Label(self.frame)
        zero_label['text'] = 'Zero'
        zero_label.grid(row=0, column=0, sticky=E)
        zero_entry = Entry(self.frame, width=20)
        zero_entry['textvariable'] = zero
        # zero_entry['command'] = self.update('binary', '0', zero.get())
        zero_entry.grid(row=0, column=1, sticky=W)
        
        one = StringVar()
        one.set(config['binary']['1'])
        one_label = Label(self.frame)
        one_label['text'] = 'One'
        one_label.grid(row=1, column=0, sticky=E)
        one_entry = Entry(self.frame, width=20)
        one_entry['textvariable'] = one
        # one_entry['command'] = self.update('binary', '1', one.get())
        one_entry.grid(row=1, column=1, sticky=W)

        def update():
            with open('config.json') as f:
                config = json.load(f)
            config['binary']['1'] = one.get()
            config['binary']['0'] = zero.get()
            with open('config.json', 'w') as f:
                json.dump(config, f)
            self.window.destroy()

        apply = self.apply_button(update)
    def pig_latin(self):
        with open('config.json') as f:
            config = json.load(f)
        case_label = Label(self.frame)
        case_label['text'] = 'Case'
        case_label.grid(row=0, column=0, sticky=E)

        cases = ['upper', 'lower']
        case = StringVar()
        case.set(config['pig-latin']['case'])
        case_select = OptionMenu(self.frame, case, *cases)
        case_select['width'] = 10
        case_select['relief'] = GROOVE
        case_select.grid(row=0, column=1, sticky=W)
        # case_entry = Entry(self.frame, width=20)
        # case_entry['textvariable'] = case
        # case_entry.grid(row=0, column=1, sticky=W)

        end = StringVar()
        end.set(config['pig-latin']['end'])
        end_label = Label(self.frame)
        end_label['text'] = 'End'
        end_label.grid(row=1, column=0, sticky=E)
        end_entry = Entry(self.frame, width=20)
        end_entry['textvariable'] = end
        end_entry.grid(row=1, column=1, sticky=W)

        def update():
            with open('config.json') as f:
                config = json.load(f)
            config['pig-latin']['case'] = case.get()
            config['pig-latin']['end'] = end.get()
            with open('config.json', 'w') as f:
                json.dump(config, f)
            self.window.destroy()

        apply = self.apply_button(update)

    def apply_button(self, command):
        self.button = Button(self.frame)
        self.button['fg'] = 'white'
        self.button['bg'] = 'green'
        self.button['activeforeground'] = 'green'
        self.button['activebackground'] = 'white'
        self.button['width'] = 10
        self.button['height'] = 2
        self.button['text'] = 'Apply'
        self.button['cursor'] = 'hand2'
        self.button['command'] = command
        self.button['relief'] = FLAT
        self.button.grid(row=100, column=1, padx=10, pady=10)
    # def update(self):
    #     # config[method][location] = value
    #     with open('config.json', 'w') as f:
    #         json.dump(config, f)

# root = Tk()
# config = config_window(root, 'Pig Latin')
# root.mainloop()