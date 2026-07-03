const addItem = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');

function createNewItem() {
  const newLi = document.createElement('li');
  newLi.textContent = 'Item';
  return newLi;
}

addItem.addEventListener('click', function () {
  const item = createNewItem();
  myList.appendChild(item);
});
