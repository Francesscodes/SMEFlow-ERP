# SMEFlow ERP

A lightweight HR and operations management system built on [Frappe Framework](https://frappeframework.com), designed for small and medium-sized enterprises (SMEs) in Africa. Built from scratch as a custom Frappe app on top of ERPNext v15.

---

## Features

### Employee Management
Maintain complete staff records including designation, department, employment type, contact details, and employment status.

### Attendance Tracking
Log daily attendance per employee with check-in and check-out times. Statuses include Present, Absent, Half Day, and On Leave.

### Leave Management
Employees can apply for leave across multiple leave types (Annual, Sick, Maternity, Paternity, Unpaid). Total leave days are calculated automatically on submission.

### Payroll Engine
Process monthly payroll with basic salary, transport allowance, housing allowance, and other allowances. Gross pay and net pay are computed automatically after deductions (PAYE tax, pension, others).

### Expense Claims
Staff can submit expense claims by category (Travel, Meals, Supplies, Communication, etc.) with an approval workflow moving from Draft to Pending Approval to Approved/Paid.

### Analytics Dashboard
A real-time HR overview dashboard showing total active employees, today's attendance (present/absent), pending leave applications, unpaid payroll count, and pending expense claims — with quick-access links to every module.

---

## Tech Stack

- [Frappe Framework](https://frappeframework.com) v15
- [ERPNext](https://erpnext.com) v15
- Python 3.12
- MariaDB
- JavaScript (Frappe Page API)

---

## Installation

```bash
cd ~/frappe-bench
bench get-app https://github.com/Francesscodes/SMEFlow-ERP.git
bench --site your-site-name install-app smeflow_erp
bench --site your-site-name migrate
```

---

## App Structure

```
smeflow_erp/
└── smeflow_hr/
    ├── doctype/
    │   ├── sme_employee/
    │   ├── sme_attendance/
    │   ├── sme_leave_application/
    │   ├── sme_payroll/
    │   └── sme_expense_claim/
    └── page/
        └── smeflow_dashboard/
```

---

## User Roles

| Role | Access |
|---|---|
| SME HR Manager | Full access to all modules — create, edit, submit, delete |
| SME Finance | Payroll processing and expense claim approvals |
| SME Employee | Submit leave applications and expense claims, view own attendance |

---

## Dashboard

The SMEFlow Dashboard (`/app/smeflow-dashboard`) provides a real-time overview of:

- Total active employees
- Present and absent count for today
- Pending leave applications awaiting approval
- Unpaid payroll entries
- Expense claims pending approval

---

## Built By

[Francess Ekezie](https://github.com/Francesscodes) — Backend Engineer & Technical Product Manager  
Built as part of the Tech4Dev Women Techsters Initiative Backend Engineering track.