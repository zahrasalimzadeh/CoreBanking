from ttkbootstrap import Frame, Label, Entry, Button
from ttkbootstrap.dialogs import Messagebox
from Presentation.Component.password_entry import PasswordEntry
from Presentation.Component.captcha_entry import CaptchaEntry



class RegisterFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window, padding=30)

        self.main_view = main_view

        self.title_label = Label(self, text="Create account", font=("Segoe UI", 18, "bold"))
        self.title_label.pack(anchor="w", pady=(0, 10))

        self.firstname_label = Label(self, text="First Name")
        self.firstname_label.pack(anchor="w")

        self.firstname_entry = Entry(self)
        self.firstname_entry.pack(fill="x", pady=(0, 10))

        self.lastname_label = Label(self, text="Last Name")
        self.lastname_label.pack(anchor="w")

        self.lastname_entry = Entry(self)
        self.lastname_entry.pack(fill="x", pady=(0, 10))

        self.username_label = Label(self, text="Username")
        self.username_label.pack(anchor="w")

        self.username_entry = Entry(self)
        self.username_entry.pack(fill="x", pady=(0, 10))

        self.password_label = Label(self, text="Password")
        self.password_label.pack(anchor="w")

        self.password_entry = PasswordEntry(self)
        self.password_entry.pack(fill="x", pady=(0, 10))

        self.captcha_entry = CaptchaEntry(self)
        self.captcha_entry.pack(fill="x", pady=(0, 10))

        self.register_button = Button(self, text="Register", bootstyle="primary", command=self.register_button_clicked)
        self.register_button.pack(fill="x", pady=(0, 10))

        self.back_button = Button(self, text="Back to Login Page", bootstyle="link", command=self.back_button_clicked)
        self.back_button.pack()

    def back_button_clicked(self):
        self.main_view.show_frame("login")

    def register_button_clicked(self):
        missing = []

        if not self.firstname_entry.get():
            missing.append("first name")

        if not self.lastname_entry.get():
            missing.append("last name")

        if not self.username_entry.get():
            missing.append("username")

        if not self.password_entry.get_value():
            missing.append("password")

        if not self.captcha_entry.get_user_input():
            missing.append("captcha")

        if missing:
            Messagebox.show_error("Please enter " + ", ".join(missing) + ".", "Register Failed")
            return

        if self.captcha_entry.get_user_input() != self.captcha_entry.get_captcha_answer():
            Messagebox.show_error("Captcha is incorrect.", "Register Failed")
            self.captcha_entry.generate_new_captcha()
            return

        Messagebox.show_info("Captcha verified. (Register logic not implemented yet)", "Success")