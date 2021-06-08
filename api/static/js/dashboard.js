const counter = document.querySelector('.counter');
const hour = document.querySelector('.hour');
const calendarHour = document.querySelector('.calendar-hour');
const calendarDates = document.querySelector('.items.numbers');
const monthYear = document.querySelector('.title.date');
let count = 0;
const d = new Date();

setInterval(function () {
    if (count == 92) {
        clearInterval(count);
    } else {
        count++;
        counter.textContent = count + '%';
    }
}, 42);

setInterval(function currentTime() {
    hour.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    calendarHour.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    return currentTime;
}(), 1000 * 60);

monthYear.textContent = d.toLocaleString('default', { month: 'long' }) + " " + d.getFullYear();

function generateCalendar() {
    const calendarCurrent = calendar().of(d.getFullYear(), d.getMonth());
    let items = '';
    for (week of calendarCurrent.calendar) {
        for (day of week) {
            if (day === d.getDay())
                items += '<div class="item is-active">' + day + '</div>';
            else if (day === 0)
                items += '<div class="item disable"></div>';
            else items += '<div class="item">' + day + '</div>';
        }
    }
    return items
}

calendarDates.innerHTML = generateCalendar();

// TODO calendar, dashboard components, authentication functionality