import frappe
from frappe.model.document import Document

class SMEPAYEBand(Document):
    pass

def get_paye_tax(annual_income):
    """Calculate PAYE tax based on Nigerian tax bands"""
    bands = frappe.get_all("SME PAYE Band",
        fields=["min_income", "max_income", "tax_rate"],
        order_by="min_income asc"
    )
    
    total_tax = 0
    for band in bands:
        if annual_income <= 0:
            break
        band_min = band.min_income or 0
        band_max = band.max_income or float('inf')
        taxable_in_band = min(annual_income, band_max) - band_min
        if taxable_in_band > 0:
            total_tax += taxable_in_band * (band.tax_rate / 100)
    
    return round(total_tax / 12, 2)  # Return monthly PAYE
