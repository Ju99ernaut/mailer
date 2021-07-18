const input = document.querySelector('input');
const btn = document.querySelector('button');

window.NewsletterWidget = {
    action(ev) {
        fetch('/newsletter/' + this.type + '?email=' + this.input.value);
    },
    init(options) {
        this.type = options.type || 'subscribe';
        if (typeof options.container === 'string') {
            options.container = document.querySelector(options.container);
        }
        this.container = options.container;
        const cont = document.createElement('div');
        cont.className = 'card-form__inner';
        cont.innerHTML = '<div class="card-input">' +
            '<label for="email" class="card-input__label">Email Address</label>' +
            '<input type="email" id="email" placeholder="user@example.com" class="card-input__input" autocomplete="off">' +
            '</div>' +
            '<button class="card-form__button">' +
            '</button>';
        options.container.append(cont);
        this.input = options.container.querySelector('input');
        this.btn = options.container.querySelector('button');
        this.btn.innerText = this.type === 'subscribe' ? 'Subscribe' : 'Unsubscribe';
        this.btn.addEventListener('click', this.action.bind(this));
    }
}

btn.addEventListener('click', action);

function action(ev) {
    const actionType = ev.currentTarget.innerText.trim().toLowerCase();
    if (actionType === 'subscribe' || actionType === 'unsubscribe')
        fetch('/newsletter/' + actionType + '?email=' + input.value);
    else if (actionType === 'login') {
        const form = document.querySelector('form');
        fetch('/auth', {
            method: 'POST',
            body: new FormData(form)
        })
            .then(res => res.json())
            .then(res => {
                if (res.access_token === 200) {
                    localStorage.setItem('token', JSON.stringify(res));
                    window.location.replace('/dashboard');
                } else {
                    form.reset();
                }
            })
            .catch(err => console.log(err));
    }
    else if (actionType === 'register') {
        const usernameEl = document.querySelector('#username');
        const emailEl = document.querySelector('#email');
        const passwordEl = document.querySelector('#password');
        const username = usernameEl.value;
        const email = emailEl.value;
        const password = passwordEl.value;

        fetch('/register', {
            method: 'POST',
            body: JSON.stringify({ username, email, password })
        })
            .then(res => {
                if (res.status === 200) {
                    window.location.replace('/edit/login')
                } else {
                    usernameEl.value = '';
                    emailEl.value = '';
                    passwordEl.value = '';
                }
            })
            .catch(err => console.log(err));
    }
}