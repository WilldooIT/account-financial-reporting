# -*- coding: utf-8 -*-
# © 2014-2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class Report(models.Model):
    _inherit = 'report'

    @api.model
    def get_html(self, docids, report_name, data=None):
        # For mis_builder report must put parameter values into the context
        # before report is rendered.
        if report_name == 'mis_builder.report_mis_report_instance':
            if len(docids) == 1:
                doc = self.env['mis.report.instance'].browse(docids[0])
                self = self.with_context(mis_param_vals=doc._param_vals())

        return super(Report, self).get_html(docids, report_name, data=data)
