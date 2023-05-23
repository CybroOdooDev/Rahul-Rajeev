odoo.define('website_customer_contact.customer_contact_form', function (require) {
"use strict";

var publicWidget = require('web.public.widget');
publicWidget.registry.WebsiteCustomerContactRequestForm = publicWidget.Widget.extend({
    selector: '.customer_contact_form',
    events: {
        'change .select_box_test': '_onChangeType',
        'change .country_select': '_onChangeCountry',
    },
    // on change of customer type, fields to fill varies
    _onChangeType: function(ev){
        var $select = $(ev.currentTarget);
        var selectedValue = $select.val();
        if (selectedValue === 'contact'){
            this.$('.job_position').show();
            this.$('.contact_title').show();
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
    // on change of country, only states of that particular country will be shown
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
