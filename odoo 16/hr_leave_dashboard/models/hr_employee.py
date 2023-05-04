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
####################################################################################
from odoo import models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Inheriting Employees Module'

    def get_public_holidays(self, start_date, end_date):
        """The function get_public_holidays takes in a start date and end date as arguments
         and returns a dictionary with all the public holidays within that range.
          It does this by calling the _get_public_holidays method and
          then iterating through the results to add each holiday to the dictionary."""
        all_days = {}

        self = self or self.env.user.employee_id
        public_holidays = self._get_public_holidays(start_date, end_date)
        for holiday in public_holidays:

            num_days = (holiday.date_to - holiday.date_from).days
            for d in range(num_days + 1):
                all_days[str(holiday.date_from.date())] = d

        return all_days

    def _get_public_holidays(self, start_date, end_date):
        """The _get_public_holidays function searches for public holidays within a given date range,
        for all companies associated with the current environment's user.
        It returns a recordset of resource.calendar.leaves that match the search criteria."""
        public_holidays = self.env['resource.calendar.leaves'].search([
            ('date_from', '<=', end_date),
            ('date_to', '>=', start_date),
            ('resource_id', '=', False),
            ('company_id', 'in', self.env.companies.ids),
        ])

        return public_holidays
