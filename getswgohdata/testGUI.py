# This is going to be a GUI for my platoon planner

import tkinter
import tkinter.messagebox

class SwgohGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.bot_frame = tkinter.Frame()

        self.label1 = tkinter.Label(self.top_frame, text='Choose which ' \
                                    + 'platoon type you need')

        self.light_button = tkinter.Button(self.bot_frame, \
                                           text='Light Side', \
                                           command=self.generate_ls_platoons)

        self.dark_button = tkinter.Button(self.bot_frame, \
                                          text='Dark Side', \
                                          command=self.generate_ds_platoons)

        self.ship_button = tkinter.Button(self.bot_frame, \
                                          text='Ships', \
                                          command=self.generate_ship_platoons)
        

        self.label1.pack()
        self.light_button.pack(side='left')
        self.dark_button.pack(side='left')
        self.ship_button.pack(side='left')
        self.top_frame.pack()
        self.bot_frame.pack()

        
        tkinter.mainloop()

    def generate_ls_platoons(self):
        tkinter.messagebox.showinfo('Response', \
                                    'Light Side Platoon')

    def generate_ds_platoons(self):
        tkinter.messagebox.showinfo('Response', \
                                    'Dark Side Platoon')

    def generate_ship_platoons(self):
        tkinter.messagebox.showinfo('Response', \
                                    'Ship Platoon')
    

my_gui = SwgohGUI()
