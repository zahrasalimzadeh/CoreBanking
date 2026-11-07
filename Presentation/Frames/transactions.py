import os
from tkinter import filedialog
from PIL import Image, ImageTk
from ttkbootstrap import Frame, Label, Button, Treeview
from ttkbootstrap.dialogs import Messagebox
from BusinessLogic.account_business_logic import AccountBusinessLogic
from datetime import datetime


class TransactionsFrame(Frame):
    def __init__(self, window, main_view, account_business: AccountBusinessLogic):
        super().__init__(window, padding=20)

        self.main_view = main_view
        self.account_business = account_business
        self.employee = None
        self.account = None
        self.icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Assets", "bank_icon.png"))

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.header = Frame(self)
        self.header.grid(row=0, column=0, sticky="ew", pady=(0, 15))
        self.header.grid_columnconfigure(1, weight=1)

        self.icon_image = ImageTk.PhotoImage(Image.open(self.icon_path).resize((56, 56)))
        self.icon_label = Label(self.header, image=self.icon_image)
        self.icon_label.grid(row=0, column=0, rowspan=2, padx=(0, 15))

        self.title_label = Label(self.header, text="Transaction Report", font=("Segoe UI", 18, "bold"))
        self.title_label.grid(row=0, column=1, sticky="w")

        self.account_label = Label(self.header, text="", bootstyle="secondary")
        self.account_label.grid(row=1, column=1, sticky="w")

        self.date_label = Label(self.header, text="", bootstyle="secondary")
        self.date_label.grid(row=0, column=2, sticky="e")

        self.owner_label = Label(self.header, text="", font=("Segoe UI", 11, "bold"))
        self.owner_label.grid(row=1, column=2, sticky="e")

        self.transaction_treeview = Treeview(self, columns=("date", "type", "amount"), bootstyle="primary")
        self.transaction_treeview.grid(row=1, column=0, sticky="nsew")

        self.transaction_treeview.heading("#0", text="NO")
        self.transaction_treeview.heading("#1", text="Date")
        self.transaction_treeview.heading("#2", text="Type")
        self.transaction_treeview.heading("#3", text="Amount")
        self.transaction_treeview.column("#0", width=60, anchor="center")
        self.transaction_treeview.column("#1", width=200, anchor="center")
        self.transaction_treeview.column("#2", width=140, anchor="center")
        self.transaction_treeview.column("#3", width=180, anchor="center")
        self.transaction_treeview.tag_configure("deposit", foreground="#00bc8c")
        self.transaction_treeview.tag_configure("withdraw", foreground="#e74c3c")

        self.footer = Frame(self)
        self.footer.grid(row=2, column=0, sticky="ew", pady=(15, 0))
        self.footer.grid_columnconfigure(0, weight=1)

        self.balance_label = Label(self.footer, text="", font=("Segoe UI", 12, "bold"))
        self.balance_label.grid(row=0, column=0, sticky="w")

        self.pdf_button = Button(self.footer, text="Export PDF", bootstyle="primary", command=self.pdf_button_clicked)
        self.pdf_button.grid(row=0, column=1, padx=5)

        self.excel_button = Button(self.footer, text="Export Excel", bootstyle="success",
                                   command=self.excel_button_clicked)
        self.excel_button.grid(row=0, column=2, padx=5)

        self.back_button = Button(self.footer, text="Back", bootstyle="secondary", command=self.back_button_clicked)
        self.back_button.grid(row=0, column=3, padx=(5, 0))

    def set_account(self, employee, account):
        self.employee = employee
        self.account = account

        self.account_label.config(text=f"Account {account.account_number}")
        self.owner_label.config(text=account.owner_customer.get_fullname())
        self.date_label.config(text=f"Report date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

        self.load_transactions()

    def load_transactions(self):
        response = self.account_business.get_account_report(self.employee, self.account.id)

        if not response.success:
            Messagebox.show_error(response.message, "Transactions")
            self.main_view.show_frame("home")
            return

        for child in self.transaction_treeview.get_children(""):
            self.transaction_treeview.delete(child)

        for index, transaction in enumerate(response.data["transactions"], start=1):
            tag = transaction.transaction_type.name.lower()
            self.transaction_treeview.insert("", "end", text=str(index), tags=(tag,),
                                             values=[transaction.created_at.strftime("%Y-%m-%d %H:%M"),
                                                     transaction.transaction_type.name.title(),
                                                     f"{transaction.amount:,.0f}"])

        self.balance_label.config(text=f"Balance: {response.data['balance']:,.0f}")

    def pdf_button_clicked(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF file", "*.pdf")],
                                                 title="Export PDF")
        if file_path:
            response = self.account_business.export_pdf(self.employee, self.account, file_path, self.icon_path)
            self.show_export_result(response, file_path)

    def excel_button_clicked(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel file", "*.xlsx")],
                                                 title="Export Excel")
        if file_path:
            response = self.account_business.export_excel(self.employee, self.account, file_path)
            self.show_export_result(response, file_path)

    def show_export_result(self, response, file_path):
        if response.success:
            Messagebox.show_info(response.message, "Export")
            os.startfile(file_path)
        else:
            Messagebox.show_error(response.message, "Export")

    def back_button_clicked(self):
        self.main_view.show_frame("account_management")