from ttkbootstrap import Frame, Label, Entry, Button
from ttkbootstrap.dialogs import Messagebox
from Common.Services.sms_service import SmsService
from Common.Services.notification_publisher import NotificationPublisher


class OtpFrame(Frame):
    def __init__(self, main_window, main_view, employee):
        super().__init__(main_window, padding=30)

        self.main_view = main_view
        self.employee = employee
        self.mobile = employee.mobile
        self.sms_service = SmsService()
        self.notification_publisher = NotificationPublisher()
        self.correct_code = None

        self.remaining_seconds = 0
        self.timer_job = None

        self.welcome_label = Label(self, text="Enter the code sent to your phone", font=("Segoe UI", 14, "bold"),
                                   wraplength=340, justify="center")
        self.welcome_label.pack(pady=(0, 20))

        self.code_label = Label(self, text="Code")
        self.code_label.pack(anchor="w")

        self.code_entry = Entry(self, font=("Segoe UI", 18), justify="center")
        self.code_entry.pack(fill="x", pady=(0, 15))

        self.validation_button = Button(self, text="Validation", bootstyle="primary",
                                        command=self.validation_button_clicked)
        self.validation_button.pack(fill="x", pady=(0, 10))

        self.retry_button = Button(self, text="Send Retry SMS", bootstyle="link", command=self.retry_button_clicked)
        self.retry_button.pack()

        self.timer_label = Label(self, text="", bootstyle="light")
        self.timer_label.pack(pady=(5, 0))

        self.send_initial_otp()

    def send_initial_otp(self):
        self.correct_code = self.sms_service.generate_code()
        self.notification_publisher.publish(self.mobile, self.correct_code)
        self.start_timer(120)

    def validation_button_clicked(self):
        user_code = self.code_entry.get().strip()

        if user_code == self.correct_code:
            home_frame = self.main_view.show_frame("home")
            home_frame.set_current_employee(self.employee)
        else:
            Messagebox.show_error("The code you entered is incorrect.", "Validation Failed")

    def retry_button_clicked(self):
        if self.remaining_seconds > 0:
            return

        self.correct_code = self.sms_service.generate_code()
        self.notification_publisher.publish(self.mobile, self.correct_code)
        self.start_timer(120)

    def start_timer(self, seconds: int):
        self.remaining_seconds = seconds
        self.retry_button.config(state="disabled")
        self.update_timer()

    def update_timer(self):
        if self.remaining_seconds > 0:
            minutes = self.remaining_seconds // 60
            seconds = self.remaining_seconds % 60
            self.timer_label.config(text=f"Retry available in {minutes}:{seconds:02d}")
            self.remaining_seconds -= 1
            self.timer_job = self.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="")
            self.retry_button.config(state="normal")