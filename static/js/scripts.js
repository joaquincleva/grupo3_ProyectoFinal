const cardContainer = document.querySelector('.cardo-container');
const cardo = cardContainer.querySelector('.cardo');

cardContainer.addEventListener('click', function() {
  cardo.classList.toggle('flipped');
});