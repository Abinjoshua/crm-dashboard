# -*- coding: utf-8 -*-
from odoo import models, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def get_tiles_data(self):
        company_id = self.env.company
        leads = self.search([('company_id', '=', company_id.id),
                             ('user_id', '=', self.env.user.id)])
        my_leads = leads.filtered(lambda r: r.type == 'lead')
        my_opportunity = leads.filtered(lambda r: r.type == 'opportunity')
        currency = company_id.currency_id.symbol
        expected_revenue = sum(my_opportunity.mapped('expected_revenue'))
        won_lead = leads.search([('stage_id', '=', 4), ])
        revenue = sum(won_lead.mapped('expected_revenue'))
        win_ratio = int((len(won_lead) / len(leads)) * 100)


        lost_leads = self.read_group(
            [('active', '=', False),
             ('probability', '=', 0),
             ('user_id', '=', self.env.user.id)],
            ['name'],
            ['name']
        )

        lost_leads_labels = []
        lost_leads_values = []

        for lost_lead in lost_leads:
            lost_leads_labels.append(lost_lead['name'])
            lost_leads_values.append(lost_lead['name_count'])

        activity_data = self.env['mail.activity'].read_group(
            [('user_id', '=', self.env.user.id)],
            ['activity_type_id'],
            ['activity_type_id']
        )

        activity_labels = []
        activity_values = []

        for activity in activity_data:
            activity_labels.append(activity['activity_type_id'][1])
            activity_values.append(activity['activity_type_id_count'])

        campaign_leads = self.read_group(
            [('user_id', '=', self.env.user.id)],
            ['campaign_id'],
            ['campaign_id']
        )

        campaign_leads_labels = []
        campaign_leads_values = []

        for campaign_lead in campaign_leads:
            campaign_leads_labels.append(campaign_lead['campaign_id'][1])
            campaign_leads_values.append(campaign_lead['campaign_id_count'])

        leads_medium = self.read_group(
            [('user_id', '=', self.env.user.id)],
            ['medium_id'],
            ['medium_id']
        )

        medium_labels = []
        medium_values = []

        for medium in leads_medium:
            medium_labels.append(medium['medium_id'][1])
            medium_values.append(medium['medium_id_count'])

        print('mediums labels',medium_labels)
        print('mediums values',medium_values)

        return {
            'total_leads': len(my_leads),
            'total_opportunity': len(my_opportunity),
            'expected_revenue': expected_revenue,
            'currency': currency,
            'revenue': revenue,
            'win_ratio': str(win_ratio) + "%",
            'activity_labels': activity_labels,
            'activity_values': activity_values,
            'lost_leads_labels': lost_leads_labels,
            'lost_leads_values': lost_leads_values,
            'campaign_leads_labels': campaign_leads_labels,
            'campaign_leads_values': campaign_leads_values
        }
