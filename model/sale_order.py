from openerp import models, fields, api
import datetime
from datetime import date

class sale_order_improvements(models.Model):
    _inherit = ['sale.order']
    
    partner_invoice_id = fields.Many2one('res.partner', readonly=False)
    
    def action_button_confirm(self, cr, uid, ids, context=None):
        super(sale_order_improvements, self).action_button_confirm(cr, uid, ids, context=context)
        self.pool.get('sale.order').write(cr, uid, ids, {'date_order': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),})
        return True
