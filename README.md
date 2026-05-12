# SMEFlow ERP

A lightweight HR and operations management system built on [Frappe Framework](https://frappeframework.com), designed for small and medium-sized enterprises (SMEs) in Africa.

## Features

- **Employee Management** — maintain staff records, designations, and employment details
- **Attendance Tracking** — log daily attendance with check-in/check-out times
- **Leave Management** — apply for and approve leave with auto day calculation
- **Payroll Engine** — process monthly payroll with allowances, deductions, and auto gross/net pay calculation
- **Expense Claims** — submit and approve staff expense claims by category

## Tech Stack

- [Frappe Framework](https://frappeframework.com) v15
- [ERPNext](https://erpnext.com) v15
- Python 3
- MariaDB

## Installation

```bash
cd ~/frappe-bench
bench get-app https://github.com/Francesscodes/SMEFlow-ERP.git
bench --site your-site-name install-app smeflow_erp
bench --site your-site-name migrate
```

## User Roles

| Role | Access |
|---|---|
| SME HR Manager | Full access to all modules |
| SME Finance | Payroll and Expense management |
| SME Employee | Submit leave and expense claims |

## Built By

[Francess Ekezie](https://github.com/Francesscodes) — Backend Engineer & Technical Product Manager