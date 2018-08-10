from odoo import models, fields, api

class Employee(models.Model):
    _name="test.employee"
    
    name = fields.Char("Name", required=True)
    department_id = fields.Many2one("test.department","Department")
