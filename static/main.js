window.onload = () => {
  const sliders = {
    amount: 'amountDisplay',
    min: 'minDisplay',
    max: 'maxDisplay',
  };

  for (const key of Object.keys(sliders)) {
    displaySlider(key, sliders[key]);
  }

  const submit = document.getElementById('submit-btn');
  submit.addEventListener('click', draw);
};

const displaySlider = (sliderId, displayId) => {
  const slider = document.getElementById(sliderId);
  const sliderDisplay = document.getElementById(displayId);
  sliderDisplay.innerHTML = slider.value;

  slider.oninput = function () {
    sliderDisplay.innerHTML = this.value;
  };
};

const draw = () => {
  const form = document.forms.drawForm;
  let query = '';
  form.red.checked ? (query += 'red=true&') : (query += 'red=false&');
  form.green.checked ? (query += 'green=true&') : (query += 'green=false&');
  form.blue.checked ? (query += 'blue=true&') : (query += 'blue=false&');
  query += `amount=${form.amount.value}&`;
  query += `min_r=${form.min.value}&`;
  query += `max_r=${form.max.value}`;
  const xhr = new XMLHttpRequest();
  fetch(`/draw?${query}`)
    .then((res) => {
      return res.json();
    })
    .then((data) => {
      const src = data.path;
      const drawing = document.getElementById('drawing');
      drawing.innerHTML = `<img src=${src} alt="generated image">`;
      const download = document.getElementById('download-btn');
      download.setAttribute('href', data.path);
      download.firstChild.style.cursor = 'pointer';
    })
    .catch((err) => {
      console.log('Something went wrong', err);
    });
};
