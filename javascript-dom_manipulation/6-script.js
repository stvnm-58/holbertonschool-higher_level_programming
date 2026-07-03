const characterElement = document.querySelector('#character');

async function getCharacter() {
  const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
  const data = await response.json();
  characterElement.textContent = data.name;
}
getCharacter();
