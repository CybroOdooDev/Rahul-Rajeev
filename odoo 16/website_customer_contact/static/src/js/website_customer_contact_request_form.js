odoo.define('website_customer_contact.website_customer_contact_request_form', function (require) {
"use strict";

var core = require('web.core');
var publicWidget = require('web.public.widget');
var utils = require('web.utils');
var qweb = core.qweb;
publicWidget.registry.WebsiteCustomerContactRequestForm = publicWidget.Widget.extend({
    selector: '.customer_contact_form',
    events: {
        'change .select_box_test': '_onChangeType',
        'change .country_select': '_onChangeCountry',
    },
    _onChangeType: function(ev){
        var $select = $(ev.currentTarget);
        var selectedValue = $select.val();
        if (selectedValue === 'contact'){
            this.$('.job_position').show();
            this.$('.contact_title').show();
            console.log(this.$('.contact_title'));
            this.$('.street').hide();
            this.$('.street2').hide();
            this.$('.city').hide();
            this.$('.zip').hide();
            this.$('.state_id').hide();
            this.$('.country_id').hide();
        }else{
            this.$('.job_position').hide();
            this.$('.contact_title').hide();
            this.$('.street').show();
            this.$('.street2').show();
            this.$('.city').show();
            this.$('.zip').show();
            this.$('.state_id').show();
            this.$('.country_id').show();
        }
    },
    _onChangeCountry: function(ev){
        var selected_country = $('.country_select')[0].selectedOptions[0].innerText
        var state = $('.state_select_option')
        var state_id;
        for(var i=0; i<state.length; i++){
            $(state[i])[0].style['display'] = ""
            state_id = state[i].dataset['id']
            if (state_id != selected_country){
                    $(state[i])[0].style['display'] = "none"
            }
        }
    },
});
return publicWidget;
});

