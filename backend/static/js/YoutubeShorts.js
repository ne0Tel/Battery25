// Вертикальный слайдер для Shorts
const shortsSplider = new Splide('.splide', {
  type: 'loop',
  direction: 'ttb',
  height: '800px',
  arrows: false,
  pagination: false,
  wheel: true,
});

const sliderShorts = document.querySelectorAll('.slider-shorts-youtube .slick-slide');
let countSliderShorts = 0;
for (let i = 0; i < sliderShorts.length; i++) {
  if (sliderShorts[i].classList.contains('slick-cloned')) {
    continue;
  }
  countSliderShorts++;

  sliderShorts[i].querySelector('video').setAttribute('id', `id_slider_shorts_youtube_${countSliderShorts}`);
  document.querySelector('.splide__list').appendChild(createLiSlideSplide(countSliderShorts));
}

// Инициализация видеоплееров Plyr
const players = document.querySelectorAll('.splide__slide video');
let splideSlide = 1;


players.forEach((player, index) => {
  if (splideSlide === 5) splideSlide = 1;

  new Plyr(`#id_video_player_${index + 1}`, { ratio: '9:16', loop: {active: true}, fullscreen: {enabled: false,}, controls: [],}
  ).source = {
    type: 'video',
    title: `video_${index + 1}`,
    sources: [
    {
      src: `{% static 'video/video_1.mp4' %}`,
      type: 'video/mp4',
    }],
  }
  
  splideSlide++;
  player.plyr.muted = false;
});

shortsSplider.mount();

// Модальное окно Shorts и кнопка закрытия
const modalShorts = document.getElementById('id_youtube_shorts_modal');
const btnCloseShorts = document.getElementById('id_close_shorts');

// Инициализация кнопоки выключения звука
const btnsVolume = document.querySelectorAll('.volume-btn');
btnsVolume.forEach((btn)=> {
  btn.addEventListener("click", mutedVideo);
})

// Открыть модальное окно
for (let i = 0; i < players.length; i++) {
document.querySelector(`#id_slider_shorts_youtube_${i + 1}`).addEventListener('click', () => {
    modalShorts.classList.add('youtube-shorts-modal-show');
    shortsSplider.go(i);
    videoPlayback();
  });
}

// Закрыть модальное окно и прекратить воспроизведение
btnCloseShorts.addEventListener('click', () => {
  modalShorts.classList.remove('youtube-shorts-modal-show');
  players.forEach((player) => {
    player.plyr.stop();
  });
});

// Выключать следующее и предыдущее видео, включать текущее
shortsSplider.on('moved', () => {
  videoPlayback();
});

function videoPlayback () {
  const slides = document.querySelectorAll('.splide__slide');
  let count = 0;
  for (let i = 0; i < slides.length; i++) {
    if (slides[i].classList.contains('splide__slide--clone')) {
      continue;
    }

    if (slides[i].classList.contains('is-active')) {
      players[count].plyr.play();
      
    } else {
      players[count].plyr.stop();
    }
    count++;
  }
  
}

function mutedVideo () {
  const imgsVolume = document.querySelectorAll('#id_volume_btn');

  if (imgsVolume[0].dataset.muted === 'false'){
    imgsVolume.forEach((imgVolume, index) => {
      imgVolume.src = "{% static 'img/shorts/mute-shorts.png' %}"
      imgVolume.dataset.muted = 'true';
      players[index].plyr.muted = true;
    })
  } else{
    imgsVolume.forEach((imgVolume, index) => {
      imgVolume.src = "{%  static 'img/shorts/volume-shorts.png' %}"
      imgVolume.dataset.muted = 'false';
      players[index].plyr.muted = false;
    })
  }
}

function createLiSlideSplide(idVideo) {
  const slide = document.createElement('li');
  slide.classList.add('splide__slide');

  // Элемен видео
  const video = document.createElement('video');
  video.controls = true;
  video.playsinline = true;
  video.setAttribute("id", `id_video_player_${idVideo}`)
  slide.appendChild(video);

  // Контейнер для кнопок соц.активности
  const btnsContainer = document.createElement('div');
  btnsContainer.classList.add('btns-shorts-active');

  // Кнопка громкости
  const volumeBtn = document.createElement('div');
  volumeBtn.classList.add('volume-btn');

  const volumeImg = document.createElement('img');
  volumeImg.id = 'id_volume_btn';
  volumeImg.src = "{% static 'img/shorts/volume-shorts.png' %}";
  volumeImg.alt = 'icon';
  volumeImg.dataset.muted = 'false';
  volumeBtn.appendChild(volumeImg);

  btnsContainer.appendChild(volumeBtn);
  slide.appendChild(btnsContainer);

  return slide;
}