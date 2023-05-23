# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import fields, models


class CollegeLocation(models.Model):
    _name = 'college.location'
    _rec_name = 'country_id'

    country_id = fields.Many2one('res.country', string="Country", required=True)
    description = fields.Text(string='Description', required=True)
    image = fields.Image(string='Image', required=True)
    location = fields.Char(string='Location', required=True)
    phone = fields.Char(string='Phone', required=True)
    email = fields.Char(string='Email', required=True)
    about_us = fields.Text(string='About Us', required=True)
