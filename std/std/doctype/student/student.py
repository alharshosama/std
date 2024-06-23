# Copyright (c) 2024, std and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Student(Document):
    def validate(self):
        if self.age <= 18:
            frappe.throw("Student's age must be at least 18")

    def before_save(self):
        self.full_name = f"{self.first_name} {self.last_name}"

    # def after_insert(self):
    #     frappe.sendmail(recipients=[self.email], message="Thank you for registering!")  