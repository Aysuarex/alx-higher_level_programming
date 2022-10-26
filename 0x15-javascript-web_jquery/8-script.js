$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi.co/api/films/?format=json',
    success: function (data) {
      $.each(data.results, function (i, film) {
        $('UL#list_movies').append('<li>' + film.title + '</li>');
      });
    }
  });
});
