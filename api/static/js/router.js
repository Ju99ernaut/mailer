var icons = document.querySelectorAll('.left-side a svg'),
    subs = document.querySelectorAll('.header-link'),
    homeEl = icons[0],
    mailEl = icons[1],
    settingsEl = icons[2],
    uppyEl;

function deactivateAll(items) {
    for (item of items) {
        item.classList.remove('active');
    }
}

function hide(items) {
    for (item of items) {
        item.style.display = 'none';
    }
}

function show(items) {
    for (item of items) {
        item.style.display = 'flex';
    }
}

function activate(main, sub) {
    main.classList.add('active');
    sub && sub.classList.add('active');
}

function home() {
    deactivateAll(icons);
    deactivateAll(subs);
    hide(subs);
    // TODO Hide All
    // TODO Show home content
    activate(homeEl);
}

function mail() {
    deactivateAll(icons);
    deactivateAll(subs);
    hide(subs);
    // TODO Hide All
    // TODO Show mail content
    activate(mailEl);
}

function settings(subEl) {
    deactivateAll(icons);
    deactivateAll(subs);
    show(subs);
    // TODO Hide All
    // TODO Show settings content
    activate(settingsEl, document.querySelector('.' + subEl));
}

var routes = {
    '/home': home,
    '/mail': mail,
    '/settings/:subMenu': settings
}

var router = Router(routes);

router.init();