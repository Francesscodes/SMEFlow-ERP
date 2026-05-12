import frappe
from frappe.model.document import Document

class SMESalaryAdvance(Document):
    def before_save(self):
        if self.amount and self.repayment_months:
            self.monthly_deduction = round(self.amount / self.repayment_months, 2)
            self.outstanding_amount = self.amount - (self.amount_repaid or 0)
        if self.outstanding_amount == 0:
            self.status = "Fully Repaid"

    def on_submit(self):
        if self.status == "Draft":
            self.status = "Pending Approval"
            self.save()
