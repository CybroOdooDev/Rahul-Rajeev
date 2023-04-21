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

from odoo import http
from odoo.http import request


class CustomerContacts(http.Controller):
    """"class to create a route to website"""

    @http.route(['/my/contacts'], type='http', auth='public', website=True)
    def view_customer_contacts(self):
        """"function to render template and pass value to website"""
        customer_contact = request.env['res.partner'].sudo().search(
            [('parent_id', '=', request.env.user.partner_id.id)])

        return request.render('website_customer_contact.website_customer_contact',
                              {'customer_contact_portal': customer_contact, 'page_name': 'customer_contact'})

    @http.route(['/my/contacts/<int:contact>'], type='http', auth='public', website=True)
    def view_details_customer_contacts(self, contact):
        """"function to render template and pass value to website"""
        customer_contact = request.env['res.partner'].sudo().search(
            [('parent_id', '=', request.env.user.partner_id.id), ('id', '=', contact)])
        return request.render('website_customer_contact.website_customer_contact_detail',
                              {'customer_contact_portal': customer_contact, 'page_name': 'customer_contact_details'})
