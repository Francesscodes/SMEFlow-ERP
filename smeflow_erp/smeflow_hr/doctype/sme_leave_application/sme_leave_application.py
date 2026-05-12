import frappe
from frappe.model.document import Document

class SMELeaveApplication(Document):
    def before_save(self):
        if self.from_date and self.to_date:
            from frappe.utils import date_diff
            self.total_days = date_diff(self.to_date, self.from_date) + 1
