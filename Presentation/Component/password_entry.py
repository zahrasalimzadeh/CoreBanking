from ttkbootstrap import Frame, Entry, Button


class PasswordEntry(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=0, column=0, sticky="ew")

        # 8: فاصله بین کادر و دکمه Show = padx=(5, 0)
        self.change_state_button = Button(self, text="Show", width=6,
                                          command=self.change_state_button_clicked)
        self.change_state_button.grid(row=0, column=1, padx=(5, 0))

    def change_state_button_clicked(self):
        current_value = self.change_state_button.cget("text")

        if current_value == "Show":
            self.change_state_button.config(text="Hide")
            self.password_entry.config(show="")
        else:
            self.change_state_button.config(text="Show")
            self.password_entry.config(show="*")

    def get_value(self):
        value = self.password_entry.get()
        return value