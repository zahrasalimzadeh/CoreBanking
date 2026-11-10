from io import BytesIO
from tkinter import filedialog
from ttkbootstrap import Frame, Label, Entry, Button, Toplevel
from ttkbootstrap.dialogs import Messagebox
from PIL import Image, ImageOps, ImageTk
from Presentation.Component.password_entry import PasswordEntry
from BusinessLogic.profile_business_logic import ProfileBusinessLogic

IMAGE_SIZE = 150


class ChangePasswordDialog(Toplevel):
    def __init__(self, parent, on_submit):
        super().__init__(parent)

        self.on_submit = on_submit

        self.title("Change Password")
        self.geometry("380x360")
        self.resizable(False, False)

        self.container = Frame(self, padding=20)
        self.container.pack(fill="both", expand=True)

        self.current_label = Label(self.container, text="Current Password")
        self.current_label.pack(anchor="w")

        self.current_entry = PasswordEntry(self.container)
        self.current_entry.pack(fill="x", pady=(0, 10))

        self.new_label = Label(self.container, text="New Password")
        self.new_label.pack(anchor="w")

        self.new_entry = PasswordEntry(self.container)
        self.new_entry.pack(fill="x", pady=(0, 10))

        self.confirm_label = Label(self.container, text="Confirm New Password")
        self.confirm_label.pack(anchor="w")

        self.confirm_entry = PasswordEntry(self.container)
        self.confirm_entry.pack(fill="x", pady=(0, 10))

        self.save_button = Button(self.container, text="Save", bootstyle="primary", command=self.save_clicked)
        self.save_button.pack(fill="x", pady=(10, 5))

        self.cancel_button = Button(self.container, text="Cancel", bootstyle="secondary", command=self.destroy)
        self.cancel_button.pack(fill="x")

        self.grab_set()

    def save_clicked(self):
        done = self.on_submit(
            self.current_entry.get_value(),
            self.new_entry.get_value(),
            self.confirm_entry.get_value()
        )

        if done:
            self.destroy()


class ProfileFrame(Frame):
    def __init__(self, window, main_view, profile_business: ProfileBusinessLogic):
        super().__init__(window, padding=30)

        self.main_view = main_view
        self.profile_business = profile_business
        self.employee = None
        self.photo = None

        self.title_label = Label(self, text="My Profile", font=("Segoe UI", 18, "bold"))
        self.title_label.pack(anchor="w", pady=(0, 10))

        self.image_label = Label(self, text="No picture", anchor="center")
        self.image_label.pack(pady=(0, 5))

        self.choose_picture_button = Button(self, text="Choose Picture", bootstyle="outline-primary",
                                            command=self.choose_picture_clicked)
        self.choose_picture_button.pack(pady=(0, 10))

        self.firstname_label = Label(self, text="First Name")
        self.firstname_label.pack(anchor="w")

        self.firstname_entry = Entry(self)
        self.firstname_entry.pack(fill="x", pady=(0, 10))

        self.lastname_label = Label(self, text="Last Name")
        self.lastname_label.pack(anchor="w")

        self.lastname_entry = Entry(self)
        self.lastname_entry.pack(fill="x", pady=(0, 10))

        self.mobile_label = Label(self, text="Mobile")
        self.mobile_label.pack(anchor="w")

        self.mobile_entry = Entry(self)
        self.mobile_entry.pack(fill="x", pady=(0, 10))

        self.username_label = Label(self, text="Username")
        self.username_label.pack(anchor="w")

        self.username_value = Label(self, text="", font=("Segoe UI", 10, "bold"))
        self.username_value.pack(anchor="w", pady=(0, 10))

        self.password_bar = Frame(self)
        self.password_bar.pack(fill="x", pady=(0, 10))
        self.password_bar.grid_columnconfigure(0, weight=1)

        self.password_value = Label(self.password_bar, text="Password: ••••••")
        self.password_value.grid(row=0, column=0, sticky="w")

        self.change_password_button = Button(self.password_bar, text="Change Password", bootstyle="outline-warning",
                                             command=self.change_password_clicked)
        self.change_password_button.grid(row=0, column=1)

        self.save_button = Button(self, text="Save Changes", bootstyle="primary", command=self.save_clicked)
        self.save_button.pack(fill="x", pady=(0, 10))

        self.back_button = Button(self, text="Back", bootstyle="secondary", command=self.back_clicked)
        self.back_button.pack(fill="x")

    def set_current_employee(self, employee):
        self.employee = employee
        self.load_profile()

    def load_profile(self):
        response = self.profile_business.get_profile(self.employee.id)

        if not response.success:
            Messagebox.show_error(response.message, "My Profile")
            return

        self.employee = response.data
        self.fill_fields()
        self.show_image()
        self.main_view.frames["home"][0].set_current_employee(self.employee)

    def fill_fields(self):
        self.firstname_entry.delete(0, "end")
        self.firstname_entry.insert(0, self.employee.first_name)

        self.lastname_entry.delete(0, "end")
        self.lastname_entry.insert(0, self.employee.last_name)

        self.mobile_entry.delete(0, "end")
        self.mobile_entry.insert(0, self.employee.mobile)

        self.username_value.config(text=self.employee.username)

    def show_image(self):
        if not self.employee.profile_image:
            self.photo = None
            self.image_label.config(image="", text="No picture")
            return

        image = Image.open(BytesIO(self.employee.profile_image))
        image = ImageOps.fit(image, (IMAGE_SIZE, IMAGE_SIZE))
        self.photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.photo, text="")

    def choose_picture_clicked(self):
        path = filedialog.askopenfilename(title="Choose a picture",
                                          filetypes=[("Pictures", "*.png *.jpg *.jpeg")])

        if not path:
            return

        with open(path, "rb") as file:
            image_bytes = file.read()

        try:
            Image.open(BytesIO(image_bytes)).verify()
        except Exception:
            Messagebox.show_error("This file is not a valid picture.", "My Profile")
            return

        response = self.profile_business.change_image(self.employee.id, image_bytes)

        if response.success:
            self.load_profile()
        else:
            Messagebox.show_error(response.message, "My Profile")

    def save_clicked(self):
        response = self.profile_business.update_profile(
            self.employee.id,
            self.firstname_entry.get(),
            self.lastname_entry.get(),
            self.mobile_entry.get()
        )

        if response.success:
            Messagebox.show_info(response.message, "My Profile")
            self.load_profile()
        else:
            Messagebox.show_error(response.message, "My Profile")

    def change_password_clicked(self):
        ChangePasswordDialog(self, self.submit_password)

    def submit_password(self, current_password, new_password, confirm_password):
        response = self.profile_business.change_password(
            self.employee.id, current_password, new_password, confirm_password
        )

        if response.success:
            Messagebox.show_info(response.message, "My Profile")
            return True

        Messagebox.show_error(response.message, "My Profile")
        return False

    def back_clicked(self):
        self.main_view.show_frame("home")