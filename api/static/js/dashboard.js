var counter = document.querySelector(".counter");
var count = 0;
setInterval(function () {
    if (count == 92) {
        clearInterval(count);
    } else {
        count += 1;
        counter.textContent = count + "%";
    }
}, 42);
