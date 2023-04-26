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
import pytz
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
import datetime


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    def get_public_holidays(self, start_date, end_date):
        all_days = {}
        # all_days = []

        self = self or self.env.user.employee_id
        public_holidays = self._get_public_holidays(start_date, end_date)
        for holiday in public_holidays:

            num_days = (holiday.date_to - holiday.date_from).days
            # print('num_days', num_days)
            for d in range(num_days + 1):
                # all_days.append(str(holiday.date_from.date()))
                all_days[str(holiday.date_from.date())] = d
        # print('all_daysss', all_days)

        return all_days

    def _get_public_holidays(self, start_date, end_date):
        public_holidays = self.env['resource.calendar.leaves'].search([
            ('date_from', '<=', end_date),
            ('date_to', '>=', start_date),
            ('resource_id', '=', False),
            ('company_id', 'in', self.env.companies.ids),
        ])
        # print('sssssstrr', public_holidays)

        # # a user with hr_holidays permissions will be able to see all stress days from his calendar
        # is_leave_user = self == self.env.user.employee_id and self.user_has_groups('hr_holidays.group_hr_holidays_user')
        #
        # if not is_leave_user and stress_days.department_ids:
        #     stress_days = stress_days.filtered(lambda sd:\
        #         not sd.department_ids\
        #         or self.department_id and not set(self.department_id.ids).isdisjoint(sd.department_ids.get_children_department_ids().ids))

        return public_holidays
