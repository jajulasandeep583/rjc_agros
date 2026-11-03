## RJC Agros

Customisations for **RJC AGROS LIMITED** on ERPNext v16.

### What it adds

Read-only fields that link every record migrated from Tally (company 010068, books 1 April 2011 to 21 October 2026) back to its Tally original:

| DocType | Fields |
| --- | --- |
| Journal Entry, Purchase Invoice, Payment Entry | Tally Voucher Type, Tally Voucher No, Tally Reference, Tally GUID (unique) |
| Supplier, Customer | Tally Ledger, Tally Group |
| Account | Tally Name |

The fields are created on install and re-applied on every `bench migrate` (`rjc_agros/setup/custom_fields.py`). They are empty on new transactions.

### Requirements

- Frappe 16, ERPNext 16, India Compliance 16 (HRMS 16 is also installed on the RJC site)

### Installation

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/jajulasandeep583/rjc_agros --branch version-16
bench --site <site> install-app rjc_agros
```

To restore the RJC site backup, install erpnext, hrms, india_compliance and rjc_agros on the new site first, then restore the database and files.

### License

mit
