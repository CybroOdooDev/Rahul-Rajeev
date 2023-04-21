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

from odoo import http


class College(http.Controller):

    @http.route('/college_alumni', type='http', website=True, auth='public')
    def college_alumni(self):
        return http.request.render('theme_college.college_alumni', {})

    @http.route('/college_course', type='http', website=True, auth='public')
    def college_course(self):
        return http.request.render('theme_college.college_course', {})

    @http.route('/college_facility', type='http', website=True, auth='public')
    def college_facility(self):
        return http.request.render('theme_college.college_facility', {})

    @http.route('/college_gallery', type='http', website=True, auth='public')
    def college_gallery(self):
        return http.request.render('theme_college.college_gallery', {})

    @http.route('/location_1', type='http', website=True, auth='public')
    def location_1(self):
        return http.request.render('theme_college.location_1', {})

    @http.route('/location_2', type='http', website=True, auth='public')
    def location_2(self):
        return http.request.render('theme_college.location_2', {})

    @http.route('/location_3', type='http', website=True, auth='public')
    def location_3(self):
        return http.request.render('theme_college.location_3', {})

    @http.route('/location_4', type='http', website=True, auth='public')
    def location_4(self):
        return http.request.render('theme_college.location_4', {})

    @http.route('/location_5', type='http', website=True, auth='public')
    def location_5(self):
        return http.request.render('theme_college.location_5', {})

    @http.route('/location_6', type='http', website=True, auth='public')
    def location_6(self):
        return http.request.render('theme_college.location_6', {})
