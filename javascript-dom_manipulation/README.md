# JavaScript DOM Manipulation

## Description

Ce projet couvre la manipulation du DOM (Document Object Model) avec JavaScript : sélectionner des éléments HTML, modifier leur contenu et leur style, gérer les événements, et interagir dynamiquement avec une page web.

## Qu'est-ce que le DOM ?

Le DOM est une représentation de la page HTML sous forme d'arbre d'objets, que JavaScript peut lire et modifier. Chaque balise HTML (`<div>`, `<p>`, `<h1>`, etc.) devient un nœud accessible et manipulable depuis un script.

## Learning Objectives

À la fin de ce projet, je suis capable d'expliquer sans aide :

- Comment sélectionner un élément HTML depuis JavaScript
- Comment modifier le style d'un élément HTML
- Comment modifier le contenu d'un élément HTML
- Comment ajouter / supprimer une classe CSS à un élément
- Comment écouter et déclencher des événements (`click`, `keyup`, etc.)
- Comment soumettre un formulaire avec JavaScript

## Sélectionner des éléments

```javascript
document.getElementById('mon-id');
document.querySelector('.ma-classe');
document.querySelectorAll('p');
```

| Méthode | Retourne |
|---|---|
| `getElementById` | Un seul élément (par id) |
| `querySelector` | Le premier élément correspondant au sélecteur CSS |
| `querySelectorAll` | Tous les éléments correspondants (liste) |

## Modifier le contenu

```javascript
const titre = document.querySelector('h1');
titre.innerHTML = 'Nouveau titre';
titre.textContent = 'Nouveau titre (sans interpréter le HTML)';
```

`innerHTML` interprète le HTML inséré (attention aux risques d'injection si le contenu vient d'un utilisateur). `textContent` insère du texte brut, sans interprétation.

## Modifier le style

```javascript
const bouton = document.querySelector('button');
bouton.style.backgroundColor = 'blue';
bouton.style.fontSize = '20px';
```

## Manipuler les classes CSS

```javascript
const element = document.querySelector('.carte');
element.classList.add('active');
element.classList.remove('hidden');
element.classList.toggle('selected');
```

`classList.toggle()` ajoute la classe si elle est absente, ou la retire si elle est présente — pratique pour les menus déroulants, les modes sombres, etc.

## Gérer les événements

```javascript
const bouton = document.querySelector('button');
bouton.addEventListener('click', () => {
  console.log('Bouton cliqué !');
});
```

| Événement | Déclenché quand |
|---|---|
| `click` | L'utilisateur clique sur l'élément |
| `keyup` | Une touche du clavier est relâchée |
| `submit` | Un formulaire est soumis |
| `change` | La valeur d'un champ change |

## Soumettre un formulaire en JavaScript

```javascript
const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
  event.preventDefault(); // empêche le rechargement de la page
  console.log('Formulaire envoyé');
});
```

`event.preventDefault()` est essentiel : sans lui, le navigateur recharge la page par défaut à chaque soumission de formulaire.

## Requirements

- Tout le code JavaScript est testé dans un navigateur (console développeur, F12)
- Pas d'utilisation de `var`
- Code conforme aux règles ESLint / semistandard du projet

## Auteur

Madian Limadi