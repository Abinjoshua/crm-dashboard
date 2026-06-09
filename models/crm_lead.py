# -*- coding: utf-8 -*-
from odoo import models, api
import datetime


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        print('working')
        print(self.create_date)
        print(self.probability)

    @api.model
    def get_tiles_data(self, date):

        if date:
            company_id = self.env.company
            if date == 'Year':
                current_year = datetime.date.today().year
                start_date = datetime.datetime(current_year, 1, 1)
                end_date = datetime.datetime(current_year + 1, 1, 1)
                print('current year', current_year)
                print('current year start date', start_date)
                print('current year end date', end_date)
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id),
                                     ('create_date', '>=', start_date),
                                     ('create_date', '<', end_date)
                                     ])
                lost_leads = self.read_group(
                    [('active', '=', False),
                     ('probability', '=', 0),
                     ('user_id', '=', self.env.user.id),
                     ('create_date', '>=', start_date),
                     ('create_date', '<', end_date), ],
                    ['name'],
                    ['name']
                )
                activity_data = self.env['mail.activity'].read_group(
                    [('user_id', '=', self.env.user.id),
                     ('create_date', '>=', start_date),
                     ('create_date', '<', end_date)
                     ],
                    ['activity_type_id'],
                    ['activity_type_id']
                )
                campaign_leads = self.read_group(
                    [('user_id', '=', self.env.user.id),
                     ('create_date', '>=', start_date),
                     ('create_date', '<', end_date)
                     ],
                    ['campaign_id'],
                    ['campaign_id']
                )
                leads_medium = self.read_group(
                    [('user_id', '=', self.env.user.id),
                     ('create_date', '>=', start_date),
                     ('create_date', '<', end_date)
                     ],
                    ['medium_id'],
                    ['medium_id']
                )
                print('lost leads', lost_leads)
            elif date == 'Quarter':
                current_year = datetime.date.today().year
                current_month = datetime.date.today().month
                print('current month', current_month)
                if current_month in [1, 2, 3]:
                    start_date = datetime.datetime(current_year, 1, 1)
                    end_date = datetime.datetime(current_year, 4, 1)
                    quarter = 1
                    leads = self.search([('company_id', '=', company_id.id),
                                         ('user_id', '=', self.env.user.id),
                                         ('create_date', '>=', start_date),
                                         ('create_date', '<', end_date)
                                         ])
                    lost_leads = self.read_group(
                        [('active', '=', False),
                         ('probability', '=', 0),
                         ('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date), ],
                        ['name'],
                        ['name']
                    )
                    activity_data = self.env['mail.activity'].read_group(
                        [('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date)
                         ],
                        ['activity_type_id'],
                        ['activity_type_id']
                    )
                    campaign_leads = self.read_group(
                        [('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date)
                         ],
                        ['campaign_id'],
                        ['campaign_id']
                    )
                    leads_medium = self.read_group(
                        [('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date)
                         ],
                        ['medium_id'],
                        ['medium_id']
                    )
                elif current_month in [4, 5, 6]:
                    start_date = datetime.datetime(current_year, 4, 1)
                    end_date = datetime.datetime(current_year, 7, 1)
                    quarter = 2
                    leads = self.search([('company_id', '=', company_id.id),
                                         ('user_id', '=', self.env.user.id),
                                         ('create_date', '>=', start_date),
                                         ('create_date', '<', end_date)
                                         ])
                    lost_leads = self.read_group(
                        [('active', '=', False),
                         ('probability', '=', 0),
                         ('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date), ],
                        ['name'],
                        ['name']
                    )
                    activity_data = self.env['mail.activity'].read_group(
                        [('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date)
                         ],
                        ['activity_type_id'],
                        ['activity_type_id']
                    )
                    campaign_leads = self.read_group(
                        [('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date)
                         ],
                        ['campaign_id'],
                        ['campaign_id']
                    )
                    leads_medium = self.read_group(
                        [('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date)
                         ],
                        ['medium_id'],
                        ['medium_id']
                    )
                elif current_month in [7, 8, 9]:
                    start_date = datetime.datetime(current_year, 7, 1)
                    end_date = datetime.datetime(current_year, 10, 1)
                    quarter = 3
                    leads = self.search([('company_id', '=', company_id.id),
                                         ('user_id', '=', self.env.user.id),
                                         ('create_date', '>=', start_date),
                                         ('create_date', '<', end_date)
                                         ])
                    lost_leads = self.read_group(
                        [('active', '=', False),
                         ('probability', '=', 0),
                         ('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date), ],
                        ['name'],
                        ['name']
                    )
                    activity_data = self.env['mail.activity'].read_group(
                        [('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date)
                         ],
                        ['activity_type_id'],
                        ['activity_type_id']
                    )
                    campaign_leads = self.read_group(
                        [('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date)
                         ],
                        ['campaign_id'],
                        ['campaign_id']
                    )
                    leads_medium = self.read_group(
                        [('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date)
                         ],
                        ['medium_id'],
                        ['medium_id']
                    )
                elif current_month in [10, 11, 12]:
                    start_date = datetime.datetime(current_year, 10, 1)
                    end_date = datetime.datetime(current_year, 12, 1)
                    quarter = 4
                    leads = self.search([('company_id', '=', company_id.id),
                                         ('user_id', '=', self.env.user.id),
                                         ('create_date', '>=', start_date),
                                         ('create_date', '<', end_date)
                                         ])
                    lost_leads = self.read_group(
                        [('active', '=', False),
                         ('probability', '=', 0),
                         ('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date), ],
                        ['name'],
                        ['name']
                    )
                    activity_data = self.env['mail.activity'].read_group(
                        [('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date)
                         ],
                        ['activity_type_id'],
                        ['activity_type_id']
                    )
                    campaign_leads = self.read_group(
                        [('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date)
                         ],
                        ['campaign_id'],
                        ['campaign_id']
                    )
                    leads_medium = self.read_group(
                        [('user_id', '=', self.env.user.id),
                         ('create_date', '>=', start_date),
                         ('create_date', '<', end_date)
                         ],
                        ['medium_id'],
                        ['medium_id']
                    )

            elif date == 'Month':
                current_date = datetime.date.today()
                start_date = datetime.datetime(current_date.year, current_date.month, 1)
                if current_date.month == 12:
                    end_date = datetime.datetime(current_date.year + 1, 1, 1)
                else:
                    end_date = datetime.datetime(current_date.year, current_date.month + 1, 1)
                print('current month start date', start_date)
                print('current month end date', end_date)
                print('current date', current_date)
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id),
                                     ('create_date', '>=', start_date),
                                     ('create_date', '<', end_date)
                                     ])
                lost_leads = self.read_group(
                    [('active', '=', False),
                     ('probability', '=', 0),
                     ('user_id', '=', self.env.user.id),
                     ('create_date', '>=', start_date),
                     ('create_date', '<', end_date), ],
                    ['name'],
                    ['name']
                )
                activity_data = self.env['mail.activity'].read_group(
                    [('user_id', '=', self.env.user.id),
                     ('create_date', '>=', start_date),
                     ('create_date', '<', end_date)
                     ],
                    ['activity_type_id'],
                    ['activity_type_id']
                )
                campaign_leads = self.read_group(
                    [('user_id', '=', self.env.user.id),
                     ('create_date', '>=', start_date),
                     ('create_date', '<', end_date)
                     ],
                    ['campaign_id'],
                    ['campaign_id']
                )
                leads_medium = self.read_group(
                    [('user_id', '=', self.env.user.id),
                     ('create_date', '>=', start_date),
                     ('create_date', '<', end_date)
                     ],
                    ['medium_id'],
                    ['medium_id']
                )
                print('lost leads by month', lost_leads)
            elif date == 'Week':
                current_date = datetime.date.today()
                week_num = current_date.isocalendar()[1]
                start_date = datetime.datetime(current_date.year, current_date.month, current_date.day - 7)
                end_date = datetime.datetime(current_date.year, current_date.month, current_date.day)
                leads = self.search([('company_id', '=', company_id.id),
                                     ('user_id', '=', self.env.user.id),
                                     ('create_date', '>=', start_date),
                                     ('create_date', '<', end_date)
                                     ])
                lost_leads = self.read_group(
                    [('active', '=', False),
                     ('probability', '=', 0),
                     ('user_id', '=', self.env.user.id),
                     ('create_date', '>=', start_date),
                     ('create_date', '<', end_date), ],
                    ['name'],
                    ['name']
                )
                activity_data = self.env['mail.activity'].read_group(
                    [('user_id', '=', self.env.user.id),
                     ('create_date', '>=', start_date),
                     ('create_date', '<', end_date)
                     ],
                    ['activity_type_id'],
                    ['activity_type_id']
                )
                campaign_leads = self.read_group(
                    [('user_id', '=', self.env.user.id),
                     ('create_date', '>=', start_date),
                     ('create_date', '<', end_date)
                     ],
                    ['campaign_id'],
                    ['campaign_id']
                )
                leads_medium = self.read_group(
                    [('user_id', '=', self.env.user.id),
                     ('create_date', '>=', start_date),
                     ('create_date', '<', end_date)
                     ],
                    ['medium_id'],
                    ['medium_id']
                )
                print('week', week_num)

        else:
            company_id = self.env.company
            leads = self.search([('company_id', '=', company_id.id),
                                 ('user_id', '=', self.env.user.id)])

            lost_leads = self.read_group(
                [('active', '=', False),
                 ('probability', '=', 0),
                 ('user_id', '=', self.env.user.id)],
                ['name'],
                ['name']
            )
            activity_data = self.env['mail.activity'].read_group(
                [('user_id', '=', self.env.user.id)],
                ['activity_type_id'],
                ['activity_type_id']
            )
            campaign_leads = self.read_group(
                [('user_id', '=', self.env.user.id)],
                ['campaign_id'],
                ['campaign_id']
            )
            leads_medium = self.read_group(
                [('user_id', '=', self.env.user.id)],
                ['medium_id'],
                ['medium_id']
            )

        my_leads = leads.filtered(lambda r: r.type == 'lead')
        my_opportunity = leads.filtered(lambda r: r.type == 'opportunity')
        currency = company_id.currency_id.symbol
        expected_revenue = sum(my_opportunity.mapped('expected_revenue'))
        won_lead = leads.search([('stage_id', '=', 4), ])
        revenue = sum(won_lead.mapped('expected_revenue'))
        win_ratio = int((len(won_lead) / len(leads)) * 100)
        print('Win Ratio',type(win_ratio))

        lost_leads_labels = []
        lost_leads_values = []

        for lost_lead in lost_leads:
            lost_leads_labels.append(lost_lead['name'])
            lost_leads_values.append(lost_lead['name_count'])

        activity_labels = []
        activity_values = []

        for activity in activity_data:
            activity_labels.append(activity['activity_type_id'][1])
            activity_values.append(activity['activity_type_id_count'])

        campaign_leads_labels = []
        campaign_leads_values = []

        for campaign_lead in campaign_leads:
            campaign_leads_labels.append(campaign_lead['campaign_id'][1])
            campaign_leads_values.append(campaign_lead['campaign_id_count'])

        medium_labels = []
        medium_values = []

        for medium in leads_medium:
            medium_labels.append(medium['medium_id'][1])
            medium_values.append(medium['medium_id_count'])

        print('mediums labels', medium_labels)
        print('mediums values', medium_values)

        return {
            'total_leads': len(my_leads),
            'total_leads_label':'Total Leads',
            'total_opportunity': len(my_opportunity),
            'total_opportunity_label': 'Total Opportunity',
            'expected_revenue': expected_revenue,
            'expected_revenue_label': 'Expected Revenue',
            'currency': currency,
            'revenue': revenue,
            'revenue_label': 'Revenue Label',
            'win_ratio': str(win_ratio) + "%",
            'win_ratio_int': win_ratio,
            'win_ratio_label': "Win Ratio",
            'activity_labels': activity_labels,
            'activity_values': activity_values,
            'lost_leads_labels': lost_leads_labels,
            'lost_leads_values': lost_leads_values,
            'campaign_leads_labels': campaign_leads_labels,
            'campaign_leads_values': campaign_leads_values,
            'medium_labels': medium_labels,
            'medium_values': medium_values,
        }
