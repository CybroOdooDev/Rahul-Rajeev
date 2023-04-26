/* @odoo-module */

//import Popover from "web.Popover";
import session from 'web.session';
import { useService } from "@web/core/utils/hooks";
import { buildQuery } from "web.rpc";

const { Component } = owl;
//this.rpc = useService('rpc');
//const rpc = useService('rpc');
//const orm = useService('orm');


export class TimeOffEmpCard extends Component {}

//TimeOffEmpCard.components = { Popover };
TimeOffEmpCard.template = 'hr_leave_dashboard.TimeOffEmpCard';
TimeOffEmpCard.props = ['name', 'id', 'department_id', 'job_position', 'children', 'image_1920', 'work_email', 'work_phone', 'company', 'resource_calendar_id'];

export class TimeOffEmpOrgChart extends Component {
    setup() {
        this.props;
        console.log('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
        session.user_has_group('hr_holidays.group_hr_holidays_manager').then(hasGroup => {
            this.manager = hasGroup;
        });
        console.log('-=-=...........................', this)

    }
}

//TimeOffEmpOrgChart.components = { Popover };
//TimeOffEmpOrgChart.template = 'hr_leave_dashboard.hr_org_chart_employee';
TimeOffEmpOrgChart.template = 'hr_leave_dashboard.hr_org_chart';
TimeOffEmpOrgChart.props = ['name', 'id', 'department_id', 'job_position', 'children'];

export class EmpDepartmentCard extends Component {}

//EmpDepartmentCard.components = { Popover };
EmpDepartmentCard.template = 'hr_leave_dashboard.EmpDepartmentCard';
EmpDepartmentCard.props = ['name', 'id', 'department_id', 'child_all_count', 'children', 'absentees', 'current_shift', 'upcoming_holidays'];
//var x='hr_leave_dashboard.EmpDepartmentCard'

export class ApprovalStatusCard extends Component {
        setup() {
        this.props;
        this.rpc = useService('rpc');
//        this.orm = useService('orm');
        this.actionService = useService("action");

        session.user_has_group('hr_holidays.group_hr_holidays_manager').then(hasGroup => {
            this.manager = hasGroup;
        });
        console.log('thissssssspppppp', this)

    }
    async printPdfReport() {
        console.log('printPdfReport()uuhhhhhhhhhhhhhhhh');
        const duration = $("#duration").val()
        console.log('duration', duration)
//        const rpcQuery = buildQuery({
//            model: 'hr.leave',
//            method: 'print_pdf_report',
//            args: [duration],
//        })
//        const result = await this.rpc(rpcQuery.route, rpcQuery.params);
//        console.log('rpcQuery', rpcQuery)
//        console.log('resul', result)
        return this.actionService.doAction({
            type: "ir.actions.report",
            report_type: "qweb-pdf",
            report_name: "hr_leave_dashboard.hr_leave_report",
//            report_file: this.report_file,
            report_file: "hr_leave_dashboard.hr_leave_report",
            data: {
                'duration': duration
                }
        });
    }
}
//ApprovalStatusCard.template = x;
ApprovalStatusCard.template = 'hr_leave_dashboard.ApprovalStatusCard';
ApprovalStatusCard.props = ['id','name','approval_status_count','child_ids', 'children'];