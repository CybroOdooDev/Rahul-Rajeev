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
import pytz
from odoo import api, models
import datetime


class HrLeave(models.Model):
    _inherit = 'hr.leave'
    _description = 'Inheriting Time Off Module'

    def _prepare_employee_data(self, employee):
        return dict(
            id=employee.id,
            name=employee.name,
            job_id=employee.job_id.name,
            approval_status_count=self.get_approval_status_count(employee.id)
        )

    @api.model
    def get_current_employee(self):
        """ This function fetches current employee details in a dictionary"""
        current_employee = self.env.user.employee_ids

        current_employee_details = {
            'id': current_employee.id,
            'name': current_employee.name,
            'job_id': current_employee.job_id.id,
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
        """The function retrieves a list of employees who are absent on the current date by
        querying the hr_leave table and comparing the date_from and date_to fields of validated
        leave requests. It returns a list of dictionaries containing the employee's name,
        employee_id, date_from, and date_to """
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
        for leave_date in range(len(leave)):
            date_from = leave[leave_date].get('date_from')
            date_to = leave[leave_date].get('date_to')
            if date_from <= today <= date_to:
                absentees.append(leave[leave_date])
        return absentees

    @api.model
    def get_current_shift(self):
        """ This function fetches current employee's current shift"""
        current_employee = self.env.user.employee_ids
        employee_tz = current_employee.tz or self.env.context.get('tz')
        employee_pytz = pytz.timezone(employee_tz) if employee_tz else pytz.utc
        employee_datetime = datetime.datetime.now().astimezone(employee_pytz)
        hour = employee_datetime.strftime("%H")
        minute = employee_datetime.strftime("%M")
        day = employee_datetime.strftime("%A")
        time = hour + '.' + minute
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
        return False

    @api.model
    def get_upcoming_holidays(self):
        """ This function fetches upcoming holidays"""
        current_employee = self.env.user.employee_ids
        employee_tz = current_employee.tz or self.env.context.get('tz')
        employee_pytz = pytz.timezone(employee_tz) if employee_tz else pytz.utc
        employee_datetime = datetime.datetime.now().astimezone(employee_pytz)
        query = "SELECT * FROM public.resource_calendar_leaves WHERE resource_id is null"
        self._cr.execute(query)
        holidays = self._cr.dictfetchall()
        upcoming_holidays = []
        for holiday in holidays:
            if employee_datetime.date() < holiday.get('date_to').date():
                upcoming_holidays.append(holiday)
        return upcoming_holidays

    @api.model
    def get_approval_status_count(self, current_employee):
        """ This function fetches approval status count"""
        validate_count = len(self.env['hr.leave'].search([('employee_id', '=', current_employee),
                                                          ('state', '=', 'validate')]))
        confirm_count = len(self.env['hr.leave'].search([('employee_id', '=', current_employee),
                                                         ('state', '=', 'confirm')]))
        refuse_count = len(self.env['hr.leave'].search([('employee_id', '=', current_employee),
                                                        ('state', '=', 'refuse')]))
        approval_status_count = {
            'validate_count': validate_count,
            'confirm_count': confirm_count,
            'refuse_count': refuse_count
        }
        return approval_status_count

    @api.model
    def get_all_validated_leaves(self):
        """ This function fetches all validated leaves"""
        leaves = self.env['hr.leave'].search([('state', '=', 'validate')])
        all_validated_leaves = []
        for leave in leaves:
            all_validated_leaves.append({
                'id': leave.id,
                'employee_id': leave.employee_id.id,
                'employee_name': leave.employee_id.name,
                'request_date_from': leave.request_date_from,
                'request_date_to': leave.request_date_to,
                'leave_type_id': leave.holiday_status_id.id,
                'leave_type': leave.holiday_status_id.name,
                'number_of_days': leave.number_of_days
            })
        return all_validated_leaves
