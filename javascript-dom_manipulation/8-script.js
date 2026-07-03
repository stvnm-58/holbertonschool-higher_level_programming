document.addEventListener('DOMContentLoaded', async function () {
  const helloElement = document.querySelector('#hello');
  const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
  const data = await response.json();
  helloElement.textContent = data.hello;
});
