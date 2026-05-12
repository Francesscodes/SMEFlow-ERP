import frappe
from frappe.model.document import Document

class SMEExpenseClaim(Document):
    def on_submit(self):
        if self.status == "Draft":
            self.status = "Pending Approval"
            self.save()
