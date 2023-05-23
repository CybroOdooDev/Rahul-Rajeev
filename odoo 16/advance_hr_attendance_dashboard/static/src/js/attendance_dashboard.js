odoo.define('advance_hr_attendance_dashboard.AttendanceDashboard', function(require) {
    'use strict';
    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var rpc = require('web.rpc');

    var AttendanceDashboard = AbstractAction.extend({
        contentTemplate: 'AttendanceDashboard',
        events: {

            'change #filter_duration': '_OnChangeFilterDuration',
            'click .print_attendance_pdf_report': '_OnClickPdfReport',
            'click .search_employee': '_OnClickSearchEmployee'
        },
        result : {},
        //based on change in filter duration, data in attendance table will change
        _OnChangeFilterDuration : function(e) {
                e.stopPropagation();
                var $target = $(e.target);
                var value = $target.val();
                if (value=="this_month"){
                    this.onclick_this_month($target.val());
                }else if (value=="last_15_days"){
                    this.onclick_last_15_days($target.val());
                }else if (value=="this_week"){
                    this.onclick_this_week($target.val());
                }
            },
        //on clicking search button, employees will be filtered
        _OnClickSearchEmployee: function(){
            var self = this;
            var searchbar = document.getElementById('search-bar').value.toLowerCase()
            var attendance_table_rows = document.getElementById('attendance_table').children
            self.get_employee_leave_data(self.result)
            for(var row=1;row<attendance_table_rows.length;++row){
                if (!attendance_table_rows[row].getAttribute("data-name").toLowerCase().includes(searchbar)){
                    $('#'+attendance_table_rows[row].id).hide();
                }
            }
        },
        //on clicking Print PDF button, report will be printed
        _OnClickPdfReport: function(){
            var divToPrint = document.getElementById('attendance_table')
            var htmlToPrint = '' + '<style type="text/css">' + 'table th, table td {' + 'border:1px solid #ccc;' + 'padding;0em;' + 'border-right;0em;' + 'border-bottom;0em;' + '}' + '</style>' +
                                '<style type="text/css">' + 'table{' + ' border-spacing:0px; ' + 'border-right:1px solid #ccc;' + 'border-bottom:1px solid #ccc;' + '}'
                                + '</style>'
            htmlToPrint += divToPrint.outerHTML;
            var newWin = window.open("");
            newWin.document.write("<h3 align='center'>Attendance Report</h3>");
            newWin.document.write(htmlToPrint);
            newWin.print();
            newWin.close();
        },
        //employee leave data will be fetched on calling this function
        get_employee_leave_data: function(result){
            var date;
            var leave_date=0
            $('#attendance_table').empty()
            $('#attendance_table').append("<thead id='attendance_table_head'><tr id='employee_name_head'><th><strong>Employee Name</strong></th>")
            for (date=0;date<result.filtered_duration_dates.length;++date){
                $('#employee_name_head').append("<th id='filtered_duration_dates'><strong> "+result.filtered_duration_dates[date]+" </strong></th>");
            }
            $('#employee_name_head').append("<th><strong>Total<strong></th>")
            $('#attendance_table').append("</tr></thead>")

            for (name=0;name<result.employee_data.length;++name){
                $('#attendance_table').append("<tr id='"+result.employee_data[name].id+"' data-name='"+ result.employee_data[name].name+"'><td>"+result.employee_data[name].name+"</td>")
                for (leave_date=0;leave_date<result.employee_data[name].leave_data.length;++leave_date){
                    $('#'+result.employee_data[name].leave_data[leave_date].id+'').append("<td style='text-align:center;background-color:"+result.employee_data[name].leave_data[leave_date].color+"'>"+result.employee_data[name].leave_data[leave_date].state+"</td>")
                }
                $('#'+result.employee_data[name].id+'').append("<td style='text-align:center;'>"+result.employee_data[name].total_absent_count+"</td>")
                $('#attendance_table').append("</tr>")
            }
        },
        //on click on this function, attendance table will show this weeks attendance data
        onclick_this_week: function(ev) {
            var self = this;
            rpc.query({
                    model: "hr.employee",
                    method: "get_employee_leave_data",
                    args: [ev]
                }).then(function(result){
                    self.get_employee_leave_data(result)
                    self.result = result
                });
            },
        //on click on this function, attendance table will show last 15 days attendance data
        onclick_last_15_days: function(ev) {
            var self = this;
            rpc.query({
                    model: "hr.employee",
                    method: "get_employee_leave_data",
                    args: [ev]
                }).then(function(result){
                    self.get_employee_leave_data(result)
                    self.result = result
                });
            },
        //on click on this function, attendance table will show last months attendance data
        onclick_this_month: function(ev) {
            var self = this;
            rpc.query({
                    model: "hr.employee",
                    method: "get_employee_leave_data",
                    args: [ev]
                }).then(function(result){
                    self.get_employee_leave_data(result)
                    self.result = result
                });
            },

        });
        core.action_registry.add('attendance_dashboard', AttendanceDashboard);

        return AttendanceDashboard;
        });
