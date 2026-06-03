# -*- coding: utf-8 -*-
from odoo import models, fields


class CrmTeam(models.Model):
    _inherit = 'crm.team'

    crm_lead_state = fields.Many2one('crm.stage','CRM Lead State')