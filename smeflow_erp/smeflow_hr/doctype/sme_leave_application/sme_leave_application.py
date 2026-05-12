import frappe
from frappe.model.document import Document

class SMELeaveApplication(Document):
    def before_save(self):
        if self.from_date and self.to_date:
            from frappe.utils import date_diff
            self.total_days = date_diff(self.to_date, self.from_date) + 1

def send_leave_notification(doc, method):
    try:
        # Get HR Manager emails
        hr_managers = frappe.get_all("Has Role",
            filters={"role": "SME HR Manager", "parenttype": "User"},
            fields=["parent"]
        )
        
        recipients = [u.parent for u in hr_managers if u.parent != "Guest"]
        
        if not recipients:
            recipients = [frappe.session.user]

        subject = f"Leave Application: {doc.employee} - {doc.leave_type}"
        
        message = f"""
        <div style="font-family: Arial, sans-serif; padding: 20px;">
            <h3 style="color: #1a1a2e;">New Leave Application Submitted</h3>
            <table style="width:100%; border-collapse: collapse;">
                <tr><td style="padding:8px; font-weight:bold;">Employee:</td><td>{doc.employee}</td></tr>
                <tr><td style="padding:8px; font-weight:bold;">Leave Type:</td><td>{doc.leave_type}</td></tr>
                <tr><td style="padding:8px; font-weight:bold;">From:</td><td>{doc.from_date}</td></tr>
                <tr><td style="padding:8px; font-weight:bold;">To:</td><td>{doc.to_date}</td></tr>
                <tr><td style="padding:8px; font-weight:bold;">Total Days:</td><td>{doc.total_days}</td></tr>
                <tr><td style="padding:8px; font-weight:bold;">Reason:</td><td>{doc.reason or 'Not provided'}</td></tr>
            </table>
            <p style="margin-top:16px; color:#666;">Please log in to SMEFlow ERP to approve or reject this request.</p>
        </div>
        """

        frappe.sendmail(
            recipients=recipients,
            subject=subject,
            message=message
        )
        frappe.logger().info(f"Leave notification sent for {doc.employee}")

    except Exception as e:
        frappe.logger().error(f"Leave notification failed: {str(e)}")
