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
from odoo import api, models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    billing_phone = fields.Boolean(string="Billing Phone",
                                   config_parameter='website_sale_address_management.billing_phone')
    billing_phone_is_required = fields.Boolean(
        string="Billing Phone Is Required",
        config_parameter='website_sale_address_management.billing_phone_is_required')
    billing_street = fields.Boolean(string="Billing Street",
                                    config_parameter='website_sale_address_management.billing_street')
    billing_street_is_required = fields.Boolean(
        string="Billing Street Is Required",
        config_parameter='website_sale_address_management.billing_street_is_required')
    billing_street2 = fields.Boolean(string="Billing Street 2",
                                     config_parameter='website_sale_address_management.billing_street2')
    billing_city = fields.Boolean(string="Billing City",
                                  config_parameter='website_sale_address_management.billing_city')
    billing_city_is_required = fields.Boolean(
        string="Billing City Is Required",
        config_parameter='website_sale_address_management.billing_city_is_required')
    billing_country_id = fields.Many2one('res.country',
                                         config_parameter='billing_country',
                                         string="Default Billing Country")
    billing_zip_code = fields.Boolean(string="Billing ZIP Code",
                                      config_parameter='website_sale_address_management.billing_zip_code')
    billing_zip_code_is_required = fields.Boolean(
        string="Billing ZIP Code Is Required",
        config_parameter='website_sale_address_management.billing_zip_code_is_required')
    shipping_phone = fields.Boolean(string="Shipping Phone",
                                    config_parameter='website_sale_address_management.shipping_phone')
    shipping_phone_is_required = fields.Boolean(
        string="Shipping Phone Is Required",
        config_parameter='website_sale_address_management.shipping_phone_is_required')
    shipping_street = fields.Boolean(string="Shipping Street",
                                     config_parameter='website_sale_address_management.shipping_street')
    shipping_street_is_required = fields.Boolean(
        string="Shipping Street Is Required",
        config_parameter='website_sale_address_management.shipping_street_is_required')
    shipping_street2 = fields.Boolean(string="Shipping Street 2",
                                      config_parameter='website_sale_address_management.shipping_street2')
    shipping_city = fields.Boolean(string="Shipping City",
                                   config_parameter='website_sale_address_management.shipping_city')
    shipping_city_is_required = fields.Boolean(
        string="Shipping City Is Required",
        config_parameter='website_sale_address_management.shipping_city_is_required')
    shipping_country_id = fields.Many2one('res.country',
                                          config_parameter='shipping_country',
                                          string="Default Shipping Country")
    shipping_zip_code = fields.Boolean(string="Shipping ZIP Code",
                                       config_parameter='website_sale_address_management.shipping_zip_code')
    shipping_zip_code_is_required = fields.Boolean(
        string="Shipping ZIP Code Is Required",
        config_parameter='website_sale_address_management.shipping_zip_code_is_required')

    @api.onchange('billing_phone')
    def onchange_billing_phone(self):
        if not self.billing_phone:
            self.billing_phone_is_required = False

    @api.onchange('billing_phone_is_required')
    def onchange_billing_phone_is_required(self):
        if self.billing_phone_is_required:
            self.billing_phone = True

    @api.onchange('billing_street')
    def onchange_billing_street(self):
        if not self.billing_street:
            self.billing_street_is_required = False

    @api.onchange('billing_street_is_required')
    def onchange_billing_street_is_required(self):
        if self.billing_street_is_required:
            self.billing_street = True

    @api.onchange('billing_city')
    def onchange_billing_city(self):
        if not self.billing_city:
            self.billing_city_is_required = False

    @api.onchange('billing_city_is_required')
    def onchange_billing_city_is_required(self):
        if self.billing_city_is_required:
            self.billing_city = True

    @api.onchange('billing_zip_code')
    def onchange_billing_zip_code(self):
        if not self.billing_zip_code:
            self.billing_zip_code_is_required = False

    @api.onchange('billing_zip_code_is_required')
    def onchange_billing_zip_code_is_required(self):
        if self.billing_zip_code_is_required:
            self.billing_zip_code = True

    @api.onchange('shipping_phone')
    def onchange_shipping_phone(self):
        if not self.shipping_phone:
            self.shipping_phone_is_required = False

    @api.onchange('shipping_phone_is_required')
    def onchange_shipping_phone_is_required(self):
        if self.shipping_phone_is_required:
            self.shipping_phone = True

    @api.onchange('shipping_street')
    def onchange_shipping_street(self):
        if not self.shipping_street:
            self.shipping_street_is_required = False

    @api.onchange('shipping_street_is_required')
    def onchange_shipping_street_is_required(self):
        if self.shipping_street_is_required:
            self.shipping_street = True

    @api.onchange('shipping_city')
    def onchange_shipping_city(self):
        if not self.shipping_city:
            self.shipping_city_is_required = False

    @api.onchange('shipping_city_is_required')
    def onchange_shipping_city_is_required(self):
        if self.shipping_city_is_required:
            self.shipping_city = True

    @api.onchange('shipping_zip_code')
    def onchange_shipping_zip_code(self):
        if not self.shipping_zip_code:
            self.shipping_zip_code_is_required = False

    @api.onchange('shipping_zip_code_is_required')
    def onchange_shipping_zip_code_is_required(self):
        if self.shipping_zip_code_is_required:
            self.shipping_zip_code = True
