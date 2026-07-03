const toggleHeader = document.querySelector('#toggle_header');
const header = document.querySelector('header');

function switchColors() {
  if (header.className === 'red') {
    header.className = 'green';
  } else {
    header.className = 'red';
  }
}

toggleHeader.addEventListener('click', switchColors);
