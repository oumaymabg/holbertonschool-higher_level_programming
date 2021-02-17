$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: (r) => {
    $.each(r.results, (index, movie) => {
      $('<li>' + movie.title + '</li>').appendTo('UL#list_movies');
    });
  }
});
