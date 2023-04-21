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
    "name": "Theme College",
    "summary": "Theme College",
    "version": "15.0.1.0.0",
    "category": "Theme/Education",
    "website": "https://www.cybrosys.com",
    "description": """
        Theme College
    """,
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    "depends": [
        'base',
        'web',
        'website',
        'website_livechat',
    ],
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.png',
    ],
    "data": [
        'views/contact_us.xml',
        'views/snippets.xml',
        'views/header.xml',
        'views/alumni.xml',
        'views/course.xml',
        'views/facility.xml',
        'views/gallery.xml',
        'views/location.xml',
        'views/footer.xml',
        'views/views.xml',
    ],
    'assets': {
            'web.assets_frontend': [
                'theme_college/static/src/css/style.css',
                ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
