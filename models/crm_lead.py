# -*- coding: utf-8 -*-
from odoo import models, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def get_tiles_data(self):
        # print('r')
        company_id = self.env.company
        leads = self.search([('company_id', '=', company_id.id),
                             ('user_id', '=', self.env.user.id)])
        # print(leads)
        my_leads = leads.filtered(lambda r: r.type == 'lead')
        my_opportunity = leads.filtered(lambda r: r.type == 'opportunity')
        currency = company_id.currency_id.symbol
        expected_revenue = sum(my_opportunity.mapped('expected_revenue'))
        won_lead = leads.search([('stage_id', '=', 4),])
        # print(won_lead)
        revenue = sum(won_lead.mapped('expected_revenue'))
        # print(revenue)
        win_ratio = int((len(won_lead) / len(leads)) * 100)
        # print('win_ratio',win_ratio)
        lost_leads = leads.search([('active', '=', False),
                                   ('probability','=',0),
                                   ('user_id', '=', self.env.user.id)])
        lost_leads_name = lost_leads.mapped('name')
        return {
            'total_leads': len(my_leads),
            'total_opportunity': len(my_opportunity),
            'expected_revenue': expected_revenue,
            'currency': currency,
            'revenue': revenue,
            'win_ratio': str(win_ratio)+"%",
            'lost_leads': lost_leads_name,
        }
