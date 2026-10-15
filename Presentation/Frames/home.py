from ttkbootstrap import Frame, Label, Button
from Common.Entities.employee import Employee
from Common.Enums.role import Roles
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Presentation.main_view import MainView


class HomeFrame(Frame):
    def __init__(self, window, main_view: MainView):
        super().__init__(window, padding=30)

        self.grid_columnconfigure(0, weight=1)

        self.main_view = main_view
        self.current_employee = None
        self.header_label = Label(self, font=("Segoe UI", 14, "bold"), wraplength=340, justify="center")
        self.header_label.grid(row=0, column=0, pady=(0, 20))

        self.employee_management = Button(self, text="Employee Management", bootstyle="primary")

        self.account_management = Button(self, text="Account Management", bootstyle="primary")

        self.profile_management = Button(self, text="My Profile")
        self.profile_management.grid(row=3, column=0, pady=(0, 10), sticky="ew")

        self.logout_button = Button(self, text="Logout", bootstyle="danger", command=self.logout_button_clicked)
        self.logout_button.grid(row=4, column=0, sticky="ew")

    def set_current_employee(self, current_employee: Employee):
        self.current_employee = current_employee

        self.header_label.config(
            text=f"Welcome {self.current_employee.get_fullname()} ({self.current_employee.role.name})")

        match self.current_employee.role:
            case Roles.ADMINISTRATOR:
                self.employee_management.grid(row=1, column=0, pady=(0, 10), sticky="ew")
                self.account_management.grid_forget()
            case Roles.BANKER:
                self.employee_management.grid_forget()
                self.account_management.grid(row=2, column=0, pady=(0, 10), sticky="ew")
            case _:
                self.employee_management.grid_forget()
                self.account_management.grid_forget()

    def logout_button_clicked(self):
        self.current_employee = None
        self.main_view.show_frame("login")