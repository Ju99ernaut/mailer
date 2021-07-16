const counter = document.querySelector('.counter');
const hour = document.querySelector('.hour');
const calendarHour = document.querySelector('.calendar-hour');
const calendarDates = document.querySelector('.items.numbers');
const calendarNext = document.querySelector('.title.next');
const calendarPrev = document.querySelector('.title.prev');
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

function generateCalendar(opts = { year: d.getFullYear(), month: d.getMonth() }) {
    const { year, month } = opts;
    const calendarCurrent = calendar().of(year, month);
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

monthYear.textContent = d.toLocaleString('default', { month: 'long' }) + " " + d.getFullYear();
calendarDates.innerHTML = generateCalendar();
itemEvents();

calendarPrev.addEventListener('click', prevNext);
calendarNext.addEventListener('click', prevNext);

function prevNext(e) {
    // TODO Handle prev next
    const year = d.getFullYear(); //+ 1;
    const month = d.getMonth() + 1;
    // TODO Handle calendar title
    monthYear.textContent = d.toLocaleString('default', { month: 'long' }) + " " + d.getFullYear();
    calendarDates.innerHTML = generateCalendar({ year, month });
    itemEvents();
};

function itemEvents() {
    const items = document.querySelectorAll('.items.numbers .item');
    items.addEventListener('click', function (e) {
        deactivateAllDates();
        activateDate(e);
    });
}

function activateDate(e) {
    e.currentTarget.classList.add('is-active');
};

function deactivateAllDates() {
    const items = document.querySelectorAll('.items.numbers .item');
    for (item of items) {
        item.classList.remove('is-active');
    }
};

// TODO calendar, dashboard components, authentication functionality