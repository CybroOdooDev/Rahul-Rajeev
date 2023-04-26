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
from odoo import models, fields, api


class HRLeaveReport(models.AbstractModel):
    _name = 'report.hr_leave_dashboard.hr_leave_report'
    _description = 'HR Leave Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        # employee =
        query = "SELECT employee_id,name,date_from,date_to FROM hr_leave " \
                "INNER JOIN hr_employee ON hr_leave.employee_id = hr_employee.id WHERE state = 'validate'"
        self._cr.execute(query)
        print('xxxxx', data)
        print('xxxxx', data.get('report_type'))
        print('xxxxx', data.get('duration'))
        # if not data.get('form'):
        #     raise UserError(
        #         _("Form content is missing, this report cannot be printed."))
        return {
           'duration': data.get('duration')
        }



    # @api.model
    # def print_pdf_report(self, duration):
    #     print('print_pdf_report', duration)
    #     data = {}
    #     return self.env.ref('hr_leave_dashboard.action_hr_leave_report').report_action(None, data=data)
    #     # return True