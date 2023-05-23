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
{
    'name': "Advance HR Attendance Dashboard",
    'version': '16.0.1.0.0',
    'description': """This HR Attendance Dashboard 
                    includes a form for filtering attendance data, a search bar 
                    for finding specific employees, and an HTML table for displaying 
                    attendance information. The template also adds a "Print PDF" 
                    button to the form using jQuery.""",
    'summary': """This module helps you to view leaves of employee based on different leave types.""",
    'category': 'Human Resources/Attendances',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'hr_holidays', 'hr', 'hr_attendance'],
    'external_dependencies': {
        'python': ['pandas'],
    },
    'data': [
        'views/hr_leave_type.xml',
        'views/dashboard_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'advance_hr_attendance_dashboard/static/src/js/attendance_dashboard.js',
            'advance_hr_attendance_dashboard/static/src/xml/attendance_dashboard.xml',
            'advance_hr_attendance_dashboard/static/src/css/attendance_dashboard.css',
        ],
    },
    'images': [
        'static/description/banner.jpg',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
