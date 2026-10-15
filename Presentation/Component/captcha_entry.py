import random
import string
from ttkbootstrap import Frame, Label, Entry, Button
from captcha.image import ImageCaptcha
from PIL import Image, ImageTk


class CaptchaEntry(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.image_captcha = ImageCaptcha(width=200, height=70)
        self.captcha_text = ""
        self.captcha_photo = None

        self.image_label = Label(self)
        self.image_label.grid(row=0, column=0, columnspan=2, pady=(0, 5))

        self.entry = Entry(self)
        self.entry.grid(row=1, column=0, sticky="ew")

        # 10: فاصله بین کادر و دکمه Refresh = padx=(5, 0)
        self.refresh_button = Button(self, text="Refresh",
                                     command=self.generate_new_captcha)
        self.refresh_button.grid(row=1, column=1, padx=(5, 0))

        self.grid_columnconfigure(0, weight=1)

        self.generate_new_captcha()

    def generate_new_captcha(self):
        self.captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

        image_data = self.image_captcha.generate(self.captcha_text)
        image_data.seek(0)

        pil_image = Image.open(image_data)
        self.captcha_photo = ImageTk.PhotoImage(pil_image)

        self.image_label.config(image=self.captcha_photo)
        self.entry.delete(0, "end")

    def get_user_input(self) -> str:
        return self.entry.get().strip().upper()

    def get_captcha_answer(self) -> str:
        return self.captcha_text