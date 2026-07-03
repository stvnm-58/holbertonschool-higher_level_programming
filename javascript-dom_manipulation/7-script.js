const characterElement = document.querySelector('#character');

function getCharacter() {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
      characterElement.textContent = data.name;
    });
}
getCharacter();
