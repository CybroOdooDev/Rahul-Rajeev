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
    'name': "Advanced Leave Dashboard",
    'description': """Advanced Leave Dashboard""",
    'summary': """Leave dashboard module brings a multipurpose graphical dashboard"""
               """ for Time Off module and making the relationship management better and easier""",
    'category': '',
    'version': '16.0.1.0.0',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'hr_holidays', 'hr_org_chart'],
    'external_dependencies': {
        'python': ['pandas'],
    },
    'data': [

        'report/hr_leave_reports.xml',
        'report/hr_leave_report_templates.xml',

    ],
    'assets': {
        'web.assets_backend': [

            'hr_leave_dashboard/static/src/xml/approval_satus_card.xml',
            'hr_leave_dashboard/static/src/js/calendar_model.js',
            'hr_leave_dashboard/static/src/js/calendar_year_renderer.js',
            'hr_leave_dashboard/static/src/js/hooks.js',
            'hr_leave_dashboard/static/src/js/emp_org_chart.js',
            'hr_leave_dashboard/static/src/js/time_off_emp_card.js',
            'hr_leave_dashboard/static/src/js/time_off_emp_dashboard.js',
            'hr_leave_dashboard/static/src/xml/approval_satus_card.xml',
            'hr_leave_dashboard/static/src/xml/time_off_emp_dashboard.xml',
            'hr_leave_dashboard/static/src/xml/emp_org_chart.xml',
            'hr_leave_dashboard/static/src/xml/emp_department_card.xml',
            'hr_leave_dashboard/static/src/xml/time_off_emp_card.xml',
            'hr_leave_dashboard/static/src/css/hr_leave_dashboard.css',
            'hr_org_chart/static/src/fields/hr_org_chart.scss',
            'hr_leave_dashboard/static/src/scss/time_off_dashboard.scss',
            'hr_holidays/static/src/dashboard/time_off_card.scss',
            'hr_leave_dashboard/static/src/scss/calendar_renderer.scss'
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
