$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const list = $('UL#list_movies');
    data.results.forEach(movie => {
      list.append('<LI>' + movie.title + '</LI>');
    });
  });
});
