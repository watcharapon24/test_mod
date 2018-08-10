from odoo import api

def migrate(cr, version):
    print("end-migrate")
    env=api.Environment(cr, 1, {})

    res=env['test.employee'].search([])
    if not res:
        res2=env['test.department'].search([])
        if not res2:
            department=env['test.department'].create({'name': 'My Department'})
            vals={
                'name': 'Demo',
                'department_id': department.id,
            }
            employee=env['test.employee'].create(vals)
