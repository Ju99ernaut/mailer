var input = document.querySelector('input');
var btn = document.querySelector('button');

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
    fetch('/newsletter/' + ev.currentTarget.innerText.trim().toLowerCase() + '?email=' + input.value);
}