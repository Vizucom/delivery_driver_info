# -*- coding: utf-8 -*-
from openerp import models, fields


class StockPicking(models.Model):

    _inherit = 'stock.picking'

    driver = fields.Char('Driver')
