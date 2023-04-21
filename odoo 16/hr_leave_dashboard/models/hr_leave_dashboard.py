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


class HRLeave(models.Model):
    _inherit = 'hr.leave'
    _description = 'Inheriting Time Off Module'

    def _prepare_employee_data(self, employee):
        return dict(
            id=employee.id,
            name=employee.name,
            link='/mail/view?model=%s&res_id=%s' % ('hr.employee.public', employee.id,),
            # job_id=employee.job_id.id,
            # job_name=employee.job_id.name or '',
            # # job_title=employee.job_id.name or '',
            # direct_sub_count=len(employee.child_ids - employee),
            # indirect_sub_count=employee.child_all_count,
        )

    @api.model
    def get_current_employee(self):
        current_employee = self.env.user.employee_ids

        current_employee_details = {
            'id': current_employee.id,
            'name': current_employee.name,
            'image_1920': current_employee.image_1920,
            'work_email': current_employee.work_email,
            'work_phone': current_employee.work_phone,
            'resource_calendar_id': current_employee.resource_calendar_id.name,
            'link': '/mail/view?model=%s&res_id=%s' % ('hr.employee.public', current_employee.id,),
            'department_id': current_employee.department_id.name,
            'company': current_employee.company_id.name,
            'job_position': current_employee.job_id.name,
            'parent_id': current_employee.parent_id.ids,
            'child_ids': current_employee.child_ids.ids,
            'child_all_count': current_employee.child_all_count,
            'manager': self._prepare_employee_data(current_employee.parent_id) if (
                current_employee.parent_id) else {},
            'manager_all_count': len(current_employee.parent_id.ids),
            'children': [self._prepare_employee_data(child) for child in current_employee.child_ids if
                         child != current_employee],
        }
        return current_employee_details

    @api.model
    def get_absentees(self):
        today = datetime.datetime.now()
        current_employee = self.env.user.employee_ids
        children = [self._prepare_employee_data(child) for child in current_employee.child_ids if
                    child != current_employee]
        child_list = []
        for child in children:
            child_list.append(child.get('id'))
        if len(child_list) > 1:
            query = "SELECT employee_id,name,date_from,date_to FROM hr_leave " \
                    "INNER JOIN hr_employee ON hr_leave.employee_id = hr_employee.id WHERE state = 'validate' AND " \
                    "employee_id in %s" % str(tuple(child_list))
            self._cr.execute(query)
        elif len(child_list) == 1:
            query = "SELECT employee_id,name,date_from,date_to FROM hr_leave " \
                    "INNER JOIN hr_employee ON hr_leave.employee_id = hr_employee.id WHERE state = 'validate' AND " \
                    "employee_id = %s" % child_list[0]
            self._cr.execute(query)
        leave = self._cr.dictfetchall()
        absentees = []
        for i in range(len(leave)):
            date_from = leave[i].get('date_from')
            date_to = leave[i].get('date_to')
            if date_from <= today <= date_to:
                absentees.append(leave[i])
        return absentees

    @api.model
    def get_current_shift(self):
        current_employee = self.env.user.employee_ids
        # print('current_employee', current_employee)
        employee_tz = current_employee.tz or self.env.context.get('tz')
        employee_pytz = pytz.timezone(employee_tz) if employee_tz else pytz.utc
        employee_datetime = datetime.datetime.now().astimezone(employee_pytz)
        hour = employee_datetime.strftime("%H")
        minute = employee_datetime.strftime("%M")
        day = employee_datetime.strftime("%A")
        time = hour + '.' + minute
        # day_num = 0 if day == 'Monday' else 1 if day == 'Tuesday' else 2 if day == 'Wednesday' else 3 if day == 'Thursday' else 4 if day == 'Friday' else 5 if day == 'Saturday' else 6 if day == 'Sunday' else 3
        if day == 'Monday':
            day_num = '0'
        elif day == 'Tuesday':
            day_num = '1'
        elif day == 'Wednesday':
            day_num = '2'
        elif day == 'Thursday':
            day_num = '3'
        elif day == 'Friday':
            day_num = '4'
        elif day == 'Saturday':
            day_num = '5'
        else:
            day_num = '6'

        for shift in current_employee.resource_calendar_id.attendance_ids:
            if shift.dayofweek == day_num and shift.hour_from <= float(time) <= shift.hour_to:
                return shift.name
            # else:
        return False

    @api.model
    def get_upcoming_holidays(self):
        current_employee = self.env.user.employee_ids
        employee_tz = current_employee.tz or self.env.context.get('tz')
        employee_pytz = pytz.timezone(employee_tz) if employee_tz else pytz.utc
        employee_datetime = datetime.datetime.now().astimezone(employee_pytz)
        # print(employee_tz)
        # print(employee_pytz)
        # print(employee_datetime)
        # holidays = self.env['resource.calendar.leaves'].search([('resource_id', '=', False)])
        query = "SELECT * FROM public.resource_calendar_leaves WHERE resource_id is null"
        self._cr.execute(query)
        holidays = self._cr.dictfetchall()
        upcoming_holidays = []
        for holiday in holidays:
            if employee_datetime.date() < holiday.get('date_to').date():
                upcoming_holidays.append(holiday)
        # print(upcoming_holidays)
        return upcoming_holidays

    @api.model
    def get_approval_status_count(self):
        current_employee = self.env.user.employee_ids
        validate_count = len(self.env['hr.leave'].search([('employee_id', '=', current_employee.id),
                                                          ('state', '=', 'validate')]))
        confirm_count = len(self.env['hr.leave'].search([('employee_id', '=', current_employee.id),
                                                         ('state', '=', 'confirm')]))
        refuse_count = len(self.env['hr.leave'].search([('employee_id', '=', current_employee.id),
                                                        ('state', '=', 'refuse')]))

        approval_status_count = {
            'validate_count': validate_count,
            'confirm_count': confirm_count,
            'refuse_count': refuse_count
        }
        return approval_status_count
