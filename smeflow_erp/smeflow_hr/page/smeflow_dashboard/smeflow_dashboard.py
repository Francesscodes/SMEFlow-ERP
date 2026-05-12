import frappe

@frappe.whitelist()
def get_dashboard_data():
    total_employees = frappe.db.count("SME Employee", {"status": "Active"})
    
    today = frappe.utils.today()
    present_today = frappe.db.count("SME Attendance", {"attendance_date": today, "status": "Present"})
    absent_today = frappe.db.count("SME Attendance", {"attendance_date": today, "status": "Absent"})
    
    pending_leaves = frappe.db.count("SME Leave Application", {"status": "Open"})
    
    unpaid_payroll = frappe.db.count("SME Payroll", {"payment_status": "Unpaid"})
    
    pending_expenses = frappe.db.count("SME Expense Claim", {"status": "Pending Approval"})
    
    return {
        "total_employees": total_employees,
        "present_today": present_today,
        "absent_today": absent_today,
        "pending_leaves": pending_leaves,
        "unpaid_payroll": unpaid_payroll,
        "pending_expenses": pending_expenses
    }
