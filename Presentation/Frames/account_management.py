from math import ceil
from ttkbootstrap import Frame, Label, Button, Combobox, Treeview
from ttkbootstrap.dialogs import Messagebox
from BusinessLogic.account_business_logic import AccountBusinessLogic


class AccountManagementFrame(Frame):
    def __init__(self, window, main_view, account_business: AccountBusinessLogic):
        super().__init__(window, padding=20)

        self.main_view = main_view
        self.account_business = account_business
        self.employee = None
        self.page_number = 1
        self.total_pages = 1
        self.accounts = {}

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.top_bar = Frame(self)
        self.top_bar.grid(row=0, column=0, sticky="ew", pady=(0, 15))
        self.top_bar.grid_columnconfigure(0, weight=1)

        self.title_label = Label(self.top_bar, text="Account Management", font=("Segoe UI", 16, "bold"))
        self.title_label.grid(row=0, column=0, sticky="w")

        self.back_button = Button(self.top_bar, text="Back", bootstyle="secondary", command=self.back_button_clicked)
        self.back_button.grid(row=0, column=1, padx=(0, 10))

        self.transactions_button = Button(self.top_bar, text="Transactions", bootstyle="primary",
                                          command=self.transactions_button_clicked)
        self.transactions_button.grid(row=0, column=2)

        self.account_treeview = Treeview(self, columns=("account_number", "opening_date", "owner"), bootstyle="primary")
        self.account_treeview.grid(row=1, column=0, sticky="nsew")

        self.account_treeview.heading("#0", text="NO")
        self.account_treeview.heading("#1", text="Account Number")
        self.account_treeview.heading("#2", text="Opening Date")
        self.account_treeview.heading("#3", text="Owner")
        self.account_treeview.column("#0", width=60, anchor="center")
        self.account_treeview.column("#1", width=160, anchor="center")
        self.account_treeview.column("#2", width=140, anchor="center")
        self.account_treeview.column("#3", width=220, anchor="center")

        self.pager_bar = Frame(self)
        self.pager_bar.grid(row=2, column=0, pady=(15, 0))

        self.previous_button = Button(self.pager_bar, text="Previous", bootstyle="outline-primary",
                                      command=self.previous_button_clicked)
        self.previous_button.grid(row=0, column=0, padx=5)

        self.page_label = Label(self.pager_bar, text="Page 1 of 1")
        self.page_label.grid(row=0, column=1, padx=15)

        self.next_button = Button(self.pager_bar, text="Next", bootstyle="outline-primary",
                                  command=self.next_button_clicked)
        self.next_button.grid(row=0, column=2, padx=5)

        self.page_size_label = Label(self.pager_bar, text="Rows per page")
        self.page_size_label.grid(row=0, column=3, padx=(30, 5))

        self.page_size_combobox = Combobox(self.pager_bar, values=[10, 20, 50], width=5, state="readonly")
        self.page_size_combobox.current(0)
        self.page_size_combobox.grid(row=0, column=4)
        self.page_size_combobox.bind("<<ComboboxSelected>>", self.page_size_changed)

    def get_page_size(self):
        return int(self.page_size_combobox.get())

    def set_current_employee(self, employee):
        self.employee = employee
        self.page_number = 1
        self.load_page()

    def load_page(self):
        page_size = self.get_page_size()
        response = self.account_business.get_account_page(self.employee, self.page_number, page_size)

        if not response.success:
            Messagebox.show_error(response.message, "Account Management")
            self.main_view.show_frame("home")
            return

        for child in self.account_treeview.get_children(""):
            self.account_treeview.delete(child)

        self.accounts = {}
        first_number = (self.page_number - 1) * page_size

        for index, account in enumerate(response.data["accounts"]):
            self.accounts[account.id] = account
            self.account_treeview.insert("", "end", iid=account.id, text=str(first_number + index + 1),
                                         values=[account.account_number,
                                                 account.opening_date.strftime("%Y-%m-%d"),
                                                 account.owner_customer.get_fullname()])

        self.total_pages = max(1, ceil(response.data["total"] / page_size))
        self.page_label.config(text=f"Page {self.page_number} of {self.total_pages}")
        self.previous_button.config(state="normal" if self.page_number > 1 else "disabled")
        self.next_button.config(state="normal" if self.page_number < self.total_pages else "disabled")

    def previous_button_clicked(self):
        self.page_number -= 1
        self.load_page()

    def next_button_clicked(self):
        self.page_number += 1
        self.load_page()

    def page_size_changed(self, event):
        self.page_number = 1
        self.load_page()

    def transactions_button_clicked(self):
        selection = self.account_treeview.selection()
        if not selection:
            Messagebox.show_warning("Please select an account first.", "Account Management")
            return

        account = self.accounts[int(selection[0])]
        transactions_frame = self.main_view.show_frame("transactions")
        transactions_frame.set_account(self.employee, account)

    def back_button_clicked(self):
        self.main_view.show_frame("home")