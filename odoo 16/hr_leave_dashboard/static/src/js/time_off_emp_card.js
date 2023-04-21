/* @odoo-module */

//import Popover from "web.Popover";
import session from 'web.session';

const { Component } = owl;

export class TimeOffEmpCard extends Component {}

//TimeOffEmpCard.components = { Popover };
TimeOffEmpCard.template = 'hr_leave_dashboard.TimeOffEmpCard';
TimeOffEmpCard.props = ['name', 'id', 'department_id', 'job_position', 'children', 'image_1920', 'work_email', 'work_phone', 'company', 'resource_calendar_id'];

export class TimeOffEmpOrgChart extends Component {}

//TimeOffEmpOrgChart.components = { Popover };
TimeOffEmpOrgChart.template = 'hr_leave_dashboard.hr_org_chart_employee';
TimeOffEmpOrgChart.props = ['name', 'id', 'department_id', 'job_position', 'children'];

export class EmpDepartmentCard extends Component {}

//EmpDepartmentCard.components = { Popover };
EmpDepartmentCard.template = 'hr_leave_dashboard.EmpDepartmentCard';
EmpDepartmentCard.props = ['name', 'id', 'department_id', 'child_all_count', 'children', 'absentees', 'current_shift', 'upcoming_holidays'];
//var x='hr_leave_dashboard.EmpDepartmentCard'
export class ApprovalStatusCard extends Component {
        setup() {
        this.props;

        session.user_has_group('hr_holidays.group_hr_holidays_manager').then(hasGroup => {
            this.manager = hasGroup;
            console.log('xcxc',this.manager)
//            if(this.manager == true){
//                 console.log('managerrrrr',this.manager)
//                  ApprovalStatusCard.template = 'hr_leave_dashboard.ApprovalStatusCard';
//                }
        });
        console.log('thisssssss', this)

    }
}
//ApprovalStatusCard.template = x;
ApprovalStatusCard.template = 'hr_leave_dashboard.ApprovalStatusCard';
ApprovalStatusCard.props = ['id','name','approval_status_count'];