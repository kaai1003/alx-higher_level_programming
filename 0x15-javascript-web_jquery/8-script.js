/* global $ */
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const result = data.results;
    for (const film of result) {
      $('#list_movies').append('<li>' + film.title + '</li>');
    }
  });
});
