# -*- coding: utf-8 -*-

from odoo import models, fields, api

class invest(models.Model):
    _name = 'invest.invest'

    code = fields.Char()
    rubriques = fields.Char()
    report_et_anterieurs = fields.Char()
    nouveaux_credits = fields.Float()
    total_credits = fields.Float()
    credits_dengagement = fields.Float()
