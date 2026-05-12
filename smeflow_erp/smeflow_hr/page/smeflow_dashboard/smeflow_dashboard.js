frappe.pages['smeflow-dashboard'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'SMEFlow Dashboard',
        single_column: true
    });

    var d = {
        total_employees: 25,
        present_today: 18,
        absent_today: 7,
        pending_leaves: 3,
        unpaid_payroll: "₦2,450,000",
        pending_expenses: 5
    };

    var html = '<div style="padding:20px;">';
    html += '<h2 style="margin-bottom:24px;color:#1a1a2e;font-size:22px;">SMEFlow HR Overview</h2>';
    html += '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-bottom:30px;">';
    html += '<div style="background:linear-gradient(135deg,#667eea,#764ba2);border-radius:12px;padding:24px;color:white;"><div style="font-size:13px;margin-bottom:8px;">Total Employees</div><div style="font-size:42px;font-weight:700;">' + d.total_employees + '</div><div style="font-size:12px;opacity:0.7;margin-top:4px;">Active staff</div></div>';
    html += '<div style="background:linear-gradient(135deg,#11998e,#38ef7d);border-radius:12px;padding:24px;color:white;"><div style="font-size:13px;margin-bottom:8px;">Present Today</div><div style="font-size:42px;font-weight:700;">' + d.present_today + '</div><div style="font-size:12px;opacity:0.7;margin-top:4px;">Checked in</div></div>';
    html += '<div style="background:linear-gradient(135deg,#f7971e,#ffd200);border-radius:12px;padding:24px;color:white;"><div style="font-size:13px;margin-bottom:8px;">Absent Today</div><div style="font-size:42px;font-weight:700;">' + d.absent_today + '</div><div style="font-size:12px;opacity:0.7;margin-top:4px;">Not checked in</div></div>';
    html += '<div style="background:linear-gradient(135deg,#f953c6,#b91d73);border-radius:12px;padding:24px;color:white;"><div style="font-size:13px;margin-bottom:8px;">Pending Leaves</div><div style="font-size:42px;font-weight:700;">' + d.pending_leaves + '</div><div style="font-size:12px;opacity:0.7;margin-top:4px;">Awaiting approval</div></div>';
    html += '<div style="background:linear-gradient(135deg,#4facfe,#00f2fe);border-radius:12px;padding:24px;color:white;"><div style="font-size:13px;margin-bottom:8px;">Unpaid Payroll</div><div style="font-size:32px;font-weight:700;">' + d.unpaid_payroll + '</div><div style="font-size:12px;opacity:0.7;margin-top:4px;">Pending payment</div></div>';
    html += '<div style="background:linear-gradient(135deg,#fa709a,#fee140);border-radius:12px;padding:24px;color:white;"><div style="font-size:13px;margin-bottom:8px;">Pending Expenses</div><div style="font-size:42px;font-weight:700;">' + d.pending_expenses + '</div><div style="font-size:12px;opacity:0.7;margin-top:4px;">Awaiting approval</div></div>';
    html += '</div>';
    html += '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;">';
    html += '<a href="/app/sme-employee" style="background:white;border:1px solid #e2e8f0;border-radius:10px;padding:16px;text-align:center;text-decoration:none;color:#4a5568;font-weight:500;">Manage Employees</a>';
    html += '<a href="/app/sme-attendance" style="background:white;border:1px solid #e2e8f0;border-radius:10px;padding:16px;text-align:center;text-decoration:none;color:#4a5568;font-weight:500;">Log Attendance</a>';
    html += '<a href="/app/sme-leave-application" style="background:white;border:1px solid #e2e8f0;border-radius:10px;padding:16px;text-align:center;text-decoration:none;color:#4a5568;font-weight:500;">Leave Applications</a>';
    html += '<a href="/app/sme-payroll" style="background:white;border:1px solid #e2e8f0;border-radius:10px;padding:16px;text-align:center;text-decoration:none;color:#4a5568;font-weight:500;">Run Payroll</a>';
    html += '<a href="/app/sme-expense-claim" style="background:white;border:1px solid #e2e8f0;border-radius:10px;padding:16px;text-align:center;text-decoration:none;color:#4a5568;font-weight:500;">Expense Claims</a>';
    html += '<a href="/app/smeflow-hr" style="background:white;border:1px solid #e2e8f0;border-radius:10px;padding:16px;text-align:center;text-decoration:none;color:#4a5568;font-weight:500;">HR Workspace</a>';
    html += '</div></div>';

    $(wrapper).find('.layout-main-section').html(html);
}
