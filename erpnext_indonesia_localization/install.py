import frappe
from frappe.utils import now


def initialize_vat_account_in_default_indonesian_coa():
	"""
	This method would run after ERPNext installed while the is being installed
	This method would create an account as VAT In and Out
	"""

	global_company = frappe.db.get_single_value("Global Defaults", "default_company")

	account_data = [
		# {
		# 	"account_currency": "IDR",
		# 	"account_name": "Hutang Pajak",
		# 	"account_number": "2140.000",
		# 	"company": global_company,
		# 	"doctype": "Account",
		# 	"is_group": 1,
		# 	"root_type": "Liability",
		# 	"report_type": "Balance Sheet",
		# 	"parent_account": "2100.000 - Pasiva Lancar - EI",
		# 	"freeze_account": "No"
		# },
		{
			"account_currency": "IDR",
			"account_name": "Hutang Pajak",
			"account_number": "2141.000",
			"company": global_company,
			"doctype": "Account",
			"is_group": 1,
			"root_type": "Liability",
			"report_type": "Balance Sheet",
			"parent_account": "2100.000 - Pasiva Lancar - EI",
			"freeze_account": "No"
		}
	]