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
    'name': "Kanban Sticky State",
    'version': '16.0.1.0.0',
    'description': """Kanban Sticky State helps you to stick kanban heading at top and not move it.""",
    'summary': """The sticky state in Kanban systems allows teams to track and 
        manage work items effectively, promote collaboration, and identify 
        bottlenecks or areas where tasks are getting stuck. By visualizing 
        the sticky state, teams can quickly identify tasks that require 
        attention and take appropriate action to keep the workflow flowing smoothly.""",
    'category': 'Extra Tools',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'images': [
        'static/description/banner.jpg',
    ],
    'depends': ['base', 'base_setup'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'kanban_sticky_state/static/src/js/kanban_sticky_state.js',
            'kanban_sticky_state/static/src/css/kanban_sticky_state.css',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
