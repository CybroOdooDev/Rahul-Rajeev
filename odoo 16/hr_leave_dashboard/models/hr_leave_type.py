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
from odoo import models, fields


class HRLeaveType(models.Model):
    _inherit = 'hr.leave.type'
    _description = 'Inheriting Time Off Module'

    leave_code = fields.Selection([('UL', 'UL'),
                                   ('SL', 'SL'),
                                   ('RL', 'RL'),
                                   ('NL', 'NL'),
                                   ('ML', 'ML'),
                                   ('FL', 'FL'),
                                   ('CL', 'CL'),
                                   ('PL', 'PL'),
                                   ('OL', 'OL'),
                                   ], string='Leave Code', required=True)
    leave_color = fields.Integer(string="Leave Color")
