/* Fetches and lists the title for all movies */
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  const films = data.results;
  $.each(films, (i, film) => {
    const title = $('<li></li>').text(film.title);
    $('UL#list_movies').append(title);
  });
});
