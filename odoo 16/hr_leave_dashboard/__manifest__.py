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
{
    'name': "Leave Dashboard",
    'description': """Leave Dashboard""",
    'summary': """Leave dashboard module brings a multipurpose graphical dashboard"""
               """ for Time Off module and making the relationship management better and easier""",
    'category': '',
    'version': '16.0.1.0.0',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'hr_holidays', 'hr_org_chart'],
    'data': [

        'reports/report.xml',
        'reports/template.xml',

        'views/hr_leave_type.xml',
        'views/views.xml',
    ],
    'assets': {
        'web.assets_backend': [

            'hr_leave_dashboard/static/src/xml/approval_satus_card.xml',
            'hr_leave_dashboard/static/src/js/calendar_model.js',
            'hr_leave_dashboard/static/src/js/attendance_report.js',
            'hr_leave_dashboard/static/src/js/calendar_year_renderer.js',
            'hr_leave_dashboard/static/src/js/hooks.js',
            'hr_leave_dashboard/static/src/js/emp_org_chart.js',
            'hr_leave_dashboard/static/src/js/time_off_emp_card.js',
            'hr_leave_dashboard/static/src/js/time_off_emp_org_chart.js',
            'hr_leave_dashboard/static/src/js/emp_department_card.js',
            'hr_leave_dashboard/static/src/js/time_off_emp_dashboard.js',
            'hr_leave_dashboard/static/src/xml/attendance_report.xml',
            'hr_leave_dashboard/static/src/xml/approval_satus_card.xml',
            'hr_leave_dashboard/static/src/xml/time_off_emp_dashboard.xml',
            'hr_leave_dashboard/static/src/xml/emp_org_chart.xml',
            'hr_leave_dashboard/static/src/xml/emp_department_card.xml',
            'hr_leave_dashboard/static/src/xml/time_off_emp_card.xml',
            'hr_leave_dashboard/static/src/css/style.css',
            'hr_leave_dashboard/static/src/scss/hr_org_chart.scss',
            # 'hr_leave_dashboard/static/src/scss/calendar_renderer.scss',
            'hr_leave_dashboard/static/src/scss/time_off_dashboard.scss',
            'hr_leave_dashboard/static/src/scss/time_off_card.scss',


            # Don't include dark mode files in light mode
            # ('remove', 'hr_leave_dashboard/static/src/dashboard/**/*.dark.scss'),
        ],
        "web.dark_mode_assets_backend": [
            # 'hr_leave_dashboard/static/src/dashboard/**/*.dark.scss',
        ],
    },
    # 'images': [
    #     'static/description/banner.png',
    # ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
