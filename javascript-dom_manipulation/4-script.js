// script.js
document.addEventListener('DOMContentLoaded', function () {
  // Sélectionner le bouton avec l'id "add_item"
  const addItem = document.getElementById('add_item');

  // Ajouter un écouteur d'événement "click"
  addItem.addEventListener('click', function () {
    // Créer un nouvel élément <li>
    const newItem = document.createElement('li');

    // Ajouter le texte "Item" à l'élément
    newItem.textContent = 'Item';

    // Sélectionner la liste <ul> avec la classe "my_list"
    const list = document.querySelector('ul.my_list');

    // Ajouter le nouvel élément à la liste
    list.appendChild(newItem);
  });
});
