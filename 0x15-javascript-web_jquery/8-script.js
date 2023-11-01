// JavaScript script that fetches the character name from this URL:
// https://swapi-api.alx-tools.com/api/people/5/?format=json
// JQuery
$(document).ready(() => {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(url, function (data) {
    $.each(data.results, (i, movie) => {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
