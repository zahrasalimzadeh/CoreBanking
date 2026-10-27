from tkinter import PhotoImage
from ttkbootstrap import Frame, Label, Entry, Button, Checkbutton
from ttkbootstrap.dialogs import Messagebox
from Presentation.Component.password_entry import PasswordEntry
from Presentation.Component.captcha_entry import CaptchaEntry
from Common.Decorators.performance_logger import performance_logger


from BusinessLogic.user_business_logic import UserBusinessLogic


class LoginFrame(Frame):
    def __init__(self, main_window, main_view, user_business: UserBusinessLogic):
        super().__init__(main_window)

        self.main_view = main_view
        self.user_business = user_business


        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.left_form = Frame(self, bootstyle="primary", width=300)
        self.left_form.grid(row=0, column=0, sticky="nsew")

        self.icon_photo = PhotoImage(file="Presentation/Assets/bank_icon.png")
        self.logo_label = Label(self.left_form, image=self.icon_photo, text="Core Banking", compound="top",
                                font=("Segoe UI", 22, "bold"), bootstyle="inverse-primary")
        self.logo_label.place(relx=0.5, rely=0.5, anchor="center")


        self.right_form = Frame(self, padding=30)
        self.right_form.grid(row=0, column=1, sticky="nsew")

        self.title_label = Label(self.right_form, text="Welcome back", font=("Segoe UI", 18, "bold"))
        self.title_label.pack(anchor="w", pady=(0, 10))

        self.username_label = Label(self.right_form, text="Username")
        self.username_label.pack(anchor="w")

        self.username_entry = Entry(self.right_form)
        self.username_entry.pack(fill="x", pady=(0, 10))

        self.password_label = Label(self.right_form, text="Password")
        self.password_label.pack(anchor="w")

        self.password_entry = PasswordEntry(self.right_form)
        self.password_entry.pack(fill="x", pady=(0, 10))

        self.captcha_entry = CaptchaEntry(self.right_form)
        self.captcha_entry.pack(fill="x", pady=(0, 10))

        self.remember_me_button = Checkbutton(self.right_form, text="Remember Me?", bootstyle="round-toggle")
        self.remember_me_button.pack(anchor="w", pady=(0, 10))

        self.login_button = Button(self.right_form, text="Login", bootstyle="primary", command=self.login_button_clicked)
        self.login_button.pack(fill="x", pady=(0, 10))

        self.register_button = Button(self.right_form, text="Register", bootstyle="link",
                                      command=self.register_button_clicked)
        self.register_button.pack()

    @performance_logger
    def login_button_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get_value()
        captcha_input = self.captcha_entry.get_user_input()
        captcha_answer = self.captcha_entry.get_captcha_answer()

        response = self.user_business.login(username, password, captcha_input, captcha_answer)

        if not response.success and response.message == "Captcha is incorrect.":
            self.captcha_entry.generate_new_captcha()

        if response.success:
            self.main_view.show_otp_frame(response.data)
        else:
            Messagebox.show_error(response.message, "Login Failed")

    def register_button_clicked(self):
        self.main_view.show_frame("register")