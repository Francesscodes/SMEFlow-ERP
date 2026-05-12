import frappe
from frappe.model.document import Document

class SMEInternPayroll(Document):
    def before_save(self):
        stipend = self.monthly_stipend or 0
        transport = self.transport_allowance or 0
        meal = self.meal_allowance or 0
        absent_deduction = self.deduction_for_absence or 0

        if self.days_worked and self.days_absent and stipend:
            total_days = self.days_worked + self.days_absent
            daily_rate = stipend / total_days if total_days > 0 else 0
            self.deduction_for_absence = round(daily_rate * self.days_absent, 2)
            absent_deduction = self.deduction_for_absence

        self.total_payable = round(stipend + transport + meal - absent_deduction, 2)
