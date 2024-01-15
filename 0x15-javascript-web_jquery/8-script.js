$(document).ready(function () {
  function movies (title) {
    const list = `<li>${title}</li>`;
    $('UL#list_movies').append(list);
  }

  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, displayTitle) {
    const moviesData = data.results;
    $.each(moviesData, function (index, movie) {
      displayTitle = movie.title;
      movies(displayTitle);
    });
  });
});
