from odoo import models, fields, api

class Department(models.Model):
    _name="test.department"

    name=fields.Char("Name", required=True)
