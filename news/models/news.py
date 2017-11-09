# -*- coding: utf-8 -*-

from datetime import datetime

from odoo import api, fields, models


class News(models.Model):

    _name = 'tmc.news'
    _description = 'News'

    _order = 'create_date desc'

    _states_ = [
        ('published', 'Published'),
        ('draft', 'Draft'),
    ]

    name = fields.Char(
        string='Title',
        size=60,
        required=True
    )

    description = fields.Char(
        size=140,
        required=True
    )

    state = fields.Selection(
        selection=_states_,
        default='draft'
    )

    link = fields.Char(
        size=120
    )

    date_deadline = fields.Date(
        required=True,
        default=fields.Date.context_today
    )

    important = fields.Boolean(
        default=False
    )

    office_id = fields.Many2one(
        comodel_name='tmc.hr.office'
    )

    @api.multi
    def action_draft(self):
        self.ensure_one()
        self.state = 'draft'

    @api.multi
    def action_publish(self):
        self.ensure_one()
        self.state = 'published'

    @api.multi
    def get_news(self):
        for new in self:
            res = {}
            res['title'] = new.name
            res['description'] = new.description

            create_date = datetime.strptime(
                new.create_date, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%y %H:%M')
            res['create_date'] = create_date

            if new.link:
                res['link'] = new.link
            if new.important:
                res['important'] = new.important

            return res
