from tkinter import Frame, Label

class ProfileFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.main_view = main_view

        self.title_label = Label(self, text="My Profile")
        self.title_label.grid(row=0, column=0, pady=10, padx=10)