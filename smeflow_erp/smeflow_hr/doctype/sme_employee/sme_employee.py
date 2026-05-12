import frappe
from frappe.model.document import Document

class SMEEmployee(Document):
    def before_save(self):
        self.full_name = self.full_name.strip().title()
