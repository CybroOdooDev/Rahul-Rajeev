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
from datetime import timedelta
from odoo import api, fields, models
from odoo.tools import date_utils
import pandas


class HRLeaveReport(models.AbstractModel):
    _name = 'report.hr_leave_dashboard.hr_leave_report'
    _description = 'HR Leave Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        if data.get('duration') == 'this_month':
            option = pandas.date_range(date_utils.start_of(fields.Date.today(), 'month'),
                                       date_utils.end_of(fields.Date.today(), 'month') - timedelta(days=0),
                                       freq='d').strftime(
                "%Y-%m-%d").tolist()
        elif data.get('duration') == 'this_year':
            option = pandas.date_range(date_utils.start_of(fields.Date.today(), 'year'),
                                       date_utils.end_of(fields.Date.today(), 'year') - timedelta(days=0),
                                       freq='d').strftime(
                "%Y-%m-%d").tolist()
        elif data.get('duration') == 'this_week':
            option = pandas.date_range(date_utils.start_of(fields.Date.today(), 'week'),
                                       date_utils.end_of(fields.Date.today(), 'week') - timedelta(days=0),
                                       freq='d').strftime(
                "%Y-%m-%d").tolist()
        else:
            option = [str(fields.Date.today())]

        if not self.env.user.employee_ids.child_ids:
            query = """SELECT l.id,
                        lt.id as hr_leave_type_id,
                        e.id as emp_id,
                        e.name as emp_name,
                        e.department_id as emp_department,
                        e.parent_id as emp_parent_id,
                        request_date_from,
                        request_date_to,
                        l.number_of_days,
                        lt.name ::jsonb->> 'en_US' as leave_type,
                            SUM(al.number_of_days) AS allocated_days,
                            SUM(CASE WHEN l.state = 'validate' THEN l.number_of_days ELSE 0 END) AS taken_days,
                            SUM(al.number_of_days) - SUM(CASE WHEN l.state = 'validate' THEN l.number_of_days ELSE 0 END) AS
                            balance_days
                        FROM hr_employee e
                        inner join hr_leave_allocation al ON al.employee_id = e.id	
                        inner join hr_leave l on l.employee_id = e.id
                        inner join hr_leave_type lt on l.holiday_status_id = lt.id
                        WHERE l.state = 'validate' AND e.department_id = '%s'
                        GROUP BY e.id,lt.id,l.id""" % self.env.user.employee_ids.department_id.id
        else:
            query = """SELECT l.id,
                                    lt.id as hr_leave_type_id,
                                    e.id as emp_id,
                                    e.name as emp_name,
                                    e.department_id as emp_department,
                                    e.parent_id as emp_parent_id,
                                    request_date_from,
                                    request_date_to,
                                    l.number_of_days,
                                    lt.name ::jsonb->> 'en_US' as leave_type,
                                        SUM(al.number_of_days) AS allocated_days,
                                        SUM(CASE WHEN l.state = 'validate' THEN l.number_of_days ELSE 0 END) AS taken_days,
                                        SUM(al.number_of_days) - SUM(CASE WHEN l.state = 'validate' THEN l.number_of_days ELSE 0 END) AS
                                        balance_days
                                    FROM hr_employee e
                                    inner join hr_leave_allocation al ON al.employee_id = e.id	
                                    inner join hr_leave l on l.employee_id = e.id
                                    inner join hr_leave_type lt on l.holiday_status_id = lt.id
                                    WHERE l.state = 'validate'
                                    GROUP BY e.id,lt.id,l.id"""

        self.env.cr.execute(query)
        leave_data = self.env.cr.dictfetchall()
        filtered_list = []
        filtered_tuple = []
        for leave in leave_data:
            # print(leave.get('hr_leave_type_id'), leave.get('emp_id'))
            leave_list = pandas.date_range(leave.get('request_date_from'),
                                           leave.get('request_date_to') - timedelta(days=1), freq='d').strftime(
                "%Y-%m-%d").tolist()
            for date in leave_list:
                if date in option:
                    filtered_list.append(leave)
                    break
        for leave in filtered_list:
            if (leave.get('hr_leave_type_id'), leave.get('emp_id')) in filtered_tuple:
                filtered_list.remove(leave)
            else:
                filtered_tuple.append((leave.get('hr_leave_type_id'), leave.get('emp_id')))
        print('filtered_list', filtered_list)
        return {
            'duration': data.get('duration'),
            'filtered_list': filtered_list,
        }
