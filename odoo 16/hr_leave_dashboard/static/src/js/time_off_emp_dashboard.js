/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { TimeOffDashboard } from '@hr_holidays/dashboard/time_off_dashboard';
import { TimeOffCard } from '@hr_holidays/dashboard/time_off_card';
import { TimeOffEmpCard } from './time_off_emp_card';
import { TimeOffEmpOrgChart } from './emp_org_chart';
import { EmpDepartmentCard } from './time_off_emp_card';
import { ApprovalStatusCard } from './time_off_emp_card';

//console.log("***********", TimeOffCard)
import { useBus, useService } from "@web/core/utils/hooks";

const { Component, useState, onWillStart } = owl;

patch(TimeOffDashboard.prototype, 'hr_holidays.TimeOffDashboard',{

        async loadDashboardData() {
        const context = {};
        if (this.props.employeeId !== null) {
            context['employee_id'] = this.props.employeeId;
        }

        this.state.holidays = await this.orm.call(
            'hr.leave.type',
            'get_days_all_request',
            [],
            {
                context: context
            }
        );
        this.current_employee = await this.orm.call(
            'hr.leave',
            'get_current_employee',
            [],
            {
                context: context
            }
        );
        this.absentees = await this.orm.call(
            'hr.leave',
            'get_absentees',
            [],
            {
                context: context
            }
        );
        this.current_shift = await this.orm.call(
            'hr.leave',
            'get_current_shift',
            [],
            {
                context: context
            }
        );
        this.upcoming_holidays = await this.orm.call(
            'hr.leave',
            'get_upcoming_holidays',
            [],
            {
                context: context
            }
        );
        this.approval_status_count = await this.orm.call(
            'hr.leave',
            'get_approval_status_count',
            [],
            {
                context: context
            }
        );
        if (this.props.employeeId == null) {
            this.props.employeeId = this.current_employee.id;
        }
//        console.log('popooooooooooooooooooooopopop', this)
    }
});


TimeOffDashboard.components = { TimeOffCard, TimeOffEmpCard ,TimeOffEmpOrgChart, EmpDepartmentCard, ApprovalStatusCard};
TimeOffDashboard.template = 'hr_holidays.TimeOffDashboard';
TimeOffDashboard.props = ['employeeId'];
