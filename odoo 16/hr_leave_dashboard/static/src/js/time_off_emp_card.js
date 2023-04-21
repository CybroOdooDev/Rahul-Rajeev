/* @odoo-module */

//import Popover from "web.Popover";

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