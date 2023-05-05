odoo.define('advance_hr_attendance_dashboard.AttendanceDashboard', function(require) {
    'use strict';
    var AbstractAction = require('web.AbstractAction');
    var ajax = require('web.ajax');
    var core = require('web.core');
    var rpc = require('web.rpc');
    var web_client = require('web.web_client');
    var _t = core._t;
    var QWeb = core.qweb;
    var self = this;
//    const { loadBundle } = require("@web/core/assets");
//    var currency;
    var AttendanceDashboard = AbstractAction.extend({
        contentTemplate: 'AttendanceDashboard',
        events: {
            'change #filter_duration': function(e) {
//            console.log('xxxxxxxxx', this)
                e.stopPropagation();
                var $target = $(e.target);
                var value = $target.val();
                if (value=="this_month"){
                    this.onclick_this_month($target.val());
                }else if (value=="last_15_days"){
                    this.onclick_last_15_days($target.val());
                }else if (value=="this_week"){
//                    console.log('111111',this)
                    this.onclick_this_week($target.val());
                }
            },
        },
        onclick_this_week: function(ev) {
            var self = this;
            console.log('222222',ev,'lll')
            rpc.query({
                    model: "hr.employee",
                    method: "get_data",
                    args: [ev]
                }).then(function(result){
                    console.log('resultttt', result)
                });
            },
        onclick_last_15_days: function(ev) {
            var self = this;
            rpc.query({
                    model: "hr.employee",
                    method: "get_data",
                    args: [ev]
                }).then(function(result){
                    console.log('resultttt', result.filtered_duration_dates.length)
                    var date;
                    for (date=0;date<result.filtered_duration_dates.length;++date){
                        console.log('date',result.filtered_duration_dates[date]);
//                        $('#employee_name').append('<span>' + result.filtered_duration_dates[date] + '</span>');
                    }
                });
                 },
        onclick_this_month: function(ev) {
            var self = this;
            rpc.query({
                    model: "hr.employee",
                    method: "get_data",
                    args: [ev]
                }).then(function(result){
                    console.log('resultttt', result)
                });
            }
        });
        core.action_registry.add('attendance_dashboard', AttendanceDashboard);

        return AttendanceDashboard;
        });
