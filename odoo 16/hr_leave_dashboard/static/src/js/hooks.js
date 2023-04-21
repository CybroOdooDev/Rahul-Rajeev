/** @odoo-module */

export function usePublicHolidays(props) {
    return (info) => {
        const date = luxon.DateTime.fromJSDate(info.date).toISODate();
        const publicHolidays = props.model.publicHolidays[date];

        if (publicHolidays) {
//         console.log('date',date)
//        console.log('publicHolidays', publicHolidays)
//        console.log('info', info)
            info.el.classList.add('fc-public-holiday');
        }
    }
}