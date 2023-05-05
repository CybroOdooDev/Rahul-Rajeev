# -- coding: utf-8 --
###################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2023-TODAY Cybrosys Technologies (<https://www.cybrosys.com>).
#    Author: Cybrosys (<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################
from datetime import timedelta,date
from odoo import api, fields, models
from odoo.tools import date_utils
import pandas


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Inheriting Employees Module'

    @api.model
    def get_data(self, option):
        """Returns data to the dashboard"""
        employee_data = self.env['hr.employee'].search([]).ids
        dates = False
        if option == 'this_week':
            dates = pandas.date_range(
                date_utils.start_of(fields.Date.today(), 'week'),
                date_utils.end_of(fields.Date.today(), 'week') - timedelta(
                    days=0),
                freq='d').strftime(
                "%Y-%m-%d").tolist()
        elif option == 'this_month':
            dates = pandas.date_range(
                date_utils.start_of(fields.Date.today(), 'month'),
                date_utils.end_of(fields.Date.today(), 'month') - timedelta(
                    days=0),
                freq='d').strftime(
                "%Y-%m-%d").tolist()
        elif option == 'last_15_days':
            dates = [str(date.today() - timedelta(days=day))
                     for day in range(15)]
        return {
            'employee_data': employee_data,
            'filtered_duration_dates': dates
        }
