const redHeader = document.querySelector('#red_header');

function passerLeHeaderEnRouge() {
  document.querySelector('header').style.color = '#FF0000';
}
redHeader.addEventListener('click', passerLeHeaderEnRouge);