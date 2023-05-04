/** @odoo-module */

export function usePublicHolidays(props) {
    return (info) => {
        const date = luxon.DateTime.fromJSDate(info.date).toISODate();
        const publicHolidays = props.model.publicHolidays[date];

        if (publicHolidays) {
            info.el.classList.add('fc-public-holiday');
        }
    }
}