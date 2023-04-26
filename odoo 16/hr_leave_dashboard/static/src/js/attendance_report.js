odoo.define('web.HRAttendance', function (require) {
"use strict";

var AbstractAction = require('web.AbstractAction');
var core = require('web.core');
var rpc = require('web.rpc');
var QWeb = core.qweb;
var HRAttendance = AbstractAction.extend({
    template:'HRAttendance',
    events:{
    },
//    init:function(parent, action){
//        this._super(parent, action);
//    },
//    start: function(){
//    var self = this;
//    this.set("title", 'Dashboard');
//    return this._super().then(function(){
//        self.render_dashboards();
//        })
////    self._rpc({
////        model: 'hr.leave',
////        method:'get__',
////        args:[],
////    }).then(function(datas)){
////    console.log('sssssaaaaaaaaaaawwwwwwwwwwwww',datas)
////    self.$('.table_view').html(Qweb.render('HRAttendanceTable',{
////        report_lines: datas
////        }));
////    });
//    },
//    willStart: function(){
//        var self = this;
//        return this.super()
//        },
//    render_dashboards: function(){
//        this.fetch_data()
//        var templates = []
//        var templates = ['MainSection'];
//        _.each(templates, function(template){
//            self.$('.o_hr_dashboard').append(QWeb.render(template, {widget: self}))
//        });
//
//    },
//    fetch_data: function(){
//       var self = this;
//       var def1 = this._rpc({
//            model: 'hr.leave',
//            method: 'get_data',
//       })
//       .then(function(result){
//       })
//    }
});
core.action_registry.add('attendance_report', HRAttendance);
return HRAttendance
});
