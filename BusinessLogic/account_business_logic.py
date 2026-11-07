from datetime import datetime
from Common.DTOs.response import Response
from Common.Enums.role import Roles
from Common.Repositories.iaccount_repository import IAccountRepository
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


class AccountBusinessLogic:
    def __init__(self, account_repository: IAccountRepository):
        self.account_repository = account_repository

    def get_balance(self, account_id: int):
        if account_id is None or account_id <= 0:
            return Response(False, "Invalid account.")

        balance = self.account_repository.get_balance(account_id)
        return Response(True, "Balance was loaded.", balance)

    def get_transactions(self, account_id: int):
        if account_id is None or account_id <= 0:
            return Response(False, "Invalid account.")

        transactions = self.account_repository.get_transaction_by_account_id(account_id)
        return Response(True, "Transactions were loaded.", transactions)

    def get_accounts(self, customer_id: int):
        if customer_id is None or customer_id <= 0:
            return Response(False, "Invalid customer.")

        accounts = self.account_repository.get_accounts_by_customer_id(customer_id)
        return Response(True, "Accounts were loaded.", accounts)

    def is_banker(self, employee):
        return employee is not None and employee.role == Roles.BANKER

    def get_account_page(self, employee, page_number: int, page_size: int):
        if not self.is_banker(employee):
            return Response(False, "Access denied.")

        if page_number < 1 or page_size < 1:
            return Response(False, "Invalid page.")

        accounts = self.account_repository.get_account_list(page_number, page_size)
        total = self.account_repository.get_account_count()
        return Response(True, "Accounts were loaded.", {"accounts": accounts, "total": total})

    def get_account_report(self, employee, account_id: int):
        if not self.is_banker(employee):
            return Response(False, "Access denied.")

        transactions_response = self.get_transactions(account_id)
        if not transactions_response.success:
            return transactions_response

        balance_response = self.get_balance(account_id)
        return Response(True, "Report was loaded.", {
            "transactions": transactions_response.data,
            "balance": balance_response.data
        })

    def export_excel(self, employee, account, file_path: str):
        if not self.is_banker(employee):
            return Response(False, "Access denied.")

        try:
            transactions = self.account_repository.get_transaction_by_account_id(account.id)

            workbook = Workbook()
            sheet = workbook.active
            sheet.title = "Transactions"

            sheet["A1"] = "Transaction Report"
            sheet["A1"].font = Font(size=16, bold=True, color="375A7F")
            sheet["A2"] = f"Report date: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            sheet["A3"] = f"Account number: {account.account_number}"
            sheet["A4"] = f"Owner: {account.owner_customer.get_fullname()}"

            header = ["#", "Date", "Type", "Amount"]
            for column, title in enumerate(header, start=1):
                cell = sheet.cell(row=6, column=column, value=title)
                cell.font = Font(bold=True, color="FFFFFF")
                cell.fill = PatternFill("solid", fgColor="375A7F")
                cell.alignment = Alignment(horizontal="center")

            for index, transaction in enumerate(transactions, start=1):
                row = index + 6
                sheet.cell(row=row, column=1, value=index)
                sheet.cell(row=row, column=2, value=transaction.created_at.strftime("%Y-%m-%d %H:%M"))
                sheet.cell(row=row, column=3, value=transaction.transaction_type.name.title())
                amount_cell = sheet.cell(row=row, column=4, value=float(transaction.amount))
                amount_cell.number_format = "#,##0"

            sheet.column_dimensions["A"].width = 8
            sheet.column_dimensions["B"].width = 22
            sheet.column_dimensions["C"].width = 16
            sheet.column_dimensions["D"].width = 18

            workbook.save(file_path)
            return Response(True, "Excel file was created.")
        except Exception:
            return Response(False, "Export failed.")

    def export_pdf(self, employee, account, file_path: str, icon_path=None):
        if not self.is_banker(employee):
            return Response(False, "Access denied.")

        try:
            transactions = self.account_repository.get_transaction_by_account_id(account.id)
            styles = getSampleStyleSheet()
            elements = []

            if icon_path:
                elements.append(Image(icon_path, width=2.2 * cm, height=2.2 * cm, hAlign="CENTER"))
                elements.append(Spacer(1, 0.9 * cm))

            elements.append(Paragraph("Transaction Report", styles["Title"]))
            elements.append(Spacer(1, 1.0 * cm))
            elements.append(Paragraph(f"Report date: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles["Normal"]))
            elements.append(Paragraph(f"Account number: {account.account_number}", styles["Normal"]))
            elements.append(Paragraph(f"Owner: {account.owner_customer.get_fullname()}", styles["Normal"]))
            elements.append(Spacer(1, 1.4 * cm))

            data = [("#", "Date", "Type", "Amount")] + [
                (index, t.created_at.strftime("%Y-%m-%d %H:%M"), t.transaction_type.name.title(), f"{t.amount:,.0f}")
                for index, t in enumerate(transactions, start=1)
            ]

            table = Table(data, colWidths=[2.0 * cm, 6.4 * cm, 4.6 * cm, 5.0 * cm], repeatRows=1)
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#375A7F")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 14),
                ("TOPPADDING", (0, 0), (-1, -1), 12),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey])
            ]))
            elements.append(table)

            SimpleDocTemplate(file_path, pagesize=A4, leftMargin=1.5 * cm, rightMargin=1.5 * cm).build(elements)
            return Response(True, "PDF file was created.")
        except Exception:
            return Response(False, "Export failed.")