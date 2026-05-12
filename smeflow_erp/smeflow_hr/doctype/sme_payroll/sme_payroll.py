import frappe
from frappe.model.document import Document

class SMEPayroll(Document):
    def before_save(self):
        self.gross_pay = (
            (self.basic_salary or 0) +
            (self.transport_allowance or 0) +
            (self.housing_allowance or 0) +
            (self.other_allowances or 0)
        )
        self.net_pay = self.gross_pay - (
            (self.tax_deduction or 0) +
            (self.pension_deduction or 0) +
            (self.other_deductions or 0)
        )
