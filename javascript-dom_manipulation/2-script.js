const redHeader = document.querySelector('#red_header');
const header = document.querySelector('header');

function rendreRouge() {
  header.classList.add('red');
}

redHeader.addEventListener('click', rendreRouge);
