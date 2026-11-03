"""Custom fields owned by the RJC Agros app (Tally migration traceability)."""

MODULE = "RJC Agros"


def _tally_section(insert_after):
	return [
		dict(fieldname="tally_section", label="Tally", fieldtype="Section Break", insert_after=insert_after, collapsible=1),
		dict(fieldname="tally_voucher_type", label="Tally Voucher Type", fieldtype="Data", insert_after="tally_section", read_only=1, in_standard_filter=1, no_copy=1),
		dict(fieldname="tally_voucher_no", label="Tally Voucher No", fieldtype="Data", insert_after="tally_voucher_type", read_only=1, in_standard_filter=1, no_copy=1),
		dict(fieldname="tally_reference", label="Tally Reference", fieldtype="Data", insert_after="tally_voucher_no", read_only=1, no_copy=1),
		dict(fieldname="tally_guid", label="Tally GUID", fieldtype="Data", insert_after="tally_reference", read_only=1, unique=1, no_copy=1),
	]


_party = [
	dict(fieldname="tally_ledger", label="Tally Ledger", fieldtype="Data", insert_after="tax_id", read_only=1, no_copy=1),
	dict(fieldname="tally_group", label="Tally Group", fieldtype="Data", insert_after="tally_ledger", read_only=1, no_copy=1),
]


def get_custom_fields():
	fields = {
		"Journal Entry": _tally_section("user_remark"),
		"Purchase Invoice": _tally_section("remarks"),
		"Payment Entry": _tally_section("remarks"),
		"Supplier": _party,
		"Customer": _party,
		"Account": [dict(fieldname="tally_name", label="Tally Name", fieldtype="Data", insert_after="account_name", read_only=1, no_copy=1)],
	}
	for rows in fields.values():
		for f in rows:
			f["module"] = MODULE
	return fields
