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
        self.ensure_one()
        res = {}
        res['title'] = self.name
        res['description'] = self.description

        create_date = datetime.strptime(
            self.create_date, '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%y %H:%M')
        res['create_date'] = create_date

        if self.link:
            res['link'] = self.link
        if self.important:
            res['important'] = self.important

        return res
