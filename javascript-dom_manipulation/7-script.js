document.addEventListener('DOMContentLoaded', function () {
  const movieList = document.getElementById('list_movies');

  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      data.results.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        movieList.appendChild(listItem);
      });
    })
    .catch(error => console.error('Erreur:', error));
});
