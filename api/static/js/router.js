var icons = document.querySelectorAll('.left-side a svg'),
    subs = document.querySelectorAll('.header-link'),
    box1 = document.querySelector('.first-box'),
    box2 = document.querySelector('.second-box'),
    box3 = document.querySelector('.third-box'),
    box4 = document.querySelector('.fourth-box'),
    box5 = document.querySelector('.fifth-box'),
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
    // * Hide All
    box3.style.display = 'none';
    box4.style.display = 'none';
    box5.style.display = 'none';
    // * Show home content
    box1.style.display = 'flex';
    box2.style.display = 'flex';
    activate(homeEl);
}

function mail() {
    deactivateAll(icons);
    deactivateAll(subs);
    hide(subs);
    // * Hide All
    box1.style.display = 'none';
    box2.style.display = 'none';
    box4.style.display = 'none';
    box5.style.display = 'none';
    // * Show mail content
    box3.style.display = 'flex';
    activate(mailEl);
}

function settings(subEl) {
    deactivateAll(icons);
    deactivateAll(subs);
    show(subs);
    // * Hide All
    box1.style.display = 'none';
    box2.style.display = 'none';
    box3.style.display = 'none';
    // * Show settings content
    if (subEl && subEl === 'config') {
        box4.style.display = 'flex';
        box5.style.display = 'none';
    } else if (subEl && subEl === 'uppy') {
        box4.style.display = 'none';
        box5.style.display = 'flex';
    } else {
        box4.style.display = 'none';
        box5.style.display = 'none';
    }
    activate(settingsEl, document.querySelector('.' + subEl));
}

var routes = {
    '/home': home,
    '/mail': mail,
    '/settings/:subMenu': settings
}

var router = Router(routes);

router.init();