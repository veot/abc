window.onload = () => {
    const sliders = {
        'amount': 'amountDisplay',
        'min': 'minDisplay',
        'max': 'maxDisplay'
    };

    for (const key of Object.keys(sliders)) {
        displaySlider(key, sliders[key])
    }

    const submit = document.getElementById('submit-btn')
    submit.addEventListener('click', draw)
}

const displaySlider = (sliderId, displayId) => {
    const slider = document.getElementById(sliderId);
    const sliderDisplay = document.getElementById(displayId);
    sliderDisplay.innerHTML = slider.value;

    slider.oninput = function() {
        sliderDisplay.innerHTML = this.value;
    }
}

const draw = (e) => {
    const form = document.forms.drawForm;
    let query = "";
    if (form.red.checked) {query += 'red=True&'};
    if (form.green.checked) {query += 'green=True&'};
    if (form.blue.checked) {query += 'blue=True&'};
    query += `amount=${form.amount.value}&`;
    query += `min=${form.min.value}&`;
    query += `max=${form.max.value}`;
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/draw?${query}`);
    xhr.responseType = 'json'
    xhr.onload = () => {
        const data = xhr.response;
        const src = data.path + '?' + new Date().getTime();
        const drawing = document.getElementById('drawing');
        drawing.innerHTML = `<img src=${src} alt="">`;
        const download = document.getElementById('download-btn');
        download.setAttribute('href', data.path);
        download.firstChild.style.cursor = 'pointer';
    };
    xhr.send();
}


