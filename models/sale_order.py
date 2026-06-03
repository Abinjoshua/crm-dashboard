# -*- coding: utf-8 -*-
from odoo import models


class SalesOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        if self.opportunity_id:
            self.opportunity_id.write({'stage_id':4})
            return super().action_confirm()


