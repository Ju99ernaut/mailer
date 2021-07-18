const counter = document.querySelector('.counter');
const hour = document.querySelector('.hour');
const calendarHour = document.querySelector('.calendar-hour');
const calendarDates = document.querySelector('.items.numbers');
const calendarNext = document.querySelector('.title.next');
const calendarPrev = document.querySelector('.title.prev');
const monthYear = document.querySelector('.title.date');
let count = 0;
const d = new Date();
let currentMonth = d.getMonth();
let currentYear = d.getFullYear();

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

function generateCalendar(opts = { year: currentYear, month: currentMonth }) {
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
    return { items, year, month: calendarCurrent.month }
}

monthYear.textContent = d.toLocaleString('default', { month: 'long' }) + " " + currentYear;
calendarDates.innerHTML = generateCalendar().items;
itemEvents();

calendarPrev.addEventListener('click', prevNext);
calendarNext.addEventListener('click', prevNext);

function prevNext(e) {
    const nextMonth = e.currentTarget.classList.contains('next') ? 1 : -1;
    currentMonth += nextMonth;
    currentYear = currentMonth > 11 ? (currentYear + 1) :
        (currentMonth < 0 ? (currentYear - 1) : currentYear);
    currentMonth = currentMonth > 11 ? 0 : (currentMonth < 0 ? 11 : currentMonth);

    const { items, year, month } = generateCalendar({ year: currentYear, month: currentMonth });
    monthYear.textContent = month + " " + year;
    calendarDates.innerHTML = items;
    itemEvents();
};

function itemEvents() {
    const items = document.querySelectorAll('.items.numbers .item');
    for (item of items) {
        item.addEventListener('click', function (e) {
            deactivateAllDates();
            activateDate(e);
        });
    }
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

// TODO mail config
const saveCampaignConfigBtn = document.querySelector('.fourth-box .cards-button.button');
const saveUppyConfigBtn = document.querySelector('.fifth-box .cards-button.button');

saveCampaignConfigBtn.addEventListener('click', updateCampaignConfig);
saveUppyConfigBtn.addEventListener('click', updateUppyConfig);

function updateCampaignConfig() {
    const form = document.querySelector('form.campaign-config');
    fetch('/campaigns/setup', {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(new FormData(form)))
    })
        .then(res => res.json())
        .then(res => console.log(res))
        .catch(err => console.log(err));
}

function updateUppyConfig() {
    const form = document.querySelector('form.uppy-config');
    fetch('/assets/uppy', {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(new FormData(form)))
    })
        .then(res => res.json())
        .then(res => console.log(res))
        .catch(err => console.log(err));
}