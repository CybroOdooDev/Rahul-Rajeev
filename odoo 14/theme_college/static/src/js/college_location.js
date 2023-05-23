odoo.define('theme_college.college_location', function(require){
    'use strict';

    var Animation = require('website.content.snippets.animation');
    var ajax = require('web.ajax');

    Animation.registry.get_product_tab = Animation.Class.extend({
        selector : '.college_location_class',
        start: function(){
            var self = this;
            ajax.jsonRpc('/get_college_locations', 'call', {})
            .then(function (data) {
                if(data){
                    self.$target.empty().append(data);
                }
            });
        }
    });
});