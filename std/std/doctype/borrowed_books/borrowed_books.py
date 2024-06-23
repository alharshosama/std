# Copyright (c) 2024, std and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
# class BorrowedBooks(Document):
#     def validate(self):
#         if self.status != self.return_date:
#             frappe.throw("The Status is be borrow the book")
class BorrowedBooks(Document):
    def validate(self):
        if self.status == 'borrow' and self.return_date <= self.borrow_date:
            frappe.throw("Loan must be settled before returning")
        elif self.status == 'return' and self.return_date > self.borrow_date:
            frappe.throw("Loan cannot be returned after the loan expiration date")