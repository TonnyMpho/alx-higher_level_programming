// avaScript script that fetches and lists the title for all movies by using this URL:
// https://swapi-api.alx-tools.com/api/films/?format=json
// JQuery
$(document).ready(() => {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data) {
    $.each(data.results, (i, movie) => {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
