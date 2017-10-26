# -*- coding: utf-8 -*-
# © 2017 Elico Corp (https://www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class account_invoice(models.Model):
    _inherit = 'account.invoice'
    _order = 'date_due asc'

    stage_id = fields.Many2one('project.task.type', 'Stages',
                               domain=[('used_in_invoice', '=', True)])
    color = fields.Integer('Color Index', default=0)

    @api.multi
    def _read_group_stage_ids(self, domain, read_group_order=None,
                              access_rights_uid=None):
        stage_obj = self.env['project.task.type']
        order = stage_obj._order
        access_rights_uid = access_rights_uid or self._uid
        if read_group_order == 'stage_id desc':
            order = '%s desc' % order
        search_domain = []
        search_domain += [('id', 'in', self._ids)]
        stages = stage_obj._search(search_domain, order=order,
                                   access_rights_uid=access_rights_uid)
        result = stage_obj.search([('id', 'in', stages)]).name_get()
        # restore order of the search
        result.sort(lambda x, y: cmp(stages.index(x[0]),
                                     stages.index(y[0])))
        fold = {}
        for stage in stage_obj.browse(stages):
            fold[stage.id] = stage.fold or False
        return result, fold

    _group_by_full = {
        'stage_id': _read_group_stage_ids
    }
