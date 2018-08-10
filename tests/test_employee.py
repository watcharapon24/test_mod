from odoo.tests import common

class TestEmployee(common.TransactionCase):
    
    def test_employee(self):
        cond=[]
        vals={
            'name': 'Watcharapon',
        }
        employee=self.env['test.employee'].create(vals)
        self.assertEquals(employee.name, vals['name'])
