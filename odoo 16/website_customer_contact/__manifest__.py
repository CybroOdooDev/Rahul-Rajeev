# -*- coding: utf-8 -*-
###################################################################################
#    A part of OpenHRMS Project <https://www.openhrms.com>
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2023-TODAY Cybrosys Technologies (<https://www.cybrosys.com>).
#    Author: Cybrosys Technologies (<https://www.cybrosys.com>)
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
    'name': "Website Customer Contact",
    'description': """Website Customer Contact""",
    'description': """This module helps you to create contact and addresses from website.""",
    'summary': """Website Customer Contact""",
    'category': 'Website',
    'version': '16.0.1.0.0',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'website', 'portal'],
    'data': [
        'views/portal_layout.xml',
        'views/inherited_portal_my_home.xml',
        'views/inherited_portal_breadcrumbs.xml',
        'views/inherited_user_dropdown.xml',
        'views/layout.xml',

    ],
    'images': ['static/description/banner.png'],
    'assets': {
        'web.assets_frontend': [
            'website_customer_contact/static/src/css/style.css',
            'website_customer_contact/static/src/js/website_customer_contact_request_form.js',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
